# GitHub Skill 调研与取舍

研究基准日：2026-11-12。Star 是检索时快照，只反映关注度，不等于安装量、活跃使用人数或质量认证。没有可核验的全站使用量，因此不声称这些是全球使用最多的 Skill。

本次检索 21 个候选仓库，下载并阅读重点正文/规则片段的 Skill 文件共 32 个；没有逐一审计仓库内全部 Skill。部分路由型 Skill 只阅读入口，未将其未读子文档视为已审查。

## 检索方法

- GitHub repository search 使用 agent skills、skills java go rust、frontend design skills、postgres skills、skills security rust、skills android ios，按 stars 降序取样
- 补充语言生态、平台厂商、安全团队与设计专业仓库，避免单纯依赖宽泛搜索
- 读取仓库元数据、递归树、固定提交下的相关 SKILL.md 与可用许可证，不执行远程脚本
- 别名或改名仓库使用 API 返回的 canonical full_name，记录固定提交，防止 main 分支漂移
- 搜索不是全站完备排名，正文未读、许可不清或不适用内容不纳入实现规则

## 候选与处理

| 仓库 | Star 快照 | 许可线索 | 处理与取舍 |
| --- | ---: | --- | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa) | 322,411 | MIT | 参考职责边界与领域词汇；不采用固定文件或交互仪式 |
| [obra/superpowers](https://github.com/obra/superpowers/tree/22f0b463e7a5e579904dd6211a520321035526f7) | 316,477 | MIT | 参考先定位根因与结论前验证；不覆盖 Java 测试偏好或强制代理流程 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC/tree/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b) | 301,609 | MIT | 参考按语言和框架识别的组织方式；修正无条件线程、对象池与风格规则 |
| [anthropics/skills](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579) | 193,388 | frontend-design: Apache-2.0；各技能分别核对 | 参考设计意图、内容与自我审查；仅研究 frontend-design，不复制正文 |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/6ae86f61f520d6ca229d2f40e070410638c908c5) | 148,406 | MIT | 参考任务情境、体系与无障碍优先；不捆绑上游脚本或风格数据库 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/tree/301b02b12bff98e4688e6984af6556802322bbde) | 116,253 | MIT | 参考契约优先、幂等与性能测量闭环；按项目版本核对 |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/tree/f6b76575f949707b4e3c37cd86cb44b0b98643e8) | 113,848 | MIT | 参考一致视觉语言与真实页面验收；排除固定整屏布局与强制动效 |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills/tree/00f9c4077878be6ffcc093c099f05a6cccaf1b95) | 49,581 | 根 MIT，另有 LICENSE-CONTENT，未合入 | 仅发现与路径索引；内容量大且存在独立内容许可，未导入正文 |
| [wshobson/agents](https://github.com/wshobson/agents/tree/9c61ab243def98f72da12abd41cfcf5bcd91af9d) | 42,431 | MIT | 参考按领域拆分及平台/所有权检查；不接受将语言内存安全简单排成绝对等级 |
| [github/awesome-copilot](https://github.com/github/awesome-copilot/tree/30a0d7465b14b05e05949d6588b99f7af0c537b4) | 41,064 | MIT | 参考 plain Java 工具链与框架范围；不继承与作者 Java 测试约定冲突的流程 |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills/tree/6d483e29da745a010d88974ef6d0e50d15755e9a) | 37,109 | MIT | 作为发现索引，不计为已阅读或导入的 Skill |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62) | 33,930 | 未检测到根许可 | 仅研究 Web 审查工作流；未检测到许可，不复制分发上游内容 |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills/tree/9ca476d8401f8750f92f4a7b31ec68efaa61ab02) | 29,682 | MIT | 仅发现与领域索引，未读取或导入具体 Skill 正文 |
| [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills/tree/078a25cc5bfd8011459be7b91d004e900c1d02d3) | 12,331 | MIT | 参考 Vue 与 SQL 的任务路由；不采用强制迁移 Options API 或对写查询直接 ANALYZE |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills/tree/0337446dadde6f8c94210444e2aa9d546126480f) | 8,746 | Apache-2.0 | 参考设计 tokens 与体系一致性；不要求安装或写入 Stitch 服务 |
| [trailofbits/skills](https://github.com/trailofbits/skills/tree/e4dd0bb5b15535f7c5a0834187dffba6ac37e4ff) | 8,147 | CC-BY-SA-4.0 | 仅研究审查范围与性质验证主题；CC-BY-SA 内容不复制、翻译或合入 MIT 正文 |
| [antfu/skills](https://github.com/antfu/skills/tree/d524ed287eef22757297827ce42e3cad88abd20c) | 6,065 | MIT | 参考 Vue/Pinia 的状态所有者与生态路由；版本相关语义以官方为准 |
| [expo/skills](https://github.com/expo/skills/tree/a9e5bd3fa00b4e61f632e43f85da73aee1942582) | 4,117 | MIT | 参考原生语义 tokens 与复用边界；不强制将现有 App 迁移到 Expo |
| [vuejs-ai/skills](https://github.com/vuejs-ai/skills/tree/198f0cd8f7f9c0a3d9b566ccc16de6677519ee78) | 3,331 | MIT | 参考组件职责、响应式、路由与清理；不强制改写既有架构 |
| [supabase/agent-skills](https://github.com/supabase/agent-skills/tree/c9be0e931b7930f7d02126d04774d904c381e7d7) | 3,045 | MIT | 参考 Postgres 按影响分类；数据库细则以官方版本与实际查询验证 |
| [ehmo/platform-design-skills](https://github.com/ehmo/platform-design-skills/tree/dc2be825d8b439caea78e9eaa8fb3ac23b0ff3e9) | 641 | MIT | 参考平台差异与可访问性检查；排除未加适用条件的全称审美规则 |

## 已读取的重点入口

以下链接固定到本次实际获取的提交。读取表示调研，不表示安装、全文复制或接受上游全部要求。

- [Jeffallan/claude-skills · skills/sql-pro/SKILL.md](https://github.com/Jeffallan/claude-skills/blob/078a25cc5bfd8011459be7b91d004e900c1d02d3/skills/sql-pro/SKILL.md)
- [Jeffallan/claude-skills · skills/vue-expert/SKILL.md](https://github.com/Jeffallan/claude-skills/blob/078a25cc5bfd8011459be7b91d004e900c1d02d3/skills/vue-expert/SKILL.md)
- [Leonxlnx/taste-skill · skills/taste-skill/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/f6b76575f949707b4e3c37cd86cb44b0b98643e8/skills/taste-skill/SKILL.md)
- [addyosmani/agent-skills · skills/api-and-interface-design/SKILL.md](https://github.com/addyosmani/agent-skills/blob/301b02b12bff98e4688e6984af6556802322bbde/skills/api-and-interface-design/SKILL.md)
- [addyosmani/agent-skills · skills/performance-optimization/SKILL.md](https://github.com/addyosmani/agent-skills/blob/301b02b12bff98e4688e6984af6556802322bbde/skills/performance-optimization/SKILL.md)
- [affaan-m/ECC · skills/cpp-coding-standards/SKILL.md](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/cpp-coding-standards/SKILL.md)
- [affaan-m/ECC · skills/golang-patterns/SKILL.md](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/golang-patterns/SKILL.md)
- [affaan-m/ECC · skills/java-coding-standards/SKILL.md](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/java-coding-standards/SKILL.md)
- [affaan-m/ECC · skills/python-patterns/SKILL.md](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/python-patterns/SKILL.md)
- [affaan-m/ECC · skills/rust-patterns/SKILL.md](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/rust-patterns/SKILL.md)
- [antfu/skills · skills/pinia/SKILL.md](https://github.com/antfu/skills/blob/d524ed287eef22757297827ce42e3cad88abd20c/skills/pinia/SKILL.md)
- [antfu/skills · skills/vue/SKILL.md](https://github.com/antfu/skills/blob/d524ed287eef22757297827ce42e3cad88abd20c/skills/vue/SKILL.md)
- [anthropics/skills · skills/frontend-design/SKILL.md](https://github.com/anthropics/skills/blob/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/frontend-design/SKILL.md)
- [ehmo/platform-design-skills · skills/android/SKILL.md](https://github.com/ehmo/platform-design-skills/blob/dc2be825d8b439caea78e9eaa8fb3ac23b0ff3e9/skills/android/SKILL.md)
- [ehmo/platform-design-skills · skills/ios/SKILL.md](https://github.com/ehmo/platform-design-skills/blob/dc2be825d8b439caea78e9eaa8fb3ac23b0ff3e9/skills/ios/SKILL.md)
- [expo/skills · plugins/expo/skills/expo-design-system/SKILL.md](https://github.com/expo/skills/blob/a9e5bd3fa00b4e61f632e43f85da73aee1942582/plugins/expo/skills/expo-design-system/SKILL.md)
- [github/awesome-copilot · skills/java-development/SKILL.md](https://github.com/github/awesome-copilot/blob/30a0d7465b14b05e05949d6588b99f7af0c537b4/skills/java-development/SKILL.md)
- [google-labs-code/stitch-skills · plugins/stitch-design/skills/manage-design-system/SKILL.md](https://github.com/google-labs-code/stitch-skills/blob/0337446dadde6f8c94210444e2aa9d546126480f/plugins/stitch-design/skills/manage-design-system/SKILL.md)
- [mattpocock/skills · skills/engineering/codebase-design/SKILL.md](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/codebase-design/SKILL.md)
- [mattpocock/skills · skills/engineering/domain-modeling/SKILL.md](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/domain-modeling/SKILL.md)
- [nextlevelbuilder/ui-ux-pro-max-skill · .claude/skills/ui-ux-pro-max/SKILL.md](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/6ae86f61f520d6ca229d2f40e070410638c908c5/.claude/skills/ui-ux-pro-max/SKILL.md)
- [obra/superpowers · skills/systematic-debugging/SKILL.md](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/systematic-debugging/SKILL.md)
- [obra/superpowers · skills/verification-before-completion/SKILL.md](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md)
- [supabase/agent-skills · skills/supabase-postgres-best-practices/SKILL.md](https://github.com/supabase/agent-skills/blob/c9be0e931b7930f7d02126d04774d904c381e7d7/skills/supabase-postgres-best-practices/SKILL.md)
- [trailofbits/skills · plugins/property-based-testing/skills/property-based-testing/SKILL.md](https://github.com/trailofbits/skills/blob/e4dd0bb5b15535f7c5a0834187dffba6ac37e4ff/plugins/property-based-testing/skills/property-based-testing/SKILL.md)
- [trailofbits/skills · plugins/rust-review/skills/rust-review/SKILL.md](https://github.com/trailofbits/skills/blob/e4dd0bb5b15535f7c5a0834187dffba6ac37e4ff/plugins/rust-review/skills/rust-review/SKILL.md)
- [vercel-labs/agent-skills · skills/web-design-guidelines/SKILL.md](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/web-design-guidelines/SKILL.md)
- [vuejs-ai/skills · skills/vue-best-practices/SKILL.md](https://github.com/vuejs-ai/skills/blob/198f0cd8f7f9c0a3d9b566ccc16de6677519ee78/skills/vue-best-practices/SKILL.md)
- [vuejs-ai/skills · skills/vue-router-best-practices/SKILL.md](https://github.com/vuejs-ai/skills/blob/198f0cd8f7f9c0a3d9b566ccc16de6677519ee78/skills/vue-router-best-practices/SKILL.md)
- [wshobson/agents · plugins/systems-programming/skills/memory-safety-patterns/SKILL.md](https://github.com/wshobson/agents/blob/9c61ab243def98f72da12abd41cfcf5bcd91af9d/plugins/systems-programming/skills/memory-safety-patterns/SKILL.md)
- [wshobson/agents · plugins/ui-design/skills/mobile-android-design/SKILL.md](https://github.com/wshobson/agents/blob/9c61ab243def98f72da12abd41cfcf5bcd91af9d/plugins/ui-design/skills/mobile-android-design/SKILL.md)
- [wshobson/agents · plugins/ui-design/skills/mobile-ios-design/SKILL.md](https://github.com/wshobson/agents/blob/9c61ab243def98f72da12abd41cfcf5bcd91af9d/plugins/ui-design/skills/mobile-ios-design/SKILL.md)

## 合并原则

- 本仓库规范为独立中文编写，采用通用工程概念和经过验证的官方契约，不拼接或逐句翻译上游 Skill
- 不把热度等同正确性，不继承远程执行、自动推送、强制付费工具或无关代理调度
- 个人约定集中在 profile.md；与上游测试、格式、框架和 UI 偏好冲突时保留本仓库明确规则
- 语言标准、框架契约、HIG/Material、WCAG 和 OWASP 等权威资料单独列于 sources.md
- 保留取得的适用开源许可及来源说明，具体文件许可不能仅凭 GitHub 的仓库级 license 字段推断
- CC-BY-SA 与未发现许可的内容仅用于研究发现，不复制其表达、代码、数据库或脚本到 MIT 正文

## 后续更新

更新时重新读取来源、版本、许可和实际规则，记录增删原因。不要下载整个技能库后全部启用，也不要无审查地随上游 main 自动同步。
