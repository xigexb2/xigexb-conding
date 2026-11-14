# 现代 Web 安全与隐私

[English](../../web/security.md) | **简体中文** | [规范索引](../translations.md)

## WS01 浏览器信任边界

- 不可信纯文本优先使用 `textContent`；确需接收标记时，使用维护良好的适用场景净化器，并校验 URL 协议与属性
- 实施适当的 CSP，在支持的客户端评估 Trusted Types 作为纵深防御；恒等或宽松策略不等于净化，其他浏览器仍需安全输出处理
- 将 origin 解析为协议、主机和有效端口后比较；校验 `postMessage` 的发送 origin、source、数据结构和预期接收方，敏感消息避免通配目标
- 按实际需要限制第三方脚本、网络目标、iframe 和 referrer；对适用的静态第三方资源评估 SRI，并处理 CORS 与版本更新
- 在实际需要时申请浏览器权限，说明用途和拒绝后的行为，收紧范围，避免无必要地记录或持久化敏感数据

## WS02 身份与隐私

- Passkey／WebAuthn 使用服务端生成的一次性挑战，按实际规范与部署校验 origin、RP ID、签名、凭证及重放／计数规则；定义注册、恢复与撤销
- Passkey 或联合身份选择不等于其他资源的授权；租户与对象权限仍由服务端执行
- 通过限时、一次性、用途绑定的渠道验证邮箱所有权，语法正确不能证明实际控制权
- 根据产品适用要求设置安全 Cookie、CSRF 防护、隐私友好遥测、保留期限及授权／同意流程
- 浏览器本地加密和 WebCrypto 必须有明确威胁模型；客户端交付的代码和密钥不能防御所有源站被攻破或恶意客户端场景

## WS03 兼容与验证

新的连接策略和本地网络访问等实验能力在浏览器与版本间存在差异；采用前核对安全上下文、权限、特性检测和回退。验证 XSS 载荷、CSP 报告／执行、跨源消息、认证拒绝、隐私设置与目标浏览器。详见[上游索引](catalog.md)。

改编自 [GoogleChrome Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/SKILL.md) 及索引中的相关专题，已结合项目约束并调整兼容性和安全边界。指南内容采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，扩展参考资料遵循上游 Apache-2.0。详见[许可说明](../../../THIRD_PARTY_NOTICES.zh-CN.md)。
