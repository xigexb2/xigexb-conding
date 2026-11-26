# GitHub skill research and adoption decisions

**English** | [简体中文](zh-CN/github-research.md) | [Standards index](translations.md)

[2026-11-26 upstream alignment](upstream-alignment.md)

Research baseline: 2026-11-12. Stars are attention snapshots rather than installation counts, active users, or quality certification. No verifiable site-wide usage statistics establish a global most-used ranking.

The research considered 21 repositories and downloaded/read 32 selected skill bodies/rule excerpts rather than auditing every skill. For some routers only the entry point was read; unread child documents were not considered reviewed.

## Search method

- Sample GitHub repository searches by descending stars for agent skills, skills java go rust, frontend design skills, postgres skills, skills security rust, skills android ios
- Add language ecosystems, platform vendors, security teams, design specialists beyond broad search
- Read metadata, recursive trees, relevant pinned SKILL.md files, available licenses without executing remote scripts
- Use API canonical full_name for renamed/aliased repositories and record commits against main-branch drift
- This is not a complete site-wide ranking; unread, unclear-license, inapplicable content does not become implementation rules

## Candidates and decisions

| Repository | Star snapshot | License evidence | Decision |
| --- | ---: | --- | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa) | 322,411 | MIT | Reference responsibility boundaries/domain vocabulary; omit fixed-file and interaction rituals |
| [obra/superpowers](https://github.com/obra/superpowers/tree/22f0b463e7a5e579904dd6211a520321035526f7) | 316,477 | MIT | Reference root-cause analysis and verification before conclusions; preserve Java testing preferences without mandatory agent workflows |
| [affaan-m/ECC](https://github.com/affaan-m/ECC/tree/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b) | 301,609 | MIT | Reference language/framework routing; correct unconditional threading, pooling, style rules |
| [anthropics/skills](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579) | 193,388 | frontend-design: Apache-2.0; check individual skills | Reference design intent, content, self-review; study frontend-design only without copying prose |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/6ae86f61f520d6ca229d2f40e070410638c908c5) | 148,406 | MIT | Reference context, design systems, accessibility; do not bundle upstream scripts/style databases |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/tree/301b02b12bff98e4688e6984af6556802322bbde) | 116,253 | MIT | Reference contracts, idempotency, measured optimization; verify project versions |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/tree/f6b76575f949707b4e3c37cd86cb44b0b98643e8) | 113,848 | MIT | Reference coherent visual language/page acceptance; omit mandatory full-screen layouts/animations |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills/tree/00f9c4077878be6ffcc093c099f05a6cccaf1b95) | 49,581 | Root MIT plus LICENSE-CONTENT; not imported | Discovery/path index only; large content collection with separate content licensing, no prose imported |
| [wshobson/agents](https://github.com/wshobson/agents/tree/9c61ab243def98f72da12abd41cfcf5bcd91af9d) | 42,431 | MIT | Reference domain organization/platform ownership checks; reject absolute simplistic memory-safety rankings |
| [github/awesome-copilot](https://github.com/github/awesome-copilot/tree/30a0d7465b14b05e05949d6588b99f7af0c537b4) | 41,064 | MIT | Reference plain-Java tooling/framework scope; omit workflows conflicting with the author's Java testing convention |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills/tree/6d483e29da745a010d88974ef6d0e50d15755e9a) | 37,109 | MIT | Discovery index only; not counted as read/imported skill content |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62) | 33,930 | No root license detected | Study Web review workflow only; no detected license, no copied redistribution |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills/tree/9ca476d8401f8750f92f4a7b31ec68efaa61ab02) | 29,682 | MIT | Discovery/domain index only; no individual skill bodies read/imported |
| [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills/tree/078a25cc5bfd8011459be7b91d004e900c1d02d3) | 12,331 | MIT | Reference Vue/SQL routing; omit forced Options API migration and direct ANALYZE on writes |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills/tree/0337446dadde6f8c94210444e2aa9d546126480f) | 8,746 | Apache-2.0 | Reference design tokens/coherence; no mandatory Stitch installation or service writes |
| [trailofbits/skills](https://github.com/trailofbits/skills/tree/e4dd0bb5b15535f7c5a0834187dffba6ac37e4ff) | 8,147 | CC-BY-SA-4.0 | Study review scope/property verification only; no CC-BY-SA prose translation/copying into MIT material |
| [antfu/skills](https://github.com/antfu/skills/tree/d524ed287eef22757297827ce42e3cad88abd20c) | 6,065 | MIT | Reference Vue/Pinia state ownership/ecosystem routing; official version semantics govern |
| [expo/skills](https://github.com/expo/skills/tree/a9e5bd3fa00b4e61f632e43f85da73aee1942582) | 4,117 | MIT | Reference native semantic tokens/reuse boundaries; no mandatory migration to Expo |
| [vuejs-ai/skills](https://github.com/vuejs-ai/skills/tree/198f0cd8f7f9c0a3d9b566ccc16de6677519ee78) | 3,331 | MIT | Reference components, reactivity, routing, cleanup; no forced architecture rewrite |
| [supabase/agent-skills](https://github.com/supabase/agent-skills/tree/c9be0e931b7930f7d02126d04774d904c381e7d7) | 3,045 | MIT | Reference Postgres impact categories; actual official versions/query verification govern |
| [ehmo/platform-design-skills](https://github.com/ehmo/platform-design-skills/tree/dc2be825d8b439caea78e9eaa8fb3ac23b0ff3e9) | 641 | MIT | Reference platform differences/accessibility; omit unconditional universal aesthetic rules |

## Selected entries read

Links are pinned to the commits actually retrieved. Reading denotes research rather than installation, full copying, or accepting all upstream requirements.

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

## Integration principles

- The original standards were independently authored in Chinese and now have an English translation; use general concepts/verified official contracts without stitching together or translating upstream skill prose
- Popularity does not establish correctness; omit inherited remote execution, auto-push, paid-tool mandates, unrelated agent orchestration
- Personal conventions remain in profile.md and prevail over conflicting upstream testing/format/framework/UI preferences
- Language standards, framework contracts, HIG/Material, WCAG, OWASP resources are separately listed in sources.md
- Retain applicable acquired licenses/provenance; repository-level GitHub license metadata does not establish every file's license
- CC-BY-SA/unlicensed content is research/discovery only, without copying its expression, code, databases, scripts into MIT content

## Subsequent updates

Reread sources, versions, licenses, actual rules and record reasons for changes. Do not download/activate entire libraries or automatically synchronize upstream main without review.
