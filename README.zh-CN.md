# xigexb Coding

[English](README.md) | **简体中文**

面向编码 Agent 的工程规范 Skill，覆盖软件与硬件项目中的架构、实现、UI/UX、性能、安全与交付。

以职责清晰、契约明确、资源有界、结果可验证为基础，用于企业应用、消费产品、Web 与移动应用、物联网平台、嵌入式系统和底层基础设施的设计、开发、重构与审查。

## 安装

将仓库克隆到编码 Agent 支持的技能目录。对于从 `.agents/skills` 发现项目技能的 Agent，在项目根目录执行：

```bash
git clone https://github.com/xigexb2/xigexb-conding.git .agents/skills/xigexb-coding
```

保持 `SKILL.md`、`references/`、`scripts/` 和 `agents/` 的相对位置。全局安装使用对应 Agent 支持的技能发现目录。

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

- [UI/UX 规范](references/zh-CN/product/ui-ux.md)：信息架构、页面层级、配色语义、字体、间距、导航、表单、表格、反馈、无障碍与响应式行为
- [设计体系](references/zh-CN/product/design-systems.md)：Ant Design、TDesign、Arco/Semi、JetBrains Int UI、Google Material Design、Apple HIG、IBM Carbon、Oracle Redwood 及其他公开设计资源
- [移动与跨平台规范](references/zh-CN/product/mobile.md)：iOS、Android、原生、混合、小程序、平台交互、权限、离线行为与生命周期管理

为产品选择一致的设计体系，并根据 ToB/ToC 任务与目标平台调整信息密度、交互和恢复流程。

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

使用 Python 3.11 或更高版本，检查格式、源文件规模、目录上限和本地文档链接：

```bash
python scripts/check_repo.py . --require-skill
```

元数据验证与检查器测试见[贡献指南](CONTRIBUTING.zh-CN.md)。

## 文档

- [双语规范索引](references/zh-CN/translations.md)
- [检查器用法与 Agent 元数据](references/zh-CN/tooling.md)
- [Skill 入口](SKILL.zh-CN.md)
- [默认编码约定](references/zh-CN/profile.md)
- [规范覆盖索引](references/zh-CN/coverage.md)
- [官方规范与权威来源](references/zh-CN/sources.md)
- [开源技术引入](references/zh-CN/open-source.md)
- [第三方许可说明](THIRD_PARTY_NOTICES.zh-CN.md)

完整规范提供英文与简体中文版本，每篇文档均可切换到对应译文。

## 许可

[MIT](LICENSE)。保留的第三方资料遵循各自许可。
