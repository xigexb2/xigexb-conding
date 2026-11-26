# JavaScript

[English](../../languages/javascript.md) | **简体中文** | [规范索引](../translations.md)

所有包/目录直接同类源码最多 20 个，测试、声明与第一方生成文件合并计数；设计时按职责划分子包，遵守 [统一目录规范](../directory-structure.md)

- 先确认浏览器、Node.js、模块类型、打包器与最低运行环境；`.js` 文件最多 360 行
- 使用 `const` 表达不重新绑定的引用，需要重绑定时用 `let`，不以 `var` 引入隐式作用域问题
- 避免隐式类型转换和真假值混淆，区分 `0`、空串、`null` 与 `undefined`
- 对象和数组传播运算是浅拷贝，不能据此宣称嵌套对象不可变
- 按目标运行时评估 structuredClone、非变异数组方法与 AbortSignal 的超时和组合能力。深复制前核对受支持类型和数据语义，取消信号须传递给实际 I/O。
- 大整数身份和金额不能超出 Number 的精确范围；BigInt 的 JSON 与协议转换必须明确
- Promise 必须被等待、返回或显式监督，禁止无处理的 fire-and-forget
- `Promise.all` 不自动取消其他请求；失败、取消和部分成功语义需要显式实现
- 使用 AbortSignal 等实际 I/O 取消机制；丢弃结果不等于中止请求
- 防止搜索、分页和路由请求旧结果覆盖新状态，使用取消或请求世代标识
- 测量主线程交互延迟，拆分长任务；按负载评估 Worker、调度 API 或兼容回退，见 [Web 性能](../web/performance.md)
- 事件监听、定时器、观察器、连接和订阅在生命周期结束时清理
- 不把用户输入传入 eval、动态 Function、危险 HTML 或 shell；按场景净化并在支持时实施 CSP／Trusted Types，见 [Web 安全](../web/security.md)
- Node 服务设置请求体、并发、超时和输出上限，流式处理遵循 backpressure
- 依赖管理沿用锁文件和包管理器，不混用 npm/pnpm/yarn 重写锁文件
- 模块导入不能隐式启动服务或修改全局配置，配置装配与业务逻辑分离
- 使用已有 ESLint、格式工具和行为测试；运行正式构建与真实页面验证，不能只做语法检查

权威依据见 [来源索引](../sources.md)：ECMAScript、MDN、Node.js 官方文档。
