"""验证新增语言、完整 YAML 和配置失败路径"""

from __future__ import annotations

import contextlib
import io
import pathlib
import sys
import tempfile
import unittest


sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
from check_repo import collect_paths, run
from repo_rules import check_text
from source_catalog import parse_source_groups
from validate_skill import parse_yaml, validate_metadata, validate_root, yaml


class ExtensibleSourceTests(unittest.TestCase):
    """新语言能够获得与内置语言相同的规模约束"""

    def test_custom_suffixes_are_scanned_and_counted_together(self):
        """未知后缀声明后参与全量发现及混合后缀计数"""
        with tempfile.TemporaryDirectory() as folder:
            root = pathlib.Path(folder).resolve()
            custom = parse_source_groups(["Nim=.nim,.nims"])
            for index in range(21):
                suffix = ".nim" if index % 2 == 0 else ".nims"
                (root / f"part{index}{suffix}").write_bytes(b"discard\n")
            self.assertEqual(21, len(collect_paths(root, [], [], custom)))
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(
                io.StringIO()
            ):
                self.assertEqual(1, run(root, [], [], False, custom))
                self.assertEqual(1, run(root, ["part0.nim"], [], False, custom))

    def test_custom_language_line_limit(self):
        """新增语言默认不得超过 380 行"""
        custom = parse_source_groups(["Nim=.nim"])
        path = pathlib.Path("module.nim")
        self.assertFalse(check_text(path, b"discard\n" * 380, custom)[0])
        self.assertTrue(check_text(path, b"discard\n" * 381, custom)[0])

    def test_invalid_groups_and_builtin_override_are_rejected(self):
        """错误参数与拆分内置技术族的尝试必须失败"""
        for value in (
            "Nim",
            "=.nim",
            "Nim=nim",
            "Nim=.nim,",
            "Split=.ts",
            "Nim=.../escape",
        ):
            with self.subTest(value=value), self.assertRaises(ValueError):
                parse_source_groups([value])
        with self.assertRaises(ValueError):
            parse_source_groups(["One=.toy", "Two=.toy"])

    def test_custom_groups_do_not_leak_between_runs(self):
        """声明的后缀只影响本次调用，不污染模块全局状态"""
        first = parse_source_groups(["One=.toy"])
        self.assertEqual({".toy": "One"}, first)
        self.assertEqual({}, parse_source_groups([]))


class StrictMetadataTests(unittest.TestCase):
    """正规解析需要拒绝正则字段检查无法识别的错误"""

    def test_multiline_yaml_description_is_valid(self):
        """合法 YAML 标量应按正规解析结果检查"""
        text = "---\nname: demo-skill\ndescription: >-\n  第一行说明\n  第二行说明\nmetadata:\n  version: '1.0'\n---\n"
        self.assertEqual("demo-skill", validate_metadata(text)["name"])

    def test_malformed_and_duplicate_yaml_fail(self):
        """未闭合引号、重复字段及非映射根节点必须失败"""
        for text in (
            'name: "unterminated',
            "name: one\nname: two\n",
            "- a\n- b\n",
            "value: !!python/object:builtins.object {}",
        ):
            with self.subTest(text=text), self.assertRaises(
                (ValueError, yaml.YAMLError)
            ):
                parse_yaml(text)

    def test_metadata_values_must_be_strings(self):
        """数字版本不能悄悄变为不符合 Skill 规范的类型"""
        text = "---\nname: demo\ndescription: 中文说明\nmetadata:\n  version: 1\n---\n"
        with self.assertRaises(ValueError):
            validate_metadata(text)

    def test_metadata_input_is_bounded(self):
        """超大配置应在解析前拒绝"""
        with self.assertRaises(ValueError):
            parse_yaml("description: " + "字" * 30_000)

    def test_agent_and_workflow_files_are_validated(self):
        """真实根目录的 UI 与 CI 语法错误不能被忽略"""
        with tempfile.TemporaryDirectory() as folder:
            root = pathlib.Path(folder)
            (root / "SKILL.md").write_text(
                "---\nname: demo\ndescription: 中文说明\n---\n", encoding="utf-8"
            )
            (root / "agents").mkdir()
            (root / ".github/workflows").mkdir(parents=True)
            ui = root / "agents/openai.yaml"
            ui.write_text(
                "interface:\n  short_description: '"
                + "中" * 25
                + "'\n  default_prompt: '使用 $demo'\n",
                encoding="utf-8",
            )
            validate_root(root)
            workflow = root / ".github/workflows/check.yml"
            workflow.write_text('name: "unterminated', encoding="utf-8")
            with self.assertRaises(yaml.YAMLError):
                validate_root(root)
            workflow.unlink()
            ui.write_text(
                "interface:\n  short_description: short\n  default_prompt: wrong\n",
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                validate_root(root)


if __name__ == "__main__":
    unittest.main()
