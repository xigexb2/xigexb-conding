"""定义源码规模与同类文件分组，测试和生成的第一方源码一并计数"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import re


LIMIT_360 = {".java", ".kt", ".go", ".rs", ".c", ".h", ".cpp", ".hpp", ".js", ".vue"}
LIMIT_380 = {
    ".py",
    ".pyi",
    ".ts",
    ".tsx",
    ".jsx",
    ".swift",
    ".cc",
    ".cxx",
    ".hh",
    ".hxx",
    ".kts",
    ".mjs",
    ".cjs",
    ".mts",
    ".cts",
    ".sh",
    ".bash",
    ".zsh",
    ".fish",
    ".ps1",
    ".psm1",
    ".rb",
    ".rake",
    ".php",
    ".cs",
    ".fs",
    ".fsx",
    ".vb",
    ".sql",
    ".v",
    ".sv",
    ".vh",
    ".svh",
    ".vhd",
    ".vhdl",
    ".html",
    ".htm",
    ".css",
    ".scss",
    ".sass",
    ".less",
    ".dart",
    ".zig",
    ".lua",
    ".s",
    ".S",
    ".asm",
    ".scala",
    ".sc",
    ".ex",
    ".exs",
    ".erl",
    ".hrl",
    ".hs",
    ".lhs",
    ".clj",
    ".cljs",
    ".cljc",
    ".r",
    ".R",
    ".jl",
    ".m",
    ".mm",
    ".pl",
    ".pm",
    ".svelte",
    ".astro",
    ".razor",
    ".proto",
    ".graphql",
    ".gql",
    ".tf",
    ".tfvars",
    ".cmake",
}
GROUPS = {
    "Java": {".java"},
    "Go": {".go"},
    "Rust": {".rs"},
    "C/C++": {".c", ".h", ".cpp", ".cc", ".cxx", ".hpp", ".hh", ".hxx"},
    "Python": {".py", ".pyi"},
    "JavaScript/TypeScript": {
        ".js",
        ".jsx",
        ".mjs",
        ".cjs",
        ".ts",
        ".tsx",
        ".mts",
        ".cts",
    },
    "Vue": {".vue"},
    "Kotlin": {".kt", ".kts"},
    "Swift": {".swift"},
    "HTML": {".html", ".htm"},
    "样式": {".css", ".scss", ".sass", ".less"},
    "Verilog/SystemVerilog": {".v", ".sv", ".vh", ".svh"},
    "VHDL": {".vhd", ".vhdl"},
    "Unix Shell": {".sh", ".bash", ".zsh", ".fish"},
    "PowerShell": {".ps1", ".psm1"},
    "Ruby": {".rb", ".rake"},
    "F#": {".fs", ".fsx"},
    "Scala": {".scala", ".sc"},
    "Elixir": {".ex", ".exs"},
    "Erlang": {".erl", ".hrl"},
    "Haskell": {".hs", ".lhs"},
    "Clojure": {".clj", ".cljs", ".cljc"},
    "R": {".r", ".R"},
    "Objective-C": {".m", ".mm"},
    "Perl": {".pl", ".pm"},
    "汇编": {".s", ".S", ".asm"},
    "GraphQL": {".graphql", ".gql"},
    "Terraform": {".tf", ".tfvars"},
}
EXTENSION_GROUP = {
    suffix: group for group, suffixes in GROUPS.items() for suffix in suffixes
}


def parse_source_groups(values: list[str]) -> dict[str, str]:
    """声明未知语言后缀，不允许覆盖内置技术族来绕过合并计数"""
    result = {}
    for value in values:
        name, separator, suffixes = value.partition("=")
        name = name.strip()
        if (
            not separator
            or not name
            or len(name) > 64
            or any(ord(c) < 32 for c in name)
        ):
            raise ValueError("语言分组格式必须为 名称=.后缀,.后缀")
        for suffix in suffixes.split(","):
            suffix = suffix.strip()
            if not re.fullmatch(r"\.[A-Za-z0-9][A-Za-z0-9_+-]*", suffix):
                raise ValueError(f"不合法的源码后缀：{suffix}")
            original = source_group(Path("source" + suffix))
            previous = result.get(suffix, original)
            if previous is not None and previous != name:
                raise ValueError(f"不能覆盖既有同类分组：{suffix} 属于 {previous}")
            result[suffix] = name
    return result


def source_group(path: Path, custom: dict[str, str] | None = None) -> str | None:
    """多后缀技术族合并计数，其余已识别源码按后缀计数"""
    suffix = path.suffix
    if custom and suffix in custom:
        return custom[suffix]
    if suffix not in LIMIT_360 and suffix not in LIMIT_380:
        return None
    return EXTENSION_GROUP.get(suffix, suffix)


def check_source_counts(
    paths: list[Path], custom: dict[str, str] | None = None
) -> list[tuple[Path, str]]:
    """检查涉及的源码目录全部直接同类文件，子目录独立，不能靠限定文件绕过"""
    errors = []
    parents = {path.parent for path in paths if source_group(path, custom) is not None}
    for parent in sorted(parents):
        try:
            counts = Counter(
                group
                for path in parent.iterdir()
                if path.is_file() and (group := source_group(path, custom)) is not None
            )
        except OSError as error:
            errors.append((parent, f"不能读取源码目录：{error}"))
            continue
        for group, count in sorted(counts.items()):
            if count > 20:
                errors.append(
                    (parent, f"直接归属 {count} 个 {group} 同类源码文件，超过 20 个")
                )
    return errors
