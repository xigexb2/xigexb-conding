# 设计语言、组件库与企业参考

[English](../../product/design-systems.md) | **简体中文** | [规范索引](../translations.md)

这些体系是不同产品情境下的候选，不是必须同时安装的依赖。先选择主体系，再通过统一 tokens、组件和交互适配品牌。企业产品的公开外观不等于可复制的官方规范。

## DS01 来源与适用性

| 体系 | 官方入口 | 适用参考 | 使用边界 |
| --- | --- | --- | --- |
| Ant Design / Ant Design Vue | [Ant](https://ant.design/)、[Vue 生态实现](https://antdv.com/) | 企业中后台、表单、表格、数据与操作层级 | React 与 Vue 实现分开核对，不假定 API 完全一致 |
| 腾讯 TDesign | [TDesign](https://tdesign.tencent.com/) | 企业应用、Vue/React、移动与小程序一致性 | 选择对应平台实现和版本 |
| 字节 Arco Design | [Arco](https://arco.design/) | 中后台、高密度数据、主题与设计 tokens | 区分 React/Vue 实现与具体维护状态 |
| 字节 Semi Design | [Semi](https://semi.design/) | 企业工具、主题、表单与工作台 | 不是所有字节/抖音产品的统一强制规范 |
| JetBrains Int UI | [IntelliJ Platform UI](https://plugins.jetbrains.com/docs/intellij/ui-guidelines-welcome.html) | IDE、工具型桌面、高密度与键盘效率 | 插件和桌面工具规则不能直接等同手机规则 |
| Google Material Design | [Material 3](https://m3.material.io/) | Android、自适应布局、语义色和组件状态 | 按目标平台与 SDK 能力选择，不强制所有 Web 仿 Android |
| Apple Human Interface Guidelines | [HIG](https://developer.apple.com/design/human-interface-guidelines/) | iOS、iPadOS、macOS 的原生行为与可访问性 | 平台差异、系统版本和品牌资产授权需分别核对 |
| IBM Carbon | [Carbon](https://carbondesignsystem.com/) | 企业级产品、数据密度、无障碍和可组合系统 | 选择官方支持实现，不拼接多套视觉基线 |
| Oracle Redwood | [Redwood](https://redwood.oracle.com/) | 企业业务体验、内容与业务层级 | 公开入口不代表全部内部规范可获取 |
| 京东 JDesign | [JDesign](https://jdesign.jd.com/) | 电商与企业业务设计资源的检索入口 | 页面可访问性与具体组件授权需验证，无法取得正文时不虚构细则 |
| 抖音开放平台 | [开发者文档](https://developer.open-douyin.com/) | 小程序/开放平台的能力、交互和审核要求 | 不把抖音消费端私有设计规则当作已公开规范 |
| OpenAI Apps SDK | [设计指南](https://developers.openai.com/apps-sdk/concepts/design-guidelines/) | 对话内工具、结果呈现与确认行为 | 属于 Apps SDK 场景，不声称通用 OpenAI 设计系统 |
| Anthropic / Claude | [公开技能](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | 设计意图、内容与视觉一致性，以及 AI 产品交互研究 | 公开 Skill 与 Claude 产品观察不是完整 HIG |

上述名称归各自权利人所有。本项目不代表相关公司，不打包其字体、商标、截图和非授权素材。

## DS02 选择顺序

1. 已有成熟设计系统优先，局部功能不顺带迁移组件库
2. 原生移动端先满足 HIG/Material 与平台交互，品牌在语义 tokens 和内容上表达
3. ToB 中后台按团队技术栈、组件覆盖、可访问性、主题、维护和国际化选择 Ant/TDesign/Arco/Semi/Carbon 等
4. ToC、电商和内容产品从任务、信息架构与信任设计出发，不直接复制中后台表单密度
5. IDE、运维台、协议调试与工程工具可参考 JetBrains 的键盘、密度和上下文信息
6. 大型企业业务可比较 Carbon/Redwood 的流程与信息层级，具体组件仍由技术和许可决定

## DS03 统一设计契约

- 维护语义颜色、字体、间距、圆角、层级、动效与断点 tokens
- tokens 由基础值到语义到组件映射，主题通过统一入口切换
- 工具需要交换设计令牌时，可按现有工具链导出 DTCG JSON 或 CSS 自定义属性。先用预览核对不同主题的解析结果，避免手抄色值以及覆盖现有令牌。
- 同一动作在不同页面保持名称、位置、颜色和快捷键逻辑
- 复杂组件封装业务行为时保留库的可访问性和扩展契约，避免全量重新实现
- 数据密度、暗色、焦点、禁用、错误、加载与选中态形成矩阵验收
- 设计变更记录迁移范围与视觉回归，组件库升级核对 API、样式和读屏行为
- 不把某仓库“必须深色”“禁止汉堡菜单”“每段占一屏”等审美偏好提升为全平台硬规则

需要从代码提取令牌、编写 `DESIGN.md` 或将原型交付到前端时，参见 [Google Stitch 设计与实现流程](stitch-workflow.md)。

## DS04 AI 产品与对话式工具

- 用户能够区分生成内容、来源、工具执行状态和实际外部结果
- 流式输出、停止、重试、编辑和恢复有明确语义，取消生成不自动撤销已经执行的操作
- 外部副作用在明确授权下执行，确认信息说明对象、范围和后果
- 不以假进度、虚构引用和编造成功状态增强界面可信感
- 长回答、代码、表格、附件与小屏展示分别设计；保留键盘、复制及读屏体验
- 不推断或宣传 OpenAI、Claude 未公开的内部实现与设计标准

## DS05 审查输出

记录主设计体系、实际组件版本、tokens 入口、平台差异与视觉验收结果。给出能够定位到页面、状态和触发操作的问题，不能只写“缺乏高级感”。
