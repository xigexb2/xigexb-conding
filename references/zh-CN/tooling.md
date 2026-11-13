# 检查器用法与 Agent 元数据

[English](../tooling.md) | **简体中文** | [规范索引](translations.md)

## TOOL01 从 Skill 根目录运行

需要 Python 3.11 或更高版本。基础文本和目录检查只使用标准库；严格 YAML 校验与开发测试需要固定的开发依赖。

```text
python scripts/check_repo.py . --require-skill
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py .
python scripts/check_translations.py .
python -m unittest discover -s tests -v
```

仓库和元数据检查器默认使用英文诊断，通过 --lang zh-CN 选择中文；帮助同时包含两种语言。双语检查器输出中英文诊断。

```text
python scripts/check_repo.py . --require-skill --lang zh-CN
python scripts/validate_skill.py . --lang zh-CN
```

代码注释与文档字符串继续遵循简体中文约定；标识符、命令选项和机器 schema 保持其原生形式。

## TOOL02 检查业务仓库

从已安装 Skill 解析脚本路径，再传入实际业务根目录。文件参数相对于业务根目录：

```text
python /path/to/xigexb-coding/scripts/check_repo.py /path/to/project --files src/main.go src/worker_test.go
python /path/to/xigexb-coding/scripts/check_repo.py /path/to/project --source-group 'Nim=.nim,.nims'
python scripts/check_repo.py --help
```

- --files 要求文件存在且位于根目录内，仍核对涉及源码目录的全部直接同类文件
- --source-group 只为本次调用补充后缀，执行 380 行与 20 文件上限，不能覆盖内置分组
- --exclude 接受可重复、大小写敏感、根目录相对的 POSIX glob，不能豁免第一方交付源码
- 默认排除 .git、依赖、构建产物与工具缓存；不自动加载 .gitignore，不跟随目录符号链接
- Bash/PowerShell 参数引号遵守实际 shell

## TOOL03 范围与诊断含义

| 诊断类别 | 含义与处理 |
| --- | --- |
| 编码与换行 | 保存为 UTF-8 无 BOM、LF，去掉 NUL 和尾部空白，保留一个末尾换行 |
| 源码行数与 Java 行宽 | 按职责拆分并遵守上限；Java 按 Unicode 字符计算，Tab 展开为四字符 |
| 目录同类计数 | 超过 20 前合理拆包，混合后缀、测试与第一方生成源码合并计算 |
| 语言分组错误 | 使用 名称=.后缀,.后缀，禁止覆盖既有技术族 |
| 本地链接错误 | 修复不存在或越出根目录的路径；锚点与复杂引用式链接不在检查范围 |
| YAML 与元数据错误 | 修复语法、重复键、允许字段和类型、名称说明上限、Agent 提示与双语元数据一致性 |
| 双语错误 | 补齐译文、双向跳转、规则编号、来源 URL、代码围栏与语言导航 |

检查器只读。仓库检查成功返回 0，发现问题返回 1，参数或范围错误返回 2；其他校验器失败时返回非零状态。安装依赖是单独明确执行的命令。

机械双语检查只证明覆盖与结构，不能证明语义等价；仍要审查要求、限定条件、示例和版本相关结论。

## TOOL04 中英文 Agent 元数据

- [openai.yaml](../../agents/openai.yaml) 是实际生效的默认英文界面配置
- [openai.zh-CN.yaml](../../agents/openai.zh-CN.yaml) 提供等价中文配置供手动选择，客户端不会自动发现这个备选文件名
- 需要中文界面时，在自己的安装目录中把备选内容复制到 agents/openai.yaml，并按客户端方式刷新或重新加载技能
- 可直接通过 [SKILL.zh-CN.md](../../SKILL.zh-CN.md) 进入中文参考树，或使用 $xigexb-coding 时明确要求中文
- 两种配置保持相同技能名称、调用行为、规则编号与技术要求

原始 [LICENSE](../../LICENSE) 和第三方许可文件保持原文。[中文许可说明](../../LICENSE.zh-CN.md) 仅辅助阅读，法律许可以原文为准。
