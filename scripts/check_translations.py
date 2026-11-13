"""检查双语文档完整性、反向导航与规则结构，不能代替语义审校"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from repo_rules import LINK, prose_lines


def translated_path(path: Path, root: Path) -> Path:
    """参考文档使用中文镜像树，根文档使用语言后缀"""
    relative = path.relative_to(root)
    if relative.parts[0] == "references":
        return root / "references/zh-CN" / relative.relative_to("references")
    return path.with_name(path.stem + ".zh-CN.md")


def discover_pairs(root: Path) -> dict[Path, Path]:
    """从实际文件发现文档，新增英文文档不能遗漏译文要求"""
    paths = [p for p in root.glob("*.md") if not p.name.endswith(".zh-CN.md")]
    paths.extend(
        p
        for p in (root / "references").rglob("*.md")
        if "zh-CN" not in p.relative_to(root / "references").parts
    )
    return {p: translated_path(p, root) for p in sorted(paths)}


def targets(path: Path, text: str) -> list[Path]:
    """解析正文内的本地链接，不将代码示例当作导航"""
    found = []
    for _, line in prose_lines(text):
        for match in LINK.finditer(line):
            parts = urlsplit(match.group(1).strip("<>"))
            if parts.path and not parts.scheme and not parts.netloc:
                found.append((path.parent / unquote(parts.path)).resolve())
    return found


def external_links(text: str) -> Counter:
    """来源地址与出现次数应一致，避免翻译时丢失证据"""
    return Counter(
        match.group(1)
        for _, line in prose_lines(text)
        for match in LINK.finditer(line)
        if urlsplit(match.group(1)).scheme in {"http", "https"}
    )


def balanced_fences(text: str) -> bool:
    """识别围栏字符与长度，防止正文被未闭合代码块吞掉"""
    active = ""
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if not match:
            continue
        token, suffix = match.groups()
        if not active:
            active = token
        elif token[0] == active[0] and len(token) >= len(active) and not suffix.strip():
            active = ""
    return not active


def check(root: Path) -> tuple[int, list[str]]:
    """检查双语覆盖与可执行结构，不宣称证明翻译含义等价"""
    root = root.resolve()
    pairs = discover_pairs(root)
    errors = []
    if not pairs:
        errors.append("No document pairs / 没有发现双语文档")
    expected = set(pairs.values())
    localized = set(root.glob("*.zh-CN.md")) | set(
        (root / "references/zh-CN").rglob("*.md")
    )
    localized.discard(root / "LICENSE.zh-CN.md")
    for path in sorted(localized - expected):
        errors.append(f"Orphan translation / 无对应原文：{path.relative_to(root)}")
    for english, chinese in pairs.items():
        label = english.relative_to(root).as_posix()
        if not chinese.is_file():
            errors.append(f"Missing translation / 缺少译文：{label}")
            continue
        try:
            en = english.read_text(encoding="utf-8")
            zh = chinese.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"{label}: {error}")
            continue
        if chinese not in targets(english, en) or english not in targets(chinese, zh):
            errors.append(f"Missing reciprocal navigation / 缺少双向跳转：{label}")
        for path, text in ((english, en), (chinese, zh)):
            if not balanced_fences(text):
                errors.append(
                    f"Unclosed code fence / 未闭合代码围栏：{path.relative_to(root)}"
                )
        rule_ids = lambda value: re.findall(r"^## ([A-Z]+\d+)\b", value, re.M)
        if rule_ids(en) != rule_ids(zh):
            errors.append(f"Rule identifiers differ / 规则编号不一致：{label}")
        if external_links(en) != external_links(zh):
            errors.append(f"Source links differ / 来源链接不一致：{label}")
        if english.name == "translations.md":
            continue
        for target in targets(chinese, zh):
            if target != english and target in pairs:
                errors.append(
                    f"Chinese link enters English tree / 中文链接进入英文树：{label}"
                )
        for target in targets(english, en):
            if target != chinese and target in expected:
                errors.append(
                    f"English link enters Chinese tree / 英文链接进入中文树：{label}"
                )
    return len(pairs), errors


def main() -> int:
    """提供可在本地和 CI 运行的只读双语检查入口"""
    parser = argparse.ArgumentParser(description="Check bilingual docs / 检查双语文档")
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    try:
        count, errors = check(Path(args.root))
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1
    for error in errors:
        print(error, file=sys.stderr)
    print(
        f"Checked {count} document pairs; {len(errors)} issues / 已检查 {count} 组双语文档，{len(errors)} 项问题"
    )
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
