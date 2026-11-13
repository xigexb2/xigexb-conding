"""验证缺失译文、错链、来源漂移与命令行语言的可观察行为"""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from check_translations import check
from diagnostics import localize
from validate_skill import validate_root


class TranslationTests(unittest.TestCase):
    """使用隔离的最小双语目录验证实际失败条件"""

    def setUp(self):
        """为每个场景建立独立文档树"""
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.write("README.md", "# Demo\n\n[中文](README.zh-CN.md)\n")
        self.write("README.zh-CN.md", "# 示例\n\n[English](README.md)\n")
        self.write(
            "references/rules.md",
            "# Rules\n\n[中文](zh-CN/rules.md)\n\n## A01 Contract\n\n"
            "[Source](https://example.com/spec)\n",
        )
        self.write(
            "references/zh-CN/rules.md",
            "# 规则\n\n[English](../rules.md)\n\n## A01 契约\n\n"
            "[来源](https://example.com/spec)\n",
        )

    def write(self, name: str, text: str):
        """统一写入 UTF-8 与 LF，避免测试环境改变换行"""
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")

    def test_complete_tree_passes(self):
        """两组完整文档可以通过"""
        self.assertEqual((2, []), check(self.root))

    def test_new_document_requires_translation(self):
        """新增英文文档不能绕过覆盖发现"""
        self.write("references/new.md", "# New\n")
        count, errors = check(self.root)
        self.assertEqual(3, count)
        self.assertTrue(errors)

    def test_reverse_navigation_is_required(self):
        """只有单向链接的译文必须失败"""
        self.write("README.zh-CN.md", "# 示例\n")
        self.assertTrue(check(self.root)[1])

    def test_rule_identity_and_source_changes_fail(self):
        """规则编号或权威来源变化均应可检测"""
        path = self.root / "references/zh-CN/rules.md"
        original = path.read_text(encoding="utf-8")
        for changed in (
            original.replace("A01", "A02"),
            original.replace("example.com/spec", "example.com/other"),
        ):
            with self.subTest(changed=changed):
                self.write("references/zh-CN/rules.md", changed)
                self.assertTrue(check(self.root)[1])

    def test_unclosed_fence_and_orphans_fail(self):
        """被代码围栏隐藏的正文和无原文译文必须失败"""
        self.write("README.zh-CN.md", "# 示例\n\n[English](README.md)\n\n```text\n")
        self.assertTrue(check(self.root)[1])
        self.write("README.zh-CN.md", "# 示例\n\n[English](README.md)\n")
        self.write("references/zh-CN/orphan.md", "# 无原文\n")
        self.assertTrue(check(self.root)[1])

    def test_internal_links_stay_in_selected_language(self):
        """跨篇导航不能意外跳进另一语言树"""
        path = self.root / "README.zh-CN.md"
        original = path.read_text(encoding="utf-8")
        self.write("README.zh-CN.md", original + "\n[规则](references/rules.md)\n")
        self.assertTrue(check(self.root)[1])
        self.write(
            "README.zh-CN.md", original + "\n[规则](references/zh-CN/rules.md)\n"
        )
        self.assertFalse(check(self.root)[1])

    def test_unrelated_nested_skill_is_not_discovered(self):
        """中文入口不使用第二个 SKILL.md，避免同名技能重复发现"""
        self.write("SKILL.md", "# Skill\n\n[中文](SKILL.zh-CN.md)\n")
        self.write("SKILL.zh-CN.md", "# 技能\n\n[English](SKILL.md)\n")
        self.assertEqual(1, len(list(self.root.rglob("SKILL.md"))))
        self.assertFalse(check(self.root)[1])


class LocaleTests(unittest.TestCase):
    """诊断语言选择不能改变验证结果或用户提供的路径"""

    def test_cli_languages_have_same_failure_status(self):
        """实际 CLI 在两种语言下都拒绝缺少末尾换行的文件"""
        with tempfile.TemporaryDirectory() as folder:
            (Path(folder) / "sample.py").write_bytes(b"pass")
            for language, expected in (
                ("en", "must end with LF"),
                ("zh-CN", "以 LF 结束"),
            ):
                result = subprocess.run(
                    [
                        sys.executable,
                        "-B",
                        "-X",
                        "utf8",
                        str(SCRIPTS / "check_repo.py"),
                        folder,
                        "--lang",
                        language,
                    ],
                    capture_output=True,
                    encoding="utf-8",
                    check=False,
                    env={**os.environ, "PYTHONUTF8": "1"},
                )
                self.assertEqual(1, result.returncode)
                self.assertIn(expected, result.stderr)

    def test_user_path_survives_localization(self):
        """不能翻译用户路径或把中文文件名改成其他值"""
        message = "目标必须是根目录内已存在的文件：数据/设备.py"
        self.assertTrue(localize(message).endswith("数据/设备.py"))
        self.assertEqual(message, localize(message, "zh-CN"))

    def test_localized_metadata_is_validated(self):
        """备选 Agent 配置的错误也必须被元数据检查发现"""
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "SKILL.md").write_text(
                "---\nname: demo\ndescription: Demo\n---\n", encoding="utf-8"
            )
            (root / "agents").mkdir()
            (root / "agents/openai.zh-CN.yaml").write_text(
                "interface:\n  short_description: too short\n  default_prompt: '$demo'\n",
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                validate_root(root)


if __name__ == "__main__":
    unittest.main()
