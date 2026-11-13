# 覆盖清单与边界

## 支持的研发链路

| 领域 | 覆盖内容 | 主要参考 |
| --- | --- | --- |
| 需求与架构 | 不变量、契约、领域、模式、模块、演进 | engineering/architecture.md、engineering/backend.md |
| 后端 | ToB/ToC、API、事务、任务、多实例、框架 | engineering/backend.md、engineering/frameworks.md |
| 语言 | Java、Go、Rust、C、C++、Python、JS、TS、Vue、Kotlin、Swift、SQL、HTML/CSS | languages/ |
| 产品与 UI | 信息架构、配色、排版、表单、表格、状态、无障碍 | product/ui-ux.md、design-engineering/systems.md |
| 平台 | Web、原生、混合、跨端、小程序、弱网、升级 | product/mobile.md、engineering/frameworks.md |
| 算法与性能 | 复杂度、数据结构、数值、并发、背压、测量 | engineering/algorithms.md、engineering/concurrency-performance.md |
| 系统 | 内存、SMP、中断、文件、网络 I/O、诊断 | engineering/systems.md |
| IoT 与通信 | 协议、消息、设备状态、物理接口、DSP、无线 | engineering/protocols-distributed.md、hardware/communications.md |
| 嵌入式 | BSP、RTOS、驱动、DMA、启动、升级和板测 | hardware/embedded.md |
| 硬件 | 器件、电路、电源、PCB、制造和测试 | hardware/electronics-pcb.md |
| 芯片 | RTL、CDC/RDC、时序、模拟/混合信号、PVT、后仿与签核边界 | hardware/chip-design.md、hardware/analog-ic.md |
| 数据 | 模型、约束、SQL、索引、事务、迁移与恢复 | engineering/database.md、languages/sql.md |
| 安全 | 威胁、身份、授权、输入、密码、供应链与事件 | engineering/security.md |
| 协作与运行 | Git、PR、构建、CI、发布、运维与证据 | engineering/git.md、engineering/delivery.md、verification.md |

## 如何理解“超级 Skill”

逐项需求与证据要求见 [需求映射](requirements-matrix.md)，模式选型见 [设计模式](engineering/design-patterns.md)，开源引入与许可见 [开源工程](open-source.md)。
它是共享规则与按需参考组成的研发入口，不是将所有参考全文同时注入。广度通过覆盖矩阵表达，深度通过具体任务的官方资料、实现和验证补齐。

不对“覆盖 99%”给出无统计依据的承诺。没有需求全集、版本范围和验收数据时，不能计算此类比例。

## 需要任务专属材料的领域

- 具体芯片、BSP、PDK、板卡、私有协议和特定硬件实验
- 医疗、汽车、航空、功能安全、支付合规及其他监管认证
- 模拟/RF IC 深入设计、先进封装、工艺签核和受限 IP
- 训练大模型、专业密码算法证明和未列出的语言/行业框架
- 特定公司未公开的内部规范与设计系统

涉及这些领域时沿用通用安全和工程原则，读取适用官方/行业资料并明确尚缺的资源，不能编造条文或声称认证通过。

## 规则维护

- 个人偏好修改 profile.md；语言规则修改对应语言；具体框架与平台规则放对应章节
- 每次修正规则明确来源、适用版本及旧规则为何失效
- 新增强制规则先检查与已有规则冲突，避免从单个历史故障制造无限例外
- 工具检查范围与文档一致；不能宣称脚本检查了业务、安全或设计美感
- 新领域须在 SKILL.md 路由和本表可发现，不依赖隐藏文件或用户本地环境
