"""验证检查器对真实格式、路径边界和规模问题的识别"""

from __future__ import annotations

import contextlib
import io
import pathlib
import sys
import tempfile
import unittest


sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
from check_repo import collect_paths, run
from repo_rules import check_frontmatter, check_links, check_text
from source_catalog import check_source_counts


class TextRuleTests(unittest.TestCase):
    """覆盖格式边界，不依赖固定错误文字"""

    def test_chinese_lf_and_gofmt_tab_are_valid(self):
        """中文和 Go 标准缩进不能被通用空白规则误拒绝"""
        errors, _ = check_text(
            pathlib.Path("main.go"),
            "package main\n\nfunc main() {\n\t// 保留标准缩进\n}\n".encode(),
        )
        self.assertEqual([], errors)

    def test_bom_crlf_and_missing_newline_fail(self):
        """不同非法编码与行尾均能造成失败"""
        for data in (
            b"\xef\xbb\xbfvalue\n",
            b"value\r\n",
            b"value",
            b"value\n\n",
            b"value \n",
            b"\xff",
        ):
            with self.subTest(data=data):
                self.assertTrue(check_text(pathlib.Path("a.py"), data)[0])

    def test_source_limits_include_comments_and_blank_lines(self):
        """按物理行计数，恰好上限通过，超出失败"""
        for suffix, limit in ((".java", 360), (".go", 360), (".py", 380), (".sv", 380)):
            with self.subTest(suffix=suffix):
                good = ("// 说明\n" * limit).encode()
                self.assertFalse(check_text(pathlib.Path("a" + suffix), good)[0])
                self.assertTrue(
                    check_text(pathlib.Path("a" + suffix), good + b"extra\n")[0]
                )

    def test_java_width_is_checked(self):
        """Java 超长行应被拒绝"""
        self.assertFalse(
            check_text(pathlib.Path("A.java"), ("a" * 120 + "\n").encode())[0]
        )
        self.assertTrue(
            check_text(pathlib.Path("A.java"), ("a" * 121 + "\n").encode())[0]
        )


class StructureTests(unittest.TestCase):
    """验证链接、元数据和文件范围"""

    def test_metadata_required_and_duplicate_fields(self):
        """缺字段、非法名称和重复声明不能静默通过"""
        good = "---\nname: valid-skill\ndescription: 中文说明\n---\n"
        self.assertFalse(check_frontmatter(good))
        for bad in (
            "# 正文\n",
            good.replace("valid-skill", "Invalid"),
            good.replace("description: 中文说明\n", ""),
            good.replace("---\nname", "---\nname: another\nname", 1),
        ):
            with self.subTest(bad=bad):
                self.assertTrue(check_frontmatter(bad))

    def test_local_links_and_fenced_examples(self):
        """只检查真实本地文件链接，不访问网络或误判围栏示例"""
        with tempfile.TemporaryDirectory() as folder:
            root = pathlib.Path(folder).resolve()
            path = root / "SKILL.md"
            (root / "中文 文件.md").write_text("正文\n", encoding="utf-8")
            good = "[文件](<中文 文件.md>)\n[外部](https://example.org/x)\n```text\n[示例](missing.md)\n```\n"
            self.assertEqual([], check_links(path, root, good))
            self.assertTrue(check_links(path, root, "[缺失](missing.md)\n"))
            self.assertTrue(check_links(path, root, "[越界](../outside.md)\n"))
            self.assertTrue(check_links(path, root, "[编码越界](%2e%2e/outside.md)\n"))

    def test_go_count_is_per_directory(self):
        """子目录独立计数，父包超过 20 个时失败"""
        with tempfile.TemporaryDirectory() as folder:
            root = pathlib.Path(folder)
            child = root / "child"
            child.mkdir()
            for index in range(20):
                (root / f"a{index}.go").touch()
                (child / f"b{index}.go").touch()
            self.assertFalse(check_source_counts([root / "a0.go", child / "b0.go"]))
            (root / "extra_test.go").touch()
            self.assertEqual(1, len(check_source_counts([root / "a0.go"])))

    def test_all_languages_obey_twenty_file_limit(self):
        """常见语言不能仅因不是 Go 而绕过目录上限"""
        for suffix in (
            ".java",
            ".py",
            ".rs",
            ".vue",
            ".swift",
            ".kt",
            ".sql",
            ".dart",
            ".sv",
        ):
            with self.subTest(suffix=suffix), tempfile.TemporaryDirectory() as folder:
                root = pathlib.Path(folder)
                for index in range(21):
                    (root / f"part{index}{suffix}").touch()
                self.assertTrue(check_source_counts([root / ("part0" + suffix)]))

    def test_related_suffixes_and_tests_are_counted_together(self):
        """混合后缀、测试与生成文件名不能绕过同类计数"""
        for suffixes in (
            (".js", ".tsx", ".ts"),
            (".c", ".hpp", ".cpp"),
            (".py", ".pyi"),
            (".css", ".scss"),
        ):
            with self.subTest(
                suffixes=suffixes
            ), tempfile.TemporaryDirectory() as folder:
                root = pathlib.Path(folder)
                for index in range(21):
                    suffix = suffixes[index % len(suffixes)]
                    name = f"generated_part_{index}_test{suffix}"
                    (root / name).touch()
                selected = [root / ("generated_part_0_test" + suffixes[0])]
                self.assertEqual(1, len(check_source_counts(selected)))

    def test_selection_and_exclusions_are_enforced(self):
        """限定文件和排除路径不影响其他目录"""
        with tempfile.TemporaryDirectory() as folder:
            root = pathlib.Path(folder).resolve()
            (root / "a.py").write_text("pass\n", encoding="utf-8")
            (root / "node_modules").mkdir()
            (root / "node_modules/x.js").write_text("bad", encoding="utf-8")
            self.assertEqual([root / "a.py"], collect_paths(root, [], []))
            self.assertEqual([], collect_paths(root, [], ["*.py"]))
            with self.assertRaises(ValueError):
                collect_paths(root, ["../escape.py"], [])

    def test_cli_result_reflects_real_failures(self):
        """有效项目与格式损坏项目返回不同状态，空范围不能伪造通过"""
        with tempfile.TemporaryDirectory() as folder:
            root = pathlib.Path(folder).resolve()
            path = root / "sample.py"
            path.write_bytes(b"pass\n")
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(
                io.StringIO()
            ):
                self.assertEqual(0, run(root, [], [], False))
                path.write_bytes(b"pass\r\n")
                self.assertEqual(1, run(root, [], [], False))
                self.assertEqual(1, run(root, [], ["*.py"], False))
                self.assertEqual(1, run(root, [], [], True))


if __name__ == "__main__":
    unittest.main()
