# 用户需求与验收映射

本表按已明确提出的范围核对，不能用目录存在替代内容质量与实际行为验证。具体项目必须继续提供其版本、需求和验证资源。

| 需求 | 实现位置 | 验收口径 |
| --- | --- | --- |
| 个人编码习惯 | [个人约定](profile.md) | 编码、注释、规模、测试、SQL 和 Git 规则明确 |
| 所有语言每包/目录同类文件最多 20 个 | [目录规范](directory-structure.md) | 混合后缀、测试与第一方生成文件合并；设计时拆分；CLI 支持补充未知语言 |
| Java、Go、Rust、C、C++、Python | [语言目录](languages/) | 各有独立专题，包含契约、资源、并发和验证 |
| Vue、JavaScript、TypeScript | [语言目录](languages/) | 独立专题，不强制迁移既有框架或风格 |
| SQL、网页、原生开发 | [SQL](languages/sql.md)、[HTML/CSS](languages/html-css.md)、[Kotlin](languages/kotlin.md)、[Swift](languages/swift.md) | 方言、浏览器、生命周期与平台行为分别约束 |
| 架构与设计模式 | [架构](engineering/architecture.md)、[模式](engineering/design-patterns.md) | 真实变化点、职责、模式代价及语言映射 |
| 高并发、高性能与算法 | [并发性能](engineering/concurrency-performance.md)、[算法](engineering/algorithms.md) | 有界资源、正确性、不变量、复杂度和测量证据 |
| 后端与公开企业实践 | [后端](engineering/backend.md)、[框架](engineering/frameworks.md) | ToB/ToC、接口、事务、任务恢复、具体版本与取舍 |
| UI、交互、页面、色调 | [UI](product/ui-ux.md) | 任务、状态、tokens、对比度、键盘、响应式与恢复 |
| 各厂商设计语言 | [设计体系](product/design-systems.md) | 已列明公开入口、适用领域、组件差异和不可获取边界 |
| iOS、Android、网页、混合、小程序 | [平台](product/mobile.md) | HIG/Material、权限、生命周期、弱网与升级 |
| ToB、ToC、IoT、互联网 | [后端](engineering/backend.md)、[协议](engineering/protocols-distributed.md) | 场景差异明确，受理与执行结果不混淆 |
| 系统底层 | [系统](engineering/systems.md) | ABI、内存、SMP、中断、I/O 和证据分层 |
| 嵌入式与通信 | [嵌入式](hardware/embedded.md)、[通信](hardware/communications.md) | RTOS、驱动、信号、接口、无线和真实板测边界 |
| 电路与 PCB | [硬件](hardware/electronics-pcb.md) | 器件、电源、原理图、布局、制造与测量 |
| 芯片设计 | [RTL 与芯片](hardware/chip-design.md)、[模拟 IC](hardware/analog-ic.md) | 数字时序、CDC/RDC、模拟指标、PVT/失配、后仿及签核边界 |
| 安全体系 | [安全](engineering/security.md) | 身份、授权、数据、输入、供应链、设备和 AI 工具边界 |
| Git 与发布 | [Git](engineering/git.md)、[交付](engineering/delivery.md) | 授权、原子改动、PR、版本和产物可追溯 |
| GitHub 研究与借鉴 | [调研](github-research.md)、[开源](open-source.md) | 检索快照、固定提交、许可、取舍与维护 |
| 可发现、可安装的专业 Skill | [主入口](../SKILL.md)、[README](../README.md) | 元数据、按需路由、相对资源和客户端元数据正确 |
| 可执行检查 | [验证](verification.md) | 文本/目录检查、严格 YAML、行为测试及 CI 互相补充 |

## 尚不能从通用规范直接证明的事项

- 对所有语言、所有框架逐条覆盖，或“99%”的可量化比例：没有可验证的全集和分母
- 未公开的大厂规范：只能采用可合法取得的公开资料与明确标注的产品观察
- 真实业务吞吐、安全合规、板级功能和芯片签核：必须有相应项目、数据、工具和实验
- 第三方 Agent 是否始终按规则实现：格式和脚本检查不能代替独立模型行为评测

这些边界不豁免本 Skill 已明确的强制规则。新增语言需要补充后缀和专题，新增业务需要明确不变量与验收，不能因为不在示例列表中放弃工程要求。
