# xigexb-coding

面向真实研发任务的个人工程规范 Skill，采用 **精简入口 + 按需参考 + 可运行检查** 的结构。

它把 xigexb 的编码习惯、语言官方约定和经过筛选的工程经验分开组织，覆盖从架构、实现与体验到验证、协作和交付的链路。支持 ToB、ToC、互联网、物联网、原生、网页和混合开发，并提供系统、嵌入式与硬件工程检查框架。

## 能做什么

- 按 Java、Go、Rust、C、C++、Python、JavaScript、TypeScript、Vue、Kotlin、Swift、SQL、HTML/CSS 分别应用规则
- 设计职责、接口、状态机、算法、并发、资源边界和错误恢复
- 选择并应用统一的 UI 体系，覆盖页面、交互、色调、无障碍和平台体验
- 核对数据库、协议、设备控制、多实例、安全和供应链的关键不变量
- 约束 Git、CI、发布和验证证据，保护已有修改与操作授权边界
- 对 MCU/RTOS、通信、RTL/FPGA、原理图和 PCB 提供设计与复验清单

它不承诺“99% 覆盖”“绝对无 bug”或行业认证；具体覆盖及专业边界见 [覆盖清单](references/coverage.md)。

## 快速使用

将仓库根目录作为一个 Skill 目录安装，保留 `SKILL.md`、`references/`、`scripts/` 和 `agents/` 的相对位置。

项目内使用的目录形式：

```text
your-project/
└── .agents/
    └── skills/
        └── xigexb-coding/
            ├── SKILL.md
            ├── agents/
            ├── references/
            └── scripts/
```

Codex 及其他 Agent 的发现目录以各客户端当前文档为准；支持项目技能发现的客户端可使用上述结构。不要假定所有工具都采用同一个全局目录。

显式调用示例：

```text
使用 $xigexb-coding，为这个 Go 网关实现有界请求调度，并验证取消、超时和关闭行为
```

```text
使用 $xigexb-coding，按现有 TDesign Vue 体系设计设备管理页面，覆盖批量操作、弱网与权限状态
```

```text
使用 $xigexb-coding，审查 Java 25 + Netty 的异步缓冲区所有权，不新增仓库 Java 单元测试
```

```text
使用 $xigexb-coding，检查嵌入式通信方案，分别列出主机验证、板测与仪器实测证据
```

## 规则是怎样组织的

| 层次 | 作用 | 入口 |
| --- | --- | --- |
| 个人约定 | UTF-8/LF、中文注释、规模、测试与 Git 习惯 | [profile.md](references/profile.md) |
| 工程决策 | 架构、算法、性能、底层、协议、数据与安全 | [SKILL.md](SKILL.md) 路由 |
| 语言与平台 | 对应工具链、语言与生命周期契约 | [languages/](references/languages) |
| 视觉与体验 | UI、设计体系、Web 与移动端 | [UI](references/product/ui-ux.md)、[平台](references/product/mobile.md) |
| 证据与交付 | 调试、验证、Git、CI 与运行 | [验证](references/verification.md)、[Git](references/engineering/git.md) |
| 来源与维护 | 官方资料、开源调研、许可与覆盖边界 | [来源](references/sources.md)、[调研](references/github-research.md) |

使用时先读个人约定，再按实际任务读少量相关参考。不会要求每次把所有语言、框架和硬件规范全部加载。

## 默认个人约定

- UTF-8 无 BOM、LF、简体中文注释，语言原生格式化工具优先
- 主要语言源文件上限 360 行，其余手工源文件不超过 380 行；具体后缀以 profile.md 为准
- Java 目标行宽 100 列、硬上限 120 列；**所有语言的包/目录直接归属同类源码最多 20 个，包含测试和第一方生成代码，必须在设计时按职责拆分子包**
- Java 不新增仓库单元测试，仍完成必要验证；Go 行为修改新增或更新单测
- 不生成 SQL 留底文件；正式迁移文件需要符合任务明确授权
- 未经明确授权不 commit/push；只要求提交时不推送
- 不把下发、受理、传输确认与最终执行混为一谈

这些是作者偏好，不代表所有团队或行业必须采用。使用者可通过当前任务或项目指令选择自己的规则，并保留语言和平台真实契约。

## 设计体系与安全参考

设计章节区分 Ant Design、TDesign、Arco/Semi、JetBrains Int UI、Material Design、Apple HIG、IBM Carbon、Oracle Redwood，以及京东/抖音公开入口、OpenAI 与 Claude 相关公开资源。不同来源的公开程度与适用范围均有说明，不宣称掌握未公开的企业内部规范。

安全章节参考 OWASP ASVS、API Security、NIST SSDF 和 CWE，覆盖认证授权、租户、输入输出、密码、数据、设备、供应链与事件处理。

## 本地检查

需要 Python 3.11 或更高版本。基础文本检查只用标准库；完整 YAML 校验与开发测试需要固定的开发依赖。以下命令在 Skill 根目录执行：

```text
python scripts/check_repo.py . --require-skill
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py .
python -m unittest discover -s tests -v
```

对业务仓库限定本次目标，命令中的路径相对于检查根目录：

```text
python /path/to/xigexb-coding/scripts/check_repo.py /path/to/project --files src/main.go src/worker_test.go
```

检查项包括文本编码和行尾、源文件行数、Java 行长、所有已识别语言的目录同类文件数、Skill 单行标识及内联本地 Markdown 文件链接。

检查器只读，不运行项目、不访问网络、不自动修复，也不证明业务、安全、性能、UI 质量或规范全部符合。Java 行长按 Unicode 字符数计算，Tab 按四字符展开，不计算终端视觉宽度；Markdown 不检查锚点或复杂引用式链接。`validate_skill.py` 使用正规 YAML 解析器检查元数据、Agent 配置和 CI 语法，拒绝重复键与非法类型。

默认排除 `.git`、依赖、构建与工具缓存目录，不自动读取 `.gitignore`，不跟随遍历中的符号链接。`--exclude` 使用根目录相对路径的大小写敏感 POSIX glob，可重复传入；第一方交付源码不能通过排除取得豁免。`--files` 仅接收根目录内存在的文本文件，仍核对涉及源码目录内各类别的完整数量。混合后缀和拆包要求见 [目录规模规范](references/directory-structure.md)。

```text
python scripts/check_repo.py . --exclude 'external/*'
python scripts/check_repo.py --help
```

新增语言不必修改检查器源码，例如下面的声明将 `.nim` 与 `.nims` 合并，参与文件发现、380 行上限与每目录 20 文件检查：

```text
python scripts/check_repo.py /path/to/project --source-group 'Nim=.nim,.nims'
```

分组只对本次调用生效，不能覆盖内置分组拆散计数。安装 Skill 后，工具路径相对于 Skill 所在目录解析，目标根目录仍为实际业务仓库。

Windows PowerShell 与 Bash 的参数引号规则分别遵守其 shell。检查规则不会代替 `gofmt`、编译器、Sanitizer、浏览器或真实板测。

## GitHub 发布准备

- 仓库根就是 Skill 根，可作为独立 GitHub 仓库提交
- GitHub Actions 提供 Linux/Windows 的 Python 检查与测试，第三方 Action 固定到提交
- 发布前运行本地检查、审查文件和许可，确认不含内部环境、密钥或私有代码
- 创建远端、设置可见性、commit、push、tag、Release 分别按用户授权执行
- 安装器的单命令远程安装格式在真实仓库地址确定后再补充，不提供虚构仓库链接

## 维护与来源

本版来源研究基准日为 2026-11-12。GitHub 调研包含 21 个候选仓库及 32 份重点 Skill 正文/规则片段，Star 仅为当时关注度快照；入口型 Skill 不等于其所有子文档已经阅读。

- [GitHub 调研与取舍](references/github-research.md)
- [官方规范与权威资料](references/sources.md)
- [贡献与维护](CONTRIBUTING.md)
- [版本记录](CHANGELOG.md)
- [逐项需求映射](references/requirements-matrix.md)
- [安全报告](SECURITY.md)
- [第三方来源与许可](THIRD_PARTY_NOTICES.md)

## 许可

原创内容采用 [MIT](LICENSE)。保留的第三方许可文件适用各自原始条款；企业名称、字体、商标和设计资源不随本项目自动授权。不存在相关公司的背书或认证关系。
