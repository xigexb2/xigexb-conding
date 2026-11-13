"""检查文本与 Skill 的机械约束，不修改文件，也不访问网络"""

from __future__ import annotations

import argparse
import fnmatch
import os
import sys
from pathlib import Path

from repo_rules import (
    TEXT_NAMES,
    TEXT_SUFFIXES,
    check_frontmatter,
    check_links,
    check_text,
)
from source_catalog import check_source_counts, parse_source_groups


EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "vendor",
    "target",
    "dist",
    "build",
    "__pycache__",
    ".idea",
    ".vscode",
    ".next",
    ".nuxt",
    ".output",
    ".gradle",
    "coverage",
}


def is_excluded(path: Path, root: Path, patterns: list[str]) -> bool:
    """应用目录默认排除与用户明确给出的路径模式"""
    relative = path.relative_to(root)
    if any(part in EXCLUDED_DIRS for part in relative.parts):
        return True
    name = relative.as_posix()
    return any(fnmatch.fnmatchcase(name, pattern) for pattern in patterns)


def collect_paths(
    root: Path,
    selected: list[str],
    patterns: list[str],
    custom: dict[str, str] | None = None,
) -> list[Path]:
    """选定路径必须存在且位于根内，默认不遍历符号链接目录"""
    if selected:
        result = []
        for value in selected:
            path = (root / value).resolve()
            if not path.is_relative_to(root) or not path.is_file():
                raise ValueError(f"目标必须是根目录内已存在的文件：{value}")
            if not is_excluded(path, root, patterns):
                result.append(path)
        return sorted(set(result))
    result = []

    def on_error(error: OSError) -> None:
        """无法读取目录时使检查失败，不把遗漏伪装为成功"""
        raise error

    for folder, dirs, names in os.walk(root, followlinks=False, onerror=on_error):
        parent = Path(folder)
        dirs[:] = [
            name
            for name in dirs
            if not (parent / name).is_symlink()
            and not is_excluded(parent / name, root, patterns)
        ]
        for name in names:
            path = parent / name
            if path.is_symlink() or is_excluded(path, root, patterns):
                continue
            if (
                path.suffix in TEXT_SUFFIXES
                or name in TEXT_NAMES
                or (custom and path.suffix in custom)
            ):
                result.append(path)
    return sorted(result)


def run(
    root: Path,
    selected: list[str],
    patterns: list[str],
    require_skill: bool,
    custom: dict[str, str] | None = None,
) -> int:
    """聚合独立失败，非零状态阻止 CI 将不完整验证当作通过"""
    paths = collect_paths(root, selected, patterns, custom)
    failures = []
    if not paths:
        failures.append((root, "检查范围没有可读取的目标文件"))
    if require_skill and not (root / "SKILL.md").is_file():
        failures.append((root, "缺少根 SKILL.md"))
    for path in paths:
        try:
            errors, text = check_text(path, path.read_bytes(), custom)
            failures.extend((path, error) for error in errors)
            if text is not None and path.name == "SKILL.md":
                failures.extend((path, error) for error in check_frontmatter(text))
            if text is not None and path.suffix == ".md":
                failures.extend(
                    (path, error) for error in check_links(path, root, text)
                )
        except (OSError, ValueError) as error:
            failures.append((path, f"读取或解析失败：{error}"))
    failures.extend(check_source_counts(paths, custom))
    for path, error in failures:
        label = path.relative_to(root).as_posix() if path != root else "."
        print(f"{label}: {error}", file=sys.stderr)
    print(f"已检查 {len(paths)} 个文本文件，发现 {len(failures)} 项问题")
    return 1 if failures else 0


def main() -> int:
    """提供只读 CLI，参数错误与检查失败使用不同退出码"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="检查根目录")
    parser.add_argument(
        "--files", nargs="+", default=[], help="仅检查相对根目录的指定文件"
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="排除根目录相对 POSIX 路径模式，可重复",
    )
    parser.add_argument(
        "--require-skill", action="store_true", help="要求根目录具有 SKILL.md"
    )
    parser.add_argument(
        "--source-group",
        action="append",
        default=[],
        help="补充语言分组，例如 Nim=.nim,.nims，可重复，不得改写内置分组",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        parser.error("root 必须是已存在目录")
    try:
        custom = parse_source_groups(args.source_group)
        return run(root, args.files, args.exclude, args.require_skill, custom)
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
