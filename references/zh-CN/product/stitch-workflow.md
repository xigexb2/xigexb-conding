# Google Stitch 设计与实现流程

[English](../../product/stitch-workflow.md) | **简体中文** | [规范索引](../translations.md)

用于 AI 辅助界面设计、设计体系提取、多页面迭代与实现。也可配合本地原型和项目已有设计工具使用。使用 Stitch 服务时，按当前 [MCP 安装文档](https://stitch.withgoogle.com/docs/mcp/setup/) 配置，并在调用前检查可用工具。

## ST01 定义设计任务

- 明确目标用户、主要任务、设备、预期内容、视口范围与验收标准。列出适用的加载、空态、错误、禁用和权限状态。
- 按意图选择新界面、参考图生成、局部编辑或多个变体。局部编辑时明确目标界面、区域和改动，沿用范围之外的导航、文案与令牌。
- 需要探索方向时，按任务完成度、无障碍与品牌契合度比较方案。把选定方向写成界面简报，明确组件与布局约束。见[视觉方向探索](visual-design.md)。

## ST02 记录设计决策

- 先读项目主题、组件和令牌定义。设计交接需要 `DESIGN.md` 时，将色彩角色、字体、间距、圆角、层级、断点和动效映射到项目令牌来源，记录关键组件状态、主题差异和例外。
- 从代码提取时，检查现有路由、共享布局、CSS 变量、框架主题配置和计算后样式。从预览提取时，记录采样路由、视口、主题与界面状态，注明哪些是实测值、哪些是提案，并在所支持的主题下复验代表性组件。
- 发现设计与实现偏差时，以项目令牌来源核对。已确认的改动同时影响令牌与交接文档时，同步更新两处。见[设计体系约定](design-systems.md)。

## ST03 迭代与交接

- 多页任务在 `SITE.md` 或项目现有计划文档中记录站点地图、共享导航和待办。每轮围绕一个页面或流程，明确目标和验收项。
- 记录路由或界面标识、设计版本、素材、待定事项、复验结果和下一步。维护各路由状态，让重试时更新正确的设计或实现。
- 从代码交付到设计时，选取有代表性的页面状态，将静态 HTML 或截图与 `DESIGN.md` 配套。按目标视口预览导出结果并核对素材。远程上传依赖用户对目标项目和传输材料的授权，导出使用代表性数据并移除私密值。

## ST04 实现与复验

- 将结构与行为映射到目标技术栈。Vue 或 React 优先复用现有组件、语义化 HTML 和令牌。React Native 使用原生布局、文本和触控原语，并检查安全区和系统字体缩放。
- 复用项目现有组件库，检查引入的 registry 组件依赖。仪表板的数据请求和缓存由数据层承载，复验表格语义、数据格式、空态和失败恢复。
- 在代表性设备、主题下对照已确认的设计检查实际渲染。按场景复验键盘或触控导航、焦点、表单校验、对比度、减少动效设置、加载、失败与权限状态。产品演示另验时间线、文字可读性和导出播放。见 [UI 与交互](ui-ux.md)。

## 上游技能索引

每项链接至本次审阅的上游实现。Stitch 工具参数与插件安装由上游项目维护。见[来源与许可](../../../THIRD_PARTY_NOTICES.zh-CN.md#google-stitch-skills)。

| 插件 | 上游技能 | 在本 Skill 中的应用 |
| --- | --- | --- |
| stitch-build | [react-components](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-build/skills/react-components/SKILL.md) | 将页面区域映射成可复用 React 组件、类型化属性和项目令牌，复验渲染与交互。 |
| stitch-build | [react-native](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-build/skills/react-native/SKILL.md) | 把 HTML 的布局和交互意图映射到原生视图、文本、滚动与触控，在目标设备上检查安全区、动态字体和读屏。 |
| stitch-build | [react-vite-dashboard](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-build/skills/react-vite-dashboard/SKILL.md) | 将远程数据和缓存放在数据层，覆盖加载、空态、失败和过期数据，保留表格语义。 |
| stitch-build | [remotion](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-build/skills/remotion/SKILL.md) | 按已确认的界面顺序和帧时间线制作演示，检查字幕、音画同步和渲染结果。 |
| stitch-build | [shadcn-ui](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-build/skills/shadcn-ui/SKILL.md) | 复用项目组件原语与变体，引入组件前检查 registry 源码、依赖和键盘交互。 |
| stitch-design | [code-to-design](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-design/skills/code-to-design/SKILL.md) | 将页面渲染快照与设计体系文档配套，用于产品设计迭代。 |
| stitch-design | [extract-design-md](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-design/skills/extract-design-md/SKILL.md) | 从前端源码或获准查看的预览提取令牌角色与状态，记录采样路由和待确认项。 |
| stitch-design | [extract-static-html](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-design/skills/extract-static-html/SKILL.md) | 按指定路由、视口和界面状态导出静态 HTML，携带样式和允许使用的资源，打开导出文件复验一致性。 |
| stitch-design | [generate-design](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-design/skills/generate-design/SKILL.md) | 按意图选择文字生成、参考图生成、局部编辑或方案变体，明确布局与状态约束。 |
| stitch-design | [manage-design-system](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-design/skills/manage-design-system/SKILL.md) | 读取或整理设计体系，映射语义角色，应用后检查受影响的页面。 |
| stitch-design | [upload-to-stitch](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-design/skills/upload-to-stitch/SKILL.md) | 确认目标项目、素材范围和传输授权，记录 Stitch 返回的素材或界面标识。 |
| stitch-utilities | [design-md](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-utilities/skills/design-md/SKILL.md) | 在 DESIGN.md 中记录可观察的设计规则及其与项目令牌的映射。 |
| stitch-utilities | [enhance-prompt](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-utilities/skills/enhance-prompt/SKILL.md) | 将模糊需求细化为包含用户、任务、界面结构、状态和验收标准的简报。 |
| stitch-utilities | [site-md](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-utilities/skills/site-md/SKILL.md) | 多页交接需要时，在 SITE.md 中记录范围、页面关系、共享导航及剩余工作。 |
| stitch-utilities | [stitch-loop](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-utilities/skills/stitch-loop/SKILL.md) | 以一个范围明确的页面或流程为单位交接，记录范围、复验结果与下一步。 |
| stitch-utilities | [taste-design](https://github.com/google-labs-code/stitch-skills/blob/75f4696f162000fb69fca6a31489b5b21d47a506/plugins/stitch-utilities/skills/taste-design/SKILL.md) | 让字体、构图、强调色和动效服务于产品任务与无障碍。 |
