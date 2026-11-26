# Google DESIGN.md 格式

[English](../../product/design-md.md) | **简体中文** | [规范索引](../translations.md)

团队与 Agent 需要共享界面设计约定时，可使用 `DESIGN.md`。YAML 保存准确的设计令牌，Markdown 说明使用场景、状态和例外。Google 将格式标为 `alpha`。项目已有主题或令牌仓库时，先明确权威来源和同步方向。

## DM01 格式与引用

- 将令牌放在顶部 YAML front matter、相关章节的 `yaml` 代码块，或组合使用。同一顶层键在全文只定义一次。使用带引号的点分路径引用，例如 `"{colors.primary}"`。组件可以引用复合字体令牌。
- 固定版本规范支持在 `colors`、`typography`、`rounded` 和 `spacing` 下组织分组。检查扁平键与分组路径生成同名令牌的冲突。主题切换由目标运行时负责，并核对所用工具对分组令牌的支持。
- 为解析器保留下方示例所示的英文 `##` 标题和顺序。正文可使用简体中文。保留适用章节，用规范的 `omitted` 配置声明有意省略的内容。
- 在行内代码中用 `@path[#fragment]` 引用本地交接材料。从 `DESIGN.md` 所在目录解析引用。Markdown 片段匹配标题 slug，HTML 片段匹配元素 ID 或组件标记。引用目标须位于文档目录内。

## DM02 示例

将代码块内的内容保存为 `DESIGN.md`，并按项目设计替换示例中的令牌与说明。

```markdown
---
version: alpha
name: Field Console
colors:
  primary: "#15355B"
  on-primary: "#FFFFFF"
typography:
  body-md:
    fontFamily: system-ui
    fontSize: 1rem
rounded:
  control: 6px
spacing:
  control: 12px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.control}"
    padding: "{spacing.control}"
---

## Overview

服务于查看设备状态的操作员。

## Colors

主色用于主要操作。

## Typography

控件与状态文本使用系统字体。

## Layout

关联操作之间采用控件间距。

## Elevation & Depth

用边框区分相邻区域。

## Shapes

按钮使用控件圆角。

## Motion & Micro-interaction

保持反馈短促，适配减少动效设置。

## Voice & Content Strategy

使用能说明结果的动词。

## Components

主要操作使用主按钮样式。

## Do's and Don'ts

禁用操作时保留可见标签。
```

## DM03 校验与导出

使用项目锁定的 CLI 版本。下方命令使用 npm 发布版 `0.4.0`。比较版本前，先将基线保存为 `DESIGN.base.md`。

npm 0.4.0 会忽略上游的 `motion` 令牌映射。示例将动效写入正文，以兼容该版 CLI。

```text
npx @google/design.md@0.4.0 lint DESIGN.md
npx @google/design.md@0.4.0 diff DESIGN.base.md DESIGN.md
npx @google/design.md@0.4.0 export --format dtcg DESIGN.md
npx @google/design.md@0.4.0 export --format css-tailwind DESIGN.md
npx @google/design.md@0.4.0 export --format json-tailwind DESIGN.md
```

- 先运行 `lint`，检查结构、引用与报告中的组件令牌对比度，再导出。产品验收时，在目标界面检查实际渲染的主题、对比度、焦点和状态变化。
- 查看 `diff` 输出及对应的正文改动。即使命令成功，也要检查删除或修改的令牌影响哪些组件。
- 根据目标选择 DTCG JSON、Tailwind v4 CSS 或 Tailwind v3 JSON。使用前核对导出警告和解析值，接入后检查运行时主题映射及实际效果。

需要提取或生成界面并在目标技术栈中实现时，参见 [Stitch 工作流](stitch-workflow.md)。

[Google 格式规范](https://github.com/google-labs-code/design.md/blob/db977b3c1d1f309269f43d5d17ae828d54bd6ae3/docs/spec.md) · [上游 CLI 文档](https://github.com/google-labs-code/design.md/blob/db977b3c1d1f309269f43d5d17ae828d54bd6ae3/README.md) · [Apache-2.0 归属](../../../THIRD_PARTY_NOTICES.zh-CN.md#google-designmd)
