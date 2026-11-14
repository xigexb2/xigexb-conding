# 浏览器扩展与 Chrome Manifest V3

[English](../../web/extensions.md) | **简体中文** | [规范索引](../translations.md)

## WX01 Manifest、权限与分发

- 确认目标浏览器版本与当前 Manifest V3 契约，只声明必要 API 权限和最小主机范围；实际交互允许时使用可选权限或 `activeTab`
- 按具体 API、上下文、用户手势、浏览器版本和目标 URL 验证 `activeTab`、主机权限与 `tabs` 的实际访问能力，不能声称某一种权限覆盖所有路径
- Manifest 引用的 popup、图标、侧边栏、选项、DevTools 和 Service Worker 文件必须真实存在并符合打包结构；验证浏览器 API 特性与版本
- 商店介绍、隐私政策、数据使用披露、权限理由、截图和审核信息须与真实行为一致；发布和对外联系遵循当前任务授权

## WX02 Service Worker 与状态

- 在顶层注册事件监听，并按扩展 Service Worker 可能停止／重启设计；跨事件需要的状态应持久化，根据生命周期、配额和敏感性选择 local、session、sync 或 IndexedDB
- 并发读改写需要明确串行化或事务存储；写入 `chrome.storage` 本身不能保证复合更新原子性
- 需要跨 Worker 挂起存续的任务使用 alarms，并将触发时间视为非精确；处理器须幂等并支持重启恢复
- 区分后台、popup、选项页、侧边栏、内容脚本和页面上下文；校验消息发送方、来源、结构、权限以及错误／超时行为

## WX03 注入与安全

- 遵守实际扩展 CSP 和 Manifest V3 远程代码限制，不为执行代码削弱 CSP、使用 `eval` 或把 Blob／srcdoc 视为通用 CSP 绕过方式
- 确实需要执行不可信内容时，设计允许的最小能力沙箱，约束消息、校验来源并明确威胁模型；不直接复制不安全的通配消息示例
- 最小化注入代码、主机范围与可访问数据；遵守隔离世界／主世界差异，释放时清理监听和脚本
- 侧边栏打开与图标点击行为取决于 Manifest、popup、用户手势和 API 可用性；按目标浏览器验证具体组合
- 按实际身份提供商与 Chrome 文档处理登录重定向 URI、开发／商店扩展 ID 注册及凭据存储

## WX04 验证

在目标浏览器加载未打包扩展，测试 Service Worker 挂起／重启、权限授权／撤销、popup／侧边栏入口、消息校验、CSP、存储并发、升级和卸载。所有扩展专题见[上游索引](catalog.md)。

改编自 [GoogleChrome Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/chrome-extensions/SKILL.md) 及索引中的相关专题，已结合项目约束并调整兼容性和安全边界。指南内容采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，扩展参考资料遵循上游 Apache-2.0。详见[许可说明](../../../THIRD_PARTY_NOTICES.zh-CN.md)。
