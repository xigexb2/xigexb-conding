# xigexb Coding

[English](README.md) | **简体中文** | [Skill 入口](SKILL.zh-CN.md) | [规范索引](references/zh-CN/translations.md) | [更新日志](CHANGELOG.zh-CN.md)

面向编码 Agent 的工程规范 Skill，覆盖软件与硬件项目中的架构、实现、UI/UX、性能、安全与交付。

以职责清晰、契约明确、资源有界、结果可验证为基础，用于企业应用、消费产品、Web 与移动应用、物联网平台、嵌入式系统和底层基础设施的设计、开发、重构与审查。

## 安装

将仓库克隆到编码 Agent 支持的技能目录。对于从 `.agents/skills` 发现项目技能的 Agent，在项目根目录执行：

```bash
git clone https://github.com/xigexb2/xigexb-conding.git .agents/skills/xigexb-coding
```

此命令获取默认分支。需要固定版本时，在同一命令里为 `git clone` 添加 `--branch <tag>`，标签见 [GitHub Releases](https://github.com/xigexb2/xigexb-conding/releases)。

安装时保留完整目录。Agent 从 `SKILL.md` 加载英文入口和按任务索引，用 `SKILL.zh-CN.md` 及 `references/zh-CN/` 提供简体中文内容。可在调用时指定回复语言。默认和备选 Agent 界面元数据的用法见[工具说明](references/zh-CN/tooling.md)。

## 使用

调用时说明任务及相关语言、框架或平台：

```text
使用 $xigexb-coding，设计具有有界并发、取消、背压和优雅关闭能力的 Go 网关
```

```text
使用 $xigexb-coding，基于 Vue 和 TDesign 开发设备管理页面，
覆盖批量操作、权限状态和弱网恢复
```

```text
使用 $xigexb-coding，审查 Java + Netty 服务的缓冲区所有权、
线程安全、接口契约和失败恢复
```

```text
使用 $xigexb-coding，从现有 Vue 页面提取设计令牌，整理 DESIGN.md，
并复验按钮状态、主题对比度和 Tailwind 导出结果。
```

Skill 先加载核心约定，再按任务涉及的语言和工程领域选择参考规范。

## 核心规范

以下为 Skill 的默认约定，具体应用遵循当前任务与仓库指令；语言、协议和平台的真实契约仍以其权威规范为准。

| 领域 | 规范 |
| --- | --- |
| 文本格式 | UTF-8 无 BOM、LF 换行、一个末尾换行，无行尾空白 |
| 代码注释 | 专业简体中文，遵循语言原生文档语法并保留必要的工具标记 |
| 源文件规模 | 主要语言后缀上限 360 行，其他手工维护源文件上限 380 行，含注释和空行；见[具体上限](references/zh-CN/profile.md) |
| 包与目录规模 | **所有语言的每个包或目录，直接归属的同类源文件最多 20 个** |
| 文件计数 | 生产、测试、声明、头文件、平台变体和第一方生成源码合并计数，子目录独立计数 |
| 模块边界 | 达到上限前按领域、能力、协议或生命周期拆分，保持职责内聚与依赖方向明确 |
| 设计原则 | 单一职责、高内聚、低耦合、稳定契约，模型符合业务与物理流程 |
| 设计模式 | 根据实际变化点和生命周期选择模式，评估复杂度与维护代价 |
| 并发控制 | 明确所有权，限制队列与执行规模，处理取消、超时、背压和有序关闭 |
| 性能优化 | 定义预算，测量真实负载，定位瓶颈并验证优化效果 |
| Java | 目标行宽 100 列、上限 120 列；不新增仓库单元测试，仍须编译与适当验证 |
| Go | 使用 `gofmt`；行为与并发逻辑变更新增或更新单元测试 |
| SQL | 参数化查询、明确事务边界、审查执行计划，不保留 SQL 留底文件；正式迁移需要任务授权 |
| Git | 修改聚焦、提交清晰、保护已有工作，提交和推送需要明确授权 |

同类文件的不同后缀合并计数，包括 JavaScript/TypeScript、C/C++ 源码与头文件。详见[目录与包规模规范](references/zh-CN/directory-structure.md)。

## 工程规范范围

| 领域 | 规范内容 |
| --- | --- |
| [架构设计](references/zh-CN/engineering/architecture.md) | 领域边界、接口与实现、模块化、依赖方向、状态机与架构决策 |
| [设计模式](references/zh-CN/engineering/design-patterns.md) | 创建型、结构型、行为型与架构模式，选型条件和各语言落实方式 |
| [后端开发](references/zh-CN/engineering/backend.md) | 接口契约、校验、认证、授权、租户、幂等、事务与恢复 |
| [算法](references/zh-CN/engineering/algorithms.md) | 复杂度、数据结构、数值边界、正确性与负载选型 |
| [并发与性能](references/zh-CN/engineering/concurrency-performance.md) | 内存模型、同步、有界资源、剖析、基准、延迟、吞吐与容量 |
| [数据库](references/zh-CN/engineering/database.md) | 数据建模、约束、索引、隔离、锁、迁移与缓存一致性 |
| [协议与分布式](references/zh-CN/engineering/protocols-distributed.md) | 消息语义、重试、顺序、一致性、所有权、故障转移与执行状态 |
| [安全体系](references/zh-CN/engineering/security.md) | 威胁建模、访问控制、租户隔离、凭据、密码学、供应链、设备安全与 AI/Agent 工具边界 |
| [系统底层](references/zh-CN/engineering/systems.md) | 内存安全、ABI/FFI、IPC、虚拟内存、SMP、网络 I/O 与资源生命周期 |
| [技术框架](references/zh-CN/engineering/frameworks.md) | 按版本契约使用前端、后端、持久化、消息和网络框架 |
| [Git](references/zh-CN/engineering/git.md) 与[交付](references/zh-CN/engineering/delivery.md) | 分支、提交、审查、CI/CD、版本、发布证据、回滚与运维 |

## 语言规范

各语言在共性规范基础上，遵循自身工具链、运行时、内存模型和生态约定。

| 分类 | 参考规范 |
| --- | --- |
| 后端与通用开发 | [Java](references/zh-CN/languages/java.md)、[Go](references/zh-CN/languages/go.md)、[Python](references/zh-CN/languages/python.md) |
| 系统与原生开发 | [Rust](references/zh-CN/languages/rust.md)、[C](references/zh-CN/languages/c.md)、[C++](references/zh-CN/languages/cpp.md) |
| Web 开发 | [JavaScript](references/zh-CN/languages/javascript.md)、[TypeScript](references/zh-CN/languages/typescript.md)、[Vue](references/zh-CN/languages/vue.md)、[HTML/CSS](references/zh-CN/languages/html-css.md) |
| 移动开发 | [Kotlin](references/zh-CN/languages/kotlin.md)、[Swift](references/zh-CN/languages/swift.md) |
| 数据开发 | [SQL](references/zh-CN/languages/sql.md) |

## UI、交互与应用设计

| 任务 | 项目指南 |
| --- | --- |
| 设计 ToB 或 ToC 界面，完善色彩、层级、导航、表单、表格、状态与无障碍 | [UI/UX 规范](references/zh-CN/product/ui-ux.md) |
| 选择视觉方向、制作原型并按交付媒介复验，参考花叔设计 | [视觉方向探索与原型设计](references/zh-CN/product/visual-design.md) |
| 在现有产品中选择并应用设计体系，参考 Ant Design、TDesign、Arco/Semi、JetBrains Int UI、Material 3、Apple HIG、IBM Carbon 和 Oracle Redwood | [设计体系](references/zh-CN/product/design-systems.md) |
| 编写 `DESIGN.md`、记录 YAML 设计令牌，用 CLI 校验、比较并导出 DTCG JSON 或 Tailwind | [Google DESIGN.md 格式与双语示例](references/zh-CN/product/design-md.md) |
| 从界面简报、设计体系提取和多页原型走到 Vue、React 或 React Native 实现与复验 | [Google Stitch 工作流与 16 项上游技能索引](references/zh-CN/product/stitch-workflow.md) |
| 处理 iOS、Android、混合应用与小程序的导航、权限、离线和生命周期 | [移动与跨平台规范](references/zh-CN/product/mobile.md) |

Stitch 工作流可用于本地原型。连接 Google Stitch 服务时，按其工具配置和项目权限执行。

## 现代 Web 规范

项目从 GoogleChrome Modern Web Guidance 提炼了六组双语规范，按任务可查 [Web 基础](references/zh-CN/web/foundations.md)、[表单与无障碍交互](references/zh-CN/web/interaction.md)、[性能](references/zh-CN/web/performance.md)、[安全与隐私](references/zh-CN/web/security.md)、[PWA 与新兴 API](references/zh-CN/web/advanced.md)及[浏览器扩展](references/zh-CN/web/extensions.md)。[固定版本专题索引](references/zh-CN/web/catalog.md)链接到上游原文。

## 嵌入式与硬件

- [嵌入式开发](references/zh-CN/hardware/embedded.md)：MCU/RTOS 架构、中断、DMA、内存预算、时序、看门狗、启动、OTA 与板测
- [通信](references/zh-CN/hardware/communications.md)：分帧、字节序、CRC、重传、总线时序、工业协议与互操作
- [电路与 PCB](references/zh-CN/hardware/electronics-pcb.md)：器件选型、电源、保护、接地、信号完整性、EMC、DFM/DFT 与调试上电
- [数字芯片设计](references/zh-CN/hardware/chip-design.md)：RTL/FPGA、复位、CDC/RDC、约束、时序分析、验证与签核
- [模拟与混合信号芯片](references/zh-CN/hardware/analog-ic.md)：偏置、稳定性、转换器、射频考虑、PVT、失配、寄生、可靠性与测量

## 研发流程

1. 明确需求、不变量、接口、失败语义与验收条件。
2. 检查仓库、工具链、依赖和已有修改。
3. 设计职责、包边界、状态转换、安全控制与资源预算。
4. 实现错误处理、边界检查、所有权和资源回收。
5. 根据变更范围，以适当证据验证正确性、兼容性、性能和平台行为。

软件、界面、分布式系统和硬件的验证方式见[复验规范](references/zh-CN/verification.md)。

## 仓库检查

在 Skill 根目录用 Python 3.11 或更高版本运行与 CI 对应的检查。首条命令只依赖 Python 标准库，完整 YAML 校验和测试使用开发依赖。

```bash
python -X utf8 scripts/check_repo.py . --require-skill
python -m pip install -r requirements-dev.txt
python -X utf8 scripts/validate_skill.py .
python -X utf8 scripts/check_translations.py .
python -X utf8 -m unittest discover -s tests -v
```

项目检查覆盖文本格式、文件与目录上限、本地链接、Skill 和 Agent 元数据、双语导航与检查器回归。检查业务仓库时，将业务仓库根目录传给已安装 Skill 的脚本。参数和用法见[工具说明](references/zh-CN/tooling.md)。

## 文档

- [规范覆盖与需求映射](references/zh-CN/coverage.md) · [需求验收矩阵](references/zh-CN/requirements-matrix.md)
- [官方规范与来源](references/zh-CN/sources.md) · [开源技术引入](references/zh-CN/open-source.md) · [上游对齐记录](references/zh-CN/upstream-alignment.md)
- [贡献指南](CONTRIBUTING.zh-CN.md) · [安全问题报告](SECURITY.zh-CN.md) · [第三方许可说明](THIRD_PARTY_NOTICES.zh-CN.md)

## 许可

原创内容采用 [MIT](LICENSE)；改编 Web 规范按 CC BY 4.0 署名，其他第三方资料遵循各自许可。详见[许可说明](THIRD_PARTY_NOTICES.zh-CN.md)。
