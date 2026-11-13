# Kotlin

[English](../../languages/kotlin.md) | **简体中文** | [规范索引](../translations.md)

所有包/目录直接同类源码最多 20 个，测试、声明与第一方生成文件合并计数；设计时按职责划分子包，遵守 [统一目录规范](../directory-structure.md)

- 版本以 Gradle、Kotlin 插件、JDK 与 Android 工具链兼容矩阵为准，单文件最多 360 行
- 使用官方命名和项目格式，中文 KDoc 说明职责、可空性和挂起行为
- 优先不可变值、data class、sealed 类型与明确的状态，避免以多个 nullable 字段组合状态机
- 不以 `!!` 掩盖外部输入和生命周期问题，Java 平台类型在边界校验
- scope function 适度使用，不用多层 `let/run/apply` 隐藏接收者和控制流
- 协程依附明确作用域与 Job，业务代码不随意使用 `GlobalScope`
- 挂起不等于后台线程，阻塞 I/O 和 CPU 工作使用正确 dispatcher 与容量边界
- 取消具有协作性，不吞 `CancellationException`；资源清理按可取消与不可取消范围判断
- Flow 区分冷流、StateFlow 与 SharedFlow 的订阅及重放语义，缓存和缓冲有界
- Android 按 lifecycle-aware 方式收集状态；进程死亡恢复不能只依赖 ViewModel 内存
- Compose 状态提升到合适拥有者，副作用使用正确 API；remember 不能替代持久化
- 服务端 Ktor/Spring 等沿用框架边界，不把 Android 生命周期假设套到后端
- 验证类型、协程取消、状态恢复与实际平台构建，复用 ktlint/detekt 等已有配置

结合 [移动端](../product/mobile.md)、[并发](../engineering/concurrency-performance.md) 与 Kotlin 官方文档执行。
