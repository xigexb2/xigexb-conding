# Swift

[English](../../languages/swift.md) | **简体中文** | [规范索引](../translations.md)

所有包/目录直接同类源码最多 20 个，测试、声明与第一方生成文件合并计数；设计时按职责划分子包，遵守 [统一目录规范](../directory-structure.md)

- 确认 Swift 语言模式、SDK、部署目标与严格并发设置，单文件最多 380 行
- 使用 Swift API Design Guidelines，中文文档说明参数、失败、隔离和生命周期
- 优先值语义与明确的 optional 处理，不用强制解包掩盖运行时不确定性
- ARC 不回收强引用环，闭包、delegate、timer 与订阅检查捕获关系
- `weak` / `unowned` 依据对象实际生命周期选择，不能为消除循环任意改成 unowned
- `Sendable`、actor 和主 actor 隔离遵循实际语言模式；不要用 unchecked 注解压制未证明的竞争
- async/await 与 Task 有所有者和取消路径，取消通常需要协作检查
- actor 在 await 处可能重入，跨 await 的业务不变量必须重新校验
- SwiftUI 使用稳定 identity、正确状态拥有者和可观察模型；不在 body 中启动无管理副作用
- UI 更新遵循平台主线程/actor 契约，网络与重计算不阻塞界面
- UIKit/AppKit 的 delegate、通知和回调解除注册，布局处理安全区域及文字放大
- 错误通过 throws/Result 与适用 UI 状态表达，不把取消呈现为普通服务故障
- 验证真实部署目标、深色主题、Dynamic Type、VoiceOver、后台恢复和权限拒绝

结合 [移动端](../product/mobile.md)、Apple HIG 与 Swift 官方并发文档执行。
