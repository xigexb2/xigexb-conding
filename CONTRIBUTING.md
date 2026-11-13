# 贡献与规则维护

## 修改前

- 明确修改属于个人偏好、语言官方契约、框架版本行为还是工程建议
- 先读相关参考和来源，说明适用范围与旧规则的问题
- 不为单个历史故障新增全局禁令，不复制上游整份 Skill 或无法确认许可的内容
- 不加入内网环境、真实客户数据、凭据、私有协议和受限资料

## 文档与代码

- UTF-8 无 BOM、LF、一个末尾换行，无尾部空白，中文注释
- 主入口保持精简，新规则放所属参考并更新路由和覆盖清单
- 所有本地链接可解析，版本相关结论有权威出处，不宣称无证据的性能或认证
- Python 工具采用标准库、类型标注、必要错误处理和职责分离，单文件不超过 380 行
- 新脚本或行为变更添加有意义的测试；不要只匹配文案或复制实现表达式
- 文件规模与格式要求不适用于原样保留的第三方许可，仍保持文本可读

## 复验

```text
python scripts/check_repo.py . --require-skill
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py .
python -m unittest discover -s tests -v
```

完整 YAML 校验由 validate_skill.py 执行并纳入 CI。适用时另用客户端技能校验工具，不能把基础正则字段检查称为完整 YAML 验证。

对规则变更走查 verification.md 的典型任务，确认没有改变授权、语言格式、内存所有权和平台语义。复杂变更可以开展独立行为评测，但不得把文档走查写成已经执行了模型评测。

## 提交与审查

- 一个 PR 说明具体规则缺陷、适用范围、最终变化和验证结果
- Conventional Commits：`type(scope): 简体中文摘要`，具体要求见 [Git 规范](references/engineering/git.md)
- 上游借鉴注明固定提交、文件、许可与取舍；新增代码或文字需处理其版权与 NOTICE 义务
- 不因增加了来源链接就宣称全文审查，也不因为 Star 高就采纳未经验证的建议
