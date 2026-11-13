# 框架与基础设施集成

[English](../../engineering/frameworks.md) | **简体中文** | [规范索引](../translations.md)

只加载实际使用的框架规则。版本、生命周期、线程模型和升级要求以对应官方文档及仓库锁定版本为准。

## F01 Java 服务框架

- Spring Boot/Spring Security、Quarkus、Jakarta 等识别后分别应用，避免跨框架混用
- 构造器注入、配置校验、可控启动与优雅关闭，禁止初始化阶段隐式启动无监督后台线程
- Spring 事务检查代理、自调用、传播、隔离、回滚和线程边界；响应式事务以实际上下文传播模型为准
- 阻塞库与 WebFlux/EventLoop 隔离，不能因为方法返回 Mono/Future 就认为内部非阻塞
- Hibernate/JPA 检查查询规模、懒加载、N+1 和实体状态；MyBatis 检查参数化和租户条件

## F02 Netty 与高性能网络库

- EventLoop 中不做阻塞操作或长计算；offload 有界并保持每连接业务顺序要求
- 引用计数资源明确所有者和转移点，读取、消费、转发、异步保留与出站写分别处理
- `SimpleChannelInboundHandler`、解码器和编码器可能自动释放；按具体类契约避免重复释放
- `retain`、retained slice 和复制选择取决于共享底层内存与生命周期，不以“零拷贝”代替推理
- 消费且不转发的引用在所有退出路径释放，转发后不无条件释放；提交失败明确所有权是否转移
- `safeRelease` 不应掩盖常态引用计数错误，泄漏检测与异常证据必须可观察
- gnalloy、gnet、netpoll 等分别核对回调线程、缓冲有效期、写入所有权和关闭语义

## F03 Go / Rust / Python 框架

- Gin、Echo、Fiber、标准 net/http 不共享完全相同请求上下文与对象生命周期，异步前复制必要数据
- Tokio、Axum、Actix 按运行时线程、阻塞池、提取器限制和连接关闭契约设置预算
- FastAPI、Django、Flask 区分同步/异步处理器、ORM 会话和后台任务生命周期
- 后台任务不能依赖已经释放的请求对象或连接，可靠任务使用可持久化的队列与监督机制
- 框架默认超时、Body 限制、连接数和认证配置必须检查，不能假定默认即可生产使用

## F04 前端与组件生态

- Vue、React、Angular、Svelte 按现有技术栈实现，不能为采用某 Skill 强行替换框架
- React 检查纯渲染、effect 清理、稳定身份与并发请求；不将所有派生数据写进 effect
- Angular 检查变更检测、订阅清理、DI 生命周期与模板类型；Svelte 按实际版本响应式模型设计
- SSR/SSG/CSR 按首屏、SEO、权限、缓存和部署能力取舍
- UI 组件库版本、设计 tokens、图标、表单和可访问性集中管理，见 [设计体系](../product/design-systems.md)

## F05 Redis、缓存与锁

- 所有缓存明确 key 命名、租户/权限维度、容量、TTL、空值与失效策略
- 避免大 key、热 key、无界集合及在线全量 KEYS；扫描仍需限量和预算
- Lua/事务或原子指令只保证其指定范围，不能据此宣称跨系统原子性
- 分布式锁释放校验所有者，续约和进程暂停可能影响租约；关键副作用考虑 fencing 或幂等
- Redis 缓存和分布式锁不替代持久化唯一约束

## F06 Kafka、RabbitMQ、MQTT

- 区分生产者确认、代理持久化、消费者确认和业务事务提交
- 消费重试与死信有上限、原因、保留及重放策略，检查重复副作用
- Kafka 分区顺序只在相应范围成立，消费者重平衡与提交位置需验证
- RabbitMQ ack/nack/requeue 与预取数防止毒消息循环和消费端内存膨胀
- MQTT QoS 与 retained/session 语义不等于业务完成，Topic ACL 与身份绑定

## F07 存储与私有基础设施

- MinIO/S3 的权限、预签名有效期、分片上传、校验、生命周期和大文件流式处理明确
- GitLab/Artifactory 等服务限制暴露面、最小权限、备份、升级及依赖镜像可信来源
- 搜索索引、对象存储和数据库之间定义一致性、失败补偿与删除传播
- 配置只装配选中的集成，避免未启用依赖意外建立连接或启动监听端口
