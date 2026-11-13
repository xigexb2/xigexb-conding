# TypeScript

[English](../../languages/typescript.md) | **简体中文** | [规范索引](../translations.md)

所有包/目录直接同类源码最多 20 个，测试、声明与第一方生成文件合并计数；设计时按职责划分子包，遵守 [统一目录规范](../directory-structure.md)

先应用 [JavaScript](javascript.md) 的运行时规则；类型系统不能改变网络与浏览器运行语义。

- 单文件最多 380 行，使用仓库 `tsconfig`、类型检查器与 lint 配置
- 新项目优先 strict；遗留项目增量治理，不顺带引入全仓库错误
- 外部输入先以 `unknown` 接收并运行时校验；不要用 `as`、`any` 和非空断言伪造可信数据
- 用判别联合表示请求、工作流和异步状态，确保合法组合与穷尽分支
- 避免为业务简单值设计复杂类型体操；公开类型保持可诊断和可维护
- `readonly` 主要是类型层约束，不是深层冻结或跨线程同步
- 类型导入、路径别名、ESM/CJS 及声明输出以实际运行和打包方式对齐
- API DTO 的可选字段与可空字段分开，注意 undefined 在 JSON 中的丢弃行为
- 泛型表达调用关系，不把所有接口参数化；避免通过过宽联合掩盖不同职责
- 枚举、const 对象和字面量联合按项目构建链选择，不无依据统一替换
- 前后端共享 schema 需要运行时解析、版本演进和独立发布边界，不能只共享 `.d.ts`
- 运行 `tsc --noEmit` 或项目类型命令；Vue 使用项目匹配的 `vue-tsc`
- bundler 可打包不等于类型检查通过；类型检查通过不等于外部数据有效

权威依据见 [来源索引](../sources.md)：TypeScript Handbook、TSConfig Reference。
