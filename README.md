# Skills

个人维护的 Codex skills 仓库。每个 skill 使用独立目录，并在目录内提供面向使用者的 README 和面向 Codex 的 `SKILL.md`。Skill 入口保持精简，详细规则按任务触发后从 `references/` 渐进读取

## Skills

| Skill | 用途 |
| --- | --- |
| [git-safe-collaboration](git-safe-collaboration/README.md) | 核对开发目标，安全更新，保留提交来源，管理已授权集成及推送前复核 |
| [Java 代码设计与开发](java-code-design-and-development/README.md) | 使用 `$java-code-design-and-development`，在具体 Java 后端代码的规划、分析、实现和审查中应用质量规则 |
| [prd-business-understanding](prd-business-understanding/README.md) | 在 PRD 驱动的规划和实现中梳理旧行为、变化、兼容要求及关键决策依据 |

PRD 驱动的规划或实现任务使用 prd-business-understanding，并按用户表达识别梳理或规划模式。先核对现状、契约和字段流转，区分事实、需求、方案和未决决策；排查疑点不自动扩大修改范围，需求更新只替换受影响决定。保留公共接口的兼容与失败行为，按职责整理内部实现，无须逐个审批方法或类。完成时映射场景、改动位置和验证结果；非 PRD 任务不触发该流程。

## 推荐流程

对 Git 仓库中的实质代码规划和修改任务，先由 `$git-safe-collaboration` 确认本地代码基线和远端新鲜度，再按语言加载对应质量 Skill；普通解释和固定提交的只读分析不要求开发新鲜度检查，明确的 Git 操作使用各自流程。检查本身只读；工作区干净且结果确认为 `BEHIND` 时，先告知用户，再按 Skill 已授权的策略尝试一次安全快进。无法确定提交关系时，先请求授权；工作区有修改时禁止更新，只按 Skill 的范围规则继续已有相关工作。缺少或删除远端目标、未完成 Git 操作及本地 Git 错误会停止开发。实际推送前还要独立核对指定的已有目标分支。

具体 Java 代码或实现方案的规划、分析、实现和审查使用 `$java-code-design-and-development`。规划先评估相关契约和风险；分析可以检查明确点名但尚未改动的代码并比较优化方案；实现与 diff 审查保持当前任务的变更范围。规划、分析和审查默认只读，不为采用另一种合理设计而报告问题。复杂行为按需加载事务、异常、远程调用和生命周期规则，简单任务不会扫描无关历史代码；未编辑源码时不机械运行检查器或完整测试套件。

## 项目提示

Java Skill 可选读取仓库本地的 `.codex/project-guidance.md`。该文件通过 Git 本地排除保存，只记录日志入口、工具库、远程包装方式和验证命令等稳定提示，不记录类清单、调用关系、字段含义或依赖版本。它只是参考信息，当前源码、构建配置、测试、正式文档和用户要求优先。项目提示按章节核实，不能把一次局部核实当成整个文件已更新。

## Java 质量规则

Java Skill 将规则分为两层：

- 质量门禁：调用方可理解的职责、数据和状态语义、异常分类与恢复动作、事务和资源生命周期、第三方诊断信息、关键阶段意图和最终状态验证
- 默认偏好：注释标点、方法间空行、控制语句大括号、集合变量后缀、三元表达式和换行方式

默认偏好服从项目 formatter、`AGENTS.md`、正式文档和用户明确要求，单纯偏好问题最高按 `P3` 处理

## 评测与验证

`java-code-design-and-development/evals/semantic-cases.json` 保存需要语义判断的代表性场景，`forward-evaluation-template.md` 用于在独立会话中记录有 Skill、无 Skill或旧版本的输出、断言证据、Token、耗时和实际加载的引用。JSON 结构通过不代表模型行为已经通过，仍需独立会话或人工评测

各 Skill 可用 quick_validate.py 校验结构；Git 和 Java Skill 另有各自测试，Java Skill 还提供只读检查器，用于检查当前任务 Java 变更的确定性格式问题；PRD Skill 的语义评测目录可由专用脚本做结构校验，但模型行为仍需独立会话或人工评测

## 安装

```bash
git clone git@github.com:Rayctl/skills.git
```

进入目标 skill 目录的 README，按其中说明安装到 `~/.codex/skills`
