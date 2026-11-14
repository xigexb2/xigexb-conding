# 渐进式 Web 应用与新兴浏览器能力

[English](../../web/advanced.md) | **简体中文** | [规范索引](../translations.md)

## WA01 渐进式 Web 应用

- 按目标浏览器设计 manifest 身份、作用域、启动 URL、图标和安装行为；安装必须保留用户控制的浏览器操作
- 明确 Service Worker 生命周期、缓存版本、更新生效、离线回退、认证和退出策略；敏感租户数据不得在缺乏正确隔离时缓存
- 浏览器专用安装 API、安装提示和源迁移机制依赖具体版本；验证特性检测、限制、用户同意与普通浏览器回退
- 迁移已安装应用前审查 origin、深链接、Service Worker 作用域、数据迁移、回滚与应用身份

## WA02 本地 AI 与浏览器 Agent 工具

- 浏览器内置模型、翻译、摘要、语言检测及 WebMCP 持续演进；逐目标核验安全上下文、可用性、配额、模型下载、权限和用户设置
- 未经项目明确授权不启用 Origin Trial、浏览器标志或预览依赖；能力不可用或失败时不得默认把私有数据发送给其他服务商
- 客户端浏览器工具应定义最小动作、类型化参数、注册／清理生命周期、校验与授权；重要副作用需明确确认，服务端 API 仍是权威边界
- 区分生成内容、工具实际执行与外部结果；处理界面状态过期、提示注入、资源限制与取消

## WA03 WebAssembly 与图形

- 仅对经过测量的负载选择 WebAssembly、Worker、WebGL 等图形能力；验证目标运行时、CSP、内存上限、资源分发、清理和回退
- 编译为 WebAssembly 的 C/C++ 仍须审查本机内存安全、边界、ABI、所有权和依赖；沙箱不能代替源代码正确性
- Canvas、自定义绘制及复杂 3D 效果需要可访问的语义替代、键盘交互和真机性能测试

## WA04 验证

检查离线与更新流程、作用域、隐私、浏览器／运行时版本、权限拒绝、不支持特性、资源限制、无障碍和回退。[上游索引](catalog.md)列出 PWA、AI、WebMCP、图形与 WASM 专题。

改编自 [GoogleChrome Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/SKILL.md) 及索引中的相关专题，已结合项目约束并调整兼容性和安全边界。指南内容采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，扩展参考资料遵循上游 Apache-2.0。详见[许可说明](../../../THIRD_PARTY_NOTICES.zh-CN.md)。
