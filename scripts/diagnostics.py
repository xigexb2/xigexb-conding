"""将检查器诊断按用户选择转换为英文或简体中文"""

from __future__ import annotations

import re


MESSAGES = {
    "检查范围没有可读取的目标文件": "No readable target files in the check scope",
    "缺少根 SKILL.md": "Missing root SKILL.md",
    "禁止 UTF-8 BOM": "UTF-8 BOM is not allowed",
    "不是有效 UTF-8": "Invalid UTF-8",
    "文本包含 NUL 字节": "Text contains NUL bytes",
    "必须使用 LF，不能包含 CR": "Use LF without CR characters",
    "非空文本必须以 LF 结束": "Nonempty text must end with LF",
    "文件末尾存在额外空白行": "Extra blank lines at end of file",
    "缺少完整的 YAML frontmatter 边界": "Missing complete YAML frontmatter boundaries",
    "Skill name 必须是至多 64 字符的小写连字符标识": "Skill name must be a lowercase hyphenated identifier of at most 64 characters",
    "本检查器要求 description 是非空且不超过 1024 字符的单行标量": "This checker requires a nonempty single-line description of at most 1024 characters",
    "语言分组格式必须为 名称=.后缀,.后缀": "Source groups must use Name=.ext,.ext2",
    "root 必须是已存在目录": "root must be an existing directory",
    "发布元数据超过 64 KiB": "Release metadata exceeds 64 KiB",
    "YAML 根节点必须为映射": "YAML root must be a mapping",
    "缺少完整 frontmatter": "Missing complete frontmatter",
    "frontmatter 存在不支持的顶层字段": "Unsupported top-level frontmatter fields",
    "Skill name 不合法": "Invalid Skill name",
    "description 必须为非空且不超过 1024 字符的字符串": "description must be a nonempty string of at most 1024 characters",
    "metadata 必须为字符串到字符串的映射": "metadata must map strings to strings",
    "Agent interface 必须为映射": "Agent interface must be a mapping",
    "short_description 长度必须为 25～64 字符": "short_description must contain 25 to 64 characters",
    "default_prompt 必须引用本 Skill": "default_prompt must reference this Skill",
    "映射键必须可哈希": "Mapping keys must be hashable",
    "Skill、Agent 与 CI YAML 验证通过": "Skill, Agent, and CI YAML validation passed",
}
PATTERNS = (
    (
        r"目标必须是根目录内已存在的文件：(.*)",
        r"Target must be an existing file within root: \1",
    ),
    (r"读取或解析失败：(.*)", r"Read or parse failed: \1"),
    (r"第 (\d+) 行存在尾部空白", r"Line \1 has trailing whitespace"),
    (
        r"第 (\d+) 行超过 Java 120 字符列限制",
        r"Line \1 exceeds Java's 120-character limit",
    ),
    (r"共 (\d+) 行，超过 (\d+) 行", r"\1 lines exceed the \2-line limit"),
    (r"重复 frontmatter 字段：(.*)", r"Duplicate frontmatter field: \1"),
    (r"不支持的 frontmatter 字段：(.*)", r"Unsupported frontmatter field: \1"),
    (r"第 (\d+) 行链接越出检查根目录：(.*)", r"Line \1 links outside root: \2"),
    (r"第 (\d+) 行本地链接不存在：(.*)", r"Line \1 has a missing local link: \2"),
    (r"不合法的源码后缀：(.*)", r"Invalid source suffix: \1"),
    (
        r"不能覆盖既有同类分组：(.*) 属于 (.*)",
        r"Cannot override an existing source group: \1 belongs to \2",
    ),
    (r"不能读取源码目录：(.*)", r"Cannot read source directory: \1"),
    (
        r"直接归属 (\d+) 个 (.*) 同类源码文件，超过 20 个",
        r"\1 directly owned \2 source files exceed the limit of 20",
    ),
    (
        r"已检查 (\d+) 个文本文件，发现 (\d+) 项问题",
        r"Checked \1 text files; found \2 issues",
    ),
    (r"重复 YAML 键：(.*)", r"Duplicate YAML key: \1"),
    (r"(.*) 必须为字符串", r"\1 must be a string"),
)


def localize(message: str, language: str = "en") -> str:
    """保留用户路径和底层异常，只转换检查器拥有的诊断文本"""
    if language == "zh-CN":
        return message
    if message in MESSAGES:
        return MESSAGES[message]
    for pattern, replacement in PATTERNS:
        match = re.fullmatch(pattern, message, re.S)
        if match:
            return match.expand(replacement)
    for chinese, english in sorted(MESSAGES.items(), key=lambda item: -len(item[0])):
        message = message.replace(chinese, english)
    return message
