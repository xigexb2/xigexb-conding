"""使用正规 YAML 解析器验证本 Skill 的发布元数据与配置"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from diagnostics import localize

try:
    import yaml
except ImportError:
    raise SystemExit(
        "Install development dependencies / 请安装开发依赖：python -m pip install -r requirements-dev.txt"
    ) from None


class UniqueKeyLoader(yaml.SafeLoader):
    """拒绝重复键，避免后一个字段悄悄覆盖安全配置"""

    def construct_mapping(self, node, deep=False):
        """安全构造映射，同时检查键是否可哈希与重复"""
        self.flatten_mapping(node)
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                duplicate = key in result
            except TypeError as error:
                raise yaml.constructor.ConstructorError(
                    None, None, "映射键必须可哈希", key_node.start_mark
                ) from error
            if duplicate:
                raise yaml.constructor.ConstructorError(
                    None, None, f"重复 YAML 键：{key}", key_node.start_mark
                )
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def parse_yaml(text: str) -> dict:
    """限制元数据体积并禁止执行任意 YAML 对象构造"""
    if len(text.encode("utf-8")) > 65_536:
        raise ValueError("发布元数据超过 64 KiB")
    value = yaml.load(text, Loader=UniqueKeyLoader)
    if not isinstance(value, dict):
        raise ValueError("YAML 根节点必须为映射")
    return value


def validate_metadata(text: str) -> dict:
    """按 Agent Skills 约束检查名称、说明和可选字段类型"""
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.S)
    if not match:
        raise ValueError("缺少完整 frontmatter")
    data = parse_yaml(match.group(1))
    allowed = {
        "name",
        "description",
        "license",
        "compatibility",
        "metadata",
        "allowed-tools",
    }
    if set(data) - allowed:
        raise ValueError("frontmatter 存在不支持的顶层字段")
    name = data.get("name")
    if (
        not isinstance(name, str)
        or len(name) > 64
        or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
    ):
        raise ValueError("Skill name 不合法")
    description = data.get("description")
    if (
        not isinstance(description, str)
        or not description.strip()
        or len(description) > 1024
    ):
        raise ValueError("description 必须为非空且不超过 1024 字符的字符串")
    if "metadata" in data and (
        not isinstance(data["metadata"], dict)
        or any(
            not isinstance(k, str) or not isinstance(v, str)
            for k, v in data["metadata"].items()
        )
    ):
        raise ValueError("metadata 必须为字符串到字符串的映射")
    for key in ("license", "compatibility", "allowed-tools"):
        if key in data and not isinstance(data[key], str):
            raise ValueError(f"{key} 必须为字符串")
    return data


def validate_root(root: Path) -> None:
    """解析技能、Agent 元数据及实际存在的 CI YAML"""
    data = validate_metadata((root / "SKILL.md").read_text(encoding="utf-8"))
    localized = root / "SKILL.zh-CN.md"
    if localized.exists():
        translated = validate_metadata(localized.read_text(encoding="utf-8"))
        for field in ("name", "license", "metadata"):
            if data.get(field) != translated.get(field):
                raise ValueError(
                    f"Localized metadata differs / 双语元数据不一致：{field}"
                )
    for ui_path in (root / "agents").glob("openai*.yaml"):
        interface = parse_yaml(ui_path.read_text(encoding="utf-8")).get("interface")
        if not isinstance(interface, dict):
            raise ValueError("Agent interface 必须为映射")
        short = interface.get("short_description")
        prompt = interface.get("default_prompt")
        if not isinstance(short, str) or not 25 <= len(short) <= 64:
            raise ValueError("short_description 长度必须为 25～64 字符")
        if not isinstance(prompt, str) or "$" + data["name"] not in prompt:
            raise ValueError("default_prompt 必须引用本 Skill")
    for pattern in ("*.yml", "*.yaml"):
        for path in (root / ".github/workflows").glob(pattern):
            parse_yaml(path.read_text(encoding="utf-8"))


def main() -> int:
    """解析错误返回失败，供发布检查及 CI 使用"""
    parser = argparse.ArgumentParser(
        description="Validate Skill metadata / 验证技能元数据"
    )
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--lang", choices=("en", "zh-CN"), default="en")
    args = parser.parse_args()
    try:
        validate_root(Path(args.root).resolve())
    except (OSError, ValueError, yaml.YAMLError) as error:
        print(localize(str(error), args.lang), file=sys.stderr)
        return 1
    print(localize("Skill、Agent 与 CI YAML 验证通过", args.lang))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
