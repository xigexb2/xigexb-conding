# 视觉方向探索与原型设计

[English](../../product/visual-design.md) | **简体中文** | [规范索引](../translations.md)

## VD01 确立视觉方向

从真实内容、现有产品与设计体系、受众和交付媒介出发。核验影响设计的事实，使用官方或经授权的素材。主视觉应展示产品如何使用、数据说明什么，或题材有什么特点。

方向尚未确定时，从适合题材的设计方法、同媒介的出色参考和意外的视觉处理三个角度构思。对于较大的探索任务，最多列出六个候选，选出最多三个差异明显的方向，用代表页面、幻灯片或关键帧展开。比较信息结构、密度、层级和交互。用户委托选择时，采用最贴合任务的方案并说明依据。局部迭代沿用已确定的方向。

借鉴参考如何组织信息，配色、字体、构图和图像围绕当前题材设计。内容需要图片时使用真实或有许可的图像，并明确标记缺失素材。展示真实产品描述、数据和评价前先核对。

## VD02 按交付媒介设计

| 媒介 | 设计与交付检查 |
| --- | --- |
| 网页与仪表盘 | 展示产品使用过程。检查响应式布局和关键交互。正式实现时遵循项目的生产 Web 规范。 |
| App 与小程序原型 | 展示主流程及加载、空白、错误和权限状态。遵循平台导航、安全区域和控件惯例。 |
| 商店截图与社交图文 | 安排跨画面的阅读顺序。检查裁切、可读性和平台尺寸。使用准确的产品截图与文案。 |
| 演示与可编辑 PPTX | 用代表页确立方向。按观看距离检查可读性，并核验导出文件中可编辑的文字和对象。 |
| 信息图 | 核实数据、单位、刻度和标签。选择符合比较任务的视觉编码，并按需提供无障碍说明。 |
| 动效与视频 | 用分镜规划内容与节奏。检查渲染后的关键帧，核验交付格式与适用的音频。 |

## VD03 复验实际渲染结果

按目标尺寸逐屏、逐页或逐帧检查成品。先修影响最大的几处问题，再检查新一轮渲染。核对层级、排印、溢出、素材、无障碍和主任务。按需实测键盘、触控及失败路径。用目标查看器打开导出文件，检查还原效果和可编辑性。

本流程改编自花叔设计 3.5.0。候选数量和复验轮数按任务规模调整。交付物遵循项目文件上限和素材授权要求。

## VD04 按任务选择 UI 设计参考

从当前最需要解决的页面问题出发。任务跨越多个阶段时，沿用已确认的用户流程、视觉方向和设计令牌。

| 现状 | 做法与交付物 |
| --- | --- |
| 需求或用户流程还不清楚 | 参考 [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/b73ee96f8d4ff7bbc279c52dadcd907ffe23629c) 梳理用户、任务、关键状态和失败恢复。先交付页面结构与低保真流程，走通主任务后再确定视觉方向。 |
| 已有原型或旧页面，需要视觉改版 | 参考 [Taste Skill](https://github.com/Leonxlnx/taste-skill/tree/d1a2bb41d927083ac7118f60cfc9cdf711810ea0)，用真实内容重做信息层级、版式、字体与配色。交付改版前后的代表界面，复验现有操作路径、长内容和窄屏。 |
| 需要分析成熟页面或判断现有设计哪里难用 | 参考 [Impeccable](https://github.com/pbakaus/impeccable/blob/2fc5e1459efbbf06d92c7306517c286bf12490cf/README.md) 拆解内容顺序、行动优先级、组件组合和响应式布局。按任务影响排序问题，优先复验导航、焦点、主题和性能。 |
| 需要实现管理后台、仪表盘或 SaaS 工作台 | 在项目技术栈支持且需要选型时评估 [shadcn/ui](https://github.com/shadcn-ui/ui) 的表格、表单、弹窗和图表组合。项目已有组件体系时沿用其组件和令牌。复验键盘、空态、错误恢复和权限状态。 |
| 设计完成，需要汇报或交接 | 采用文章提到的 Design MD Collection 交付思路，用项目的 [DESIGN.md 规范](design-md.md) 记录可复用令牌与组件规则。另用案例文档串联目标、设计决策、代表界面和复验结果。 |

场景选择取自 Jason 分享时间的文章。文中以名称介绍 Design MD Collection，这里通过项目已有的 `DESIGN.md` 规范落实交接。[文章原文](https://mp.weixin.qq.com/s/IgzOThFw1Bqx8zu4FKEzBQ)

设计简报、改版、评审和组件接入的步骤见 [UI 设计、评审与组件实现](ui-design-workflow.md)。

## 上游参考

- [SKILL.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/SKILL.md)
- [references/directions.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/directions.md)
- [references/polish-loop.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/polish-loop.md)
- [references/brand-asset-protocol.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/brand-asset-protocol.md)
- [references/modules/web.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/modules/web.md)
- [references/app-prototype.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/app-prototype.md)
- [references/modules/miniprogram.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/modules/miniprogram.md)
- [references/modules/appstore.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/modules/appstore.md)
- [references/modules/deck.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/modules/deck.md)
- [references/editable-pptx.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/editable-pptx.md)
- [references/modules/infographic.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/modules/infographic.md)
- [references/modules/xiaohongshu.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/modules/xiaohongshu.md)
- [references/modules/motion.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/modules/motion.md)
- [references/design-styles.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/references/design-styles.md)
