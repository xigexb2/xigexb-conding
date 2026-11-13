"""提供只读仓库规则，不执行项目构建或访问网络"""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from source_catalog import LIMIT_360, LIMIT_380

TEXT_SUFFIXES = (
    LIMIT_360
    | LIMIT_380
    | {
        ".md",
        ".txt",
        ".yaml",
        ".yml",
        ".json",
        ".toml",
        ".xml",
        ".properties",
        ".ini",
        ".cfg",
        ".conf",
        ".csv",
        ".gradle",
        ".kts",
        ".cmake",
        ".proto",
    }
)
TEXT_NAMES = {
    "LICENSE",
    "NOTICE",
    "Dockerfile",
    "Makefile",
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
}
LINK = re.compile(r"!?\[[^\]\n]*\]\((<[^>\n]+>|[^)\s]+)(?:\s+\"[^\"]*\")?\)")


def check_text(
    path: Path, data: bytes, custom: dict[str, str] | None = None
) -> tuple[list[str], str | None]:
    """检查编码、行尾与规模，保留解码后的正文用于后续结构检查"""
    errors: list[str] = []
    if data.startswith(b"\xef\xbb\xbf"):
        errors.append("禁止 UTF-8 BOM")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return [*errors, "不是有效 UTF-8"], None
    if "\x00" in text:
        errors.append("文本包含 NUL 字节")
    if "\r" in text:
        errors.append("必须使用 LF，不能包含 CR")
    if text and not text.endswith("\n"):
        errors.append("非空文本必须以 LF 结束")
    if text.endswith("\n\n"):
        errors.append("文件末尾存在额外空白行")
    lines = text.splitlines()
    for number, line in enumerate(lines, 1):
        if line.rstrip(" \t") != line:
            errors.append(f"第 {number} 行存在尾部空白")
        if path.suffix == ".java" and len(line.expandtabs(4)) > 120:
            errors.append(f"第 {number} 行超过 Java 120 字符列限制")
    limit = (
        360
        if path.suffix in LIMIT_360
        else (
            380
            if path.suffix in LIMIT_380 or (custom and path.suffix in custom)
            else None
        )
    )
    if limit is not None and len(lines) > limit:
        errors.append(f"共 {len(lines)} 行，超过 {limit} 行")
    return errors, text


def check_frontmatter(text: str) -> list[str]:
    """校验本项目约定的单行 Skill 标识，不冒充完整 YAML 解析器"""
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.S)
    if not match:
        return ["缺少完整的 YAML frontmatter 边界"]
    values = {}
    errors = []
    allowed = {
        "name",
        "description",
        "license",
        "compatibility",
        "metadata",
        "allowed-tools",
    }
    for line in match.group(1).splitlines():
        entry = re.match(r"^([a-z][a-z-]*):\s*(.*?)\s*$", line)
        if not entry:
            continue
        key, value = entry.groups()
        if key in values:
            errors.append(f"重复 frontmatter 字段：{key}")
        if key not in allowed:
            errors.append(f"不支持的 frontmatter 字段：{key}")
        values[key] = value.strip("\"'")
    name = values.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append("Skill name 必须是至多 64 字符的小写连字符标识")
    description = values.get("description", "")
    if (
        not description
        or description in {"|", ">", "|-", ">-"}
        or len(description) > 1024
    ):
        errors.append("本检查器要求 description 是非空且不超过 1024 字符的单行标量")
    return errors


def prose_lines(text: str):
    """跳过代码围栏，避免把示例里的路径当作真实文件链接"""
    marker = ""
    length = 0
    for number, line in enumerate(text.splitlines(), 1):
        fence = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if fence:
            token, suffix = fence.groups()
            if not marker:
                marker, length = token[0], len(token)
            elif token[0] == marker and len(token) >= length and not suffix.strip():
                marker = ""
            continue
        if not marker:
            yield number, line


def check_links(path: Path, root: Path, text: str) -> list[str]:
    """验证内联本地文件链接存在且不越出根目录，不访问外部网址"""
    errors = []
    for number, line in prose_lines(text):
        for match in LINK.finditer(line):
            value = match.group(1).strip("<>")
            parts = urlsplit(value)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            decoded = unquote(parts.path)
            relative = decoded.lstrip("/") if decoded.startswith("/") else decoded
            base = root if decoded.startswith("/") else path.parent
            target = (base / relative).resolve()
            if not target.is_relative_to(root):
                errors.append(f"第 {number} 行链接越出检查根目录：{value}")
            elif not target.exists():
                errors.append(f"第 {number} 行本地链接不存在：{value}")
    return errors
