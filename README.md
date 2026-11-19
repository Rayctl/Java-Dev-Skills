# Java-Dev-Skills

面向 Java 后端开发的三个 Codex Skills，分别帮助理解业务需求、设计与实现代码、安全协作 Git。可以按任务独立使用，也可以配合使用。

## 该用哪个 Skill

| 当前要做的事 | 调用入口 | 负责什么 |
| --- | --- | --- |
| 理解 PRD、梳理业务、确认关键决定 | `$prd-business-understanding` | 区分需求、现状、方案和未决事项，解释改动与业务的关系 |
| 分析、规划、实现或审查具体 Java 代码 | `$java-code-design-and-development` | 检查依据、行为、可维护性、注释、排障和验证 |
| 开始 Git 仓库开发，或进行提交、集成和推送 | `$git-safe-collaboration` | 确认开发目标与基线，保护已有修改和提交来源，核验操作目标 |

详细说明：[PRD 业务理解与协作](prd-business-understanding/README.md) · [Java 代码设计与开发](java-code-design-and-development/README.md) · [Git 安全协作](git-safe-collaboration/README.md)

## Java Skill 的六类能力

| 检查方向 | 你可以期待它关注的问题 |
| --- | --- |
| **改动依据** | 是否理解上下文，是否把猜测或偏好当成业务要求 |
| **业务行为** | 数据、状态、默认值、失败和兼容行为是否一致 |
| **理解与维护** | 名称、方法、参数和结构是否容易读懂、修改 |
| **有效注释** | 是否说明必要原因与约束，是否与当前逻辑一致 |
| **失败与排障** | 用户能否理解错误，开发能否凭记录定位问题 |
| **执行可靠性与验证** | 事务、资源、缓存、重试等是否可靠，验证结论是否有证据 |

六类能力保留在一个 Java Skill 中，详细规则按需读取。它们不是六个必跑流程，也不代表每项都由脚本自动检查。

已确认的业务契约、正确性和验证真实性必须满足；方法拆分、三元表达式和类型放置需要结合实际权衡；标点、空行、集合后缀等默认偏好服从项目和用户要求。另一种合理写法本身不构成缺陷。

Java Skill 的阶段流程、例子与完整规则索引见 [使用说明](java-code-design-and-development/README.md)。

## 怎样配合工作

1. **PRD 驱动的任务**先明确业务协作方式，复用已确认的需求和决定；非 PRD 任务无需经过这一步。
2. **进入 Git 仓库的实质代码规划或修改前**，由 Git Skill 确认开发目标与基线，再应用语言规则。普通解释和固定提交的只读分析使用相应边界，不机械启动开发检查。
3. **Java 规划与实现中**，先理解上下文和验收依据，复杂流程按阶段检查，简单任务保持局部。分析和审查默认只读，不自动变成重构。
4. **交付前**核对相关测试与代码变更带来的配置、数据迁移或兼容条件。实际发布、审批及生产操作属于项目交付流程，Skill 检查通过不授予这些权限。
5. **收到运行反馈时**区分现象与已证实原因，限定修复范围，补充有价值的回归验证。

这些是协作关系，不要求所有任务走完五步。Git 的开发分支、比较目标、集成目标与推送目标分别核实；检查通过不自动授权提交、推送或历史改写，具体行为以 [Git Skill](git-safe-collaboration/SKILL.md) 为准。

## 安装与调用

```bash
git clone git@github.com:Rayctl/Java-Dev-Skills.git
cd Java-Dev-Skills
```

按需选择 Skill，依照各自 README 安装到 `~/.codex/skills`。例如在 PowerShell 中安装 Java Skill：

```powershell
Copy-Item -Recurse -Force ".\java-code-design-and-development" "$env:USERPROFILE\.codex\skills"
```

显式调用示例：

```text
使用 $prd-business-understanding 和我一起梳理这份 PRD
使用 $java-code-design-and-development 分析这个方法，先不要修改
使用 $git-safe-collaboration 核对这次推送的目标和提交
```

各 Skill 的 `agents/openai.yaml` 声明调用策略。需要稳定触发时，可在自己的 `AGENTS.md` 配置相应入口和适用范围；详细规则留在 Skill 中，避免多处复制。

## 本地项目提示

Java Skill 支持可选的 `.codex/project-guidance.md`，保存稳定的日志入口、工具查找线索和验证提示。它按章节核实，只是参考，不缓存类清单、调用关系、依赖版本或方法配方。

创建和刷新需要授权，通过 Git 本地排除保存，不修改仓库 `.gitignore`。当前证据和正式规则优先，不能因核实一个章节就把整份提示标为最新。详见 [项目提示规则](java-code-design-and-development/references/project-guidance.md)。

## 检查结果怎样理解

- **单元测试**验证脚本的已覆盖行为。
- **Skill 与语义场景结构校验**验证文件格式和结构，不证明模型做出了正确判断。
- **语义评测**需要查看实际输出，判断是否符合业务证据和规则，并允许合理替代方案。
- **Java 样式检查器**默认输出 `ADVISORY` 提示，退出码 `0` 仍可能包含候选项；显式 `--enforce-rule` 命中才阻断。旧全规则门禁可用 `--enforce-rule all`，详见 [检查器说明](java-code-design-and-development/references/checker.md)。

检查结果应说明实际覆盖范围和缺口。测试数量、干净工作区或一次检查通过，都不能单独证明需求已经正确完成。

## 仓库如何维护

每个 Skill 的 README 面向使用者，`SKILL.md` 是执行入口，`references/` 保存按需读取的权威细则，`scripts/` 和 `tests/` 负责确定性能力，`evals/` 保存语义场景与评测方式（按各 Skill 实际需要提供）。

新增规则先明确问题、适用范围、例外和验证方式；优先归入已有能力并合并重复。个人偏好不提升为通用缺陷，项目特例不扩散为所有 Java 仓库的要求。独立业务目标或明显不同的权限流程，才是考虑新增顶层 Skill 的依据。
