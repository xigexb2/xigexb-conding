# UI 设计、评审与组件实现

[English](../../product/ui-design-workflow.md) | **简体中文** | [规范索引](../translations.md)

按当前任务选读对应章节，在项目已有的设计文档、主题令牌和组件中延续已确认的决策。设计探索见[视觉设计](visual-design.md)，交互与无障碍见 [UI/UX 规范](ui-ux.md)。

## UW01 明确设计简报

- 明确产品受众、主任务、平台、技术栈和成功条件。确定布局前，梳理主流程以及适用的加载、空态、错误和权限状态。
- 查设计资料库时，一次检索解决一个决策，并带上产品、平台或交互约束。核对建议是否符合实际技术栈和任务，记录采用的规则及适用范围。
- 在项目权威设计文档中记录共享令牌和组件规则。页面特有的例外就近说明原因。采用令牌变更前，预览代表性控件和主题组合。项目需要此交换格式时，遵循 [DESIGN.md 指南](design-md.md)。[UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/b73ee96f8d4ff7bbc279c52dadcd907ffe23629c/.claude/skills/ui-ux-pro-max/SKILL.md)

## UW02 围绕产品内容改版

- 明确需修改的界面区域与行为。视觉改版沿用已确认的导航、操作和数据语义，按简报中的改动要求调整。
- 围绕主任务和真实内容建立视觉层级，按界面用途选择布局、密度、字体、配色和强调方式。例如产品页可以用能说明实物的主图，工作台优先让用户看清当前状态和下一步操作。
- 比较改版前后的代表性界面。在目标浏览器或应用中复验长内容、窄屏和已有操作路径。动效用于解释反馈或状态变化。[Taste Skill](https://github.com/Leonxlnx/taste-skill/blob/d1a2bb41d927083ac7118f60cfc9cdf711810ea0/skills/taste-skill/SKILL.md)

## UW03 评审可用性与实现质量

- 用路由或界面、用户流程、代表性数据、主题和视口或设备界定评审范围。检查信息层级、操作可发现性和任务完成情况，再用实际交互、无障碍工具或源码检查提供独立证据。
- 按场景核对键盘焦点、可访问名称、对比度、主题、响应式布局、触控和性能。原生界面使用目标平台及其无障碍工具。记录实际验证的状态与设备。
- 每项问题写明触发条件、实测行为、影响和修复建议。优先处理任务受阻、数据丢失或严重无障碍问题，再处理外观问题。复现问题并在修复后重跑关联检查。[Impeccable 设计评审](https://github.com/pbakaus/impeccable/blob/2fc5e1459efbbf06d92c7306517c286bf12490cf/.agents/skills/impeccable/reference/critique.md) · [Impeccable 技术审查](https://github.com/pbakaus/impeccable/blob/2fc5e1459efbbf06d92c7306517c286bf12490cf/.agents/skills/impeccable/reference/audit.md)

## UW04 组合、接入与复验组件

- shadcn/ui 项目先核对 `components.json`、已采用的底层组件库、别名、主题和框架约定。用既有的表单、弹窗、表格和图表原语组合业务界面并应用项目令牌。组件变体由原有模块维护。
- 引入或更新 registry 项目前，检查源码、依赖、写入位置和差异，确认对本地定制的影响。接入后核对别名、客户端与服务端边界、样式和无障碍。
- 明确数据表格的排序、筛选、分页与选择由哪一层负责。服务端分页时，按稳定行 ID 管理选择并定义跨页行为。复验加载、空态、错误、权限相关操作、焦点恢复与键盘操作。[shadcn 技能](https://github.com/shadcn-ui/ui/blob/0e5b2e621a9ee4cf6a604bbe6c5c0d5b70561eb4/skills/shadcn/SKILL.md) · [shadcn 数据表格](https://github.com/shadcn-ui/ui/blob/0e5b2e621a9ee4cf6a604bbe6c5c0d5b70561eb4/apps/v4/content/docs/components/radix/data-table.mdx)

已审阅的来源版本与许可见[第三方归属](../../../THIRD_PARTY_NOTICES.zh-CN.md#ui-design-workflow-sources)。
