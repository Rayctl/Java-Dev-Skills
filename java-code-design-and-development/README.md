# Java 代码设计与开发

`$java-code-design-and-development` 帮助 AI 在理解具体 Java 代码、制定方案、编码和审查时，保持行为正确、代码清楚、验证可信。它使用一个入口，按当前问题读取详细规则。

## 它检查什么

| 六类能力 | 主要检查 | 典型例子 | 详细规则 |
| --- | --- | --- | --- |
| **改动依据** | 需求、当前事实、相关上下文和假设是否分清 | 没看调用方就改字段，或凭空增加默认值和限制 | [上下文与证据](references/evidence-and-verification.md) |
| **业务行为** | 输入到输出的含义、状态和边界是否一致 | 转换丢字段、重复键任意取值、新旧数据含义混用 | [契约与生命周期](references/contracts-and-lifecycles.md) |
| **理解与维护** | 名称、方法、参数和结构是否便于阅读与修改 | 布尔参数靠位置猜，短包装隐藏关键信息，共享规则散落多处 | [方法设计](references/method-design.md)、[命名](references/naming.md)、[控制流](references/control-flow.md) |
| **有效注释** | 是否补充必要信息，并与当前行为一致 | 复杂阶段缺少原因，注释复述代码，旧注释与新逻辑冲突 | [注释与 JavaDoc](references/comments-and-javadoc.md) |
| **失败与排障** | 异常是否可理解，记录是否足以定位问题 | 错误原因与恢复建议不符，第三方详情丢失，日志无法关联请求 | [异常沟通](references/exception-communication.md)、[远程调用](references/remote-calls.md) |
| **执行可靠性与验证** | 执行顺序、资源归属和验证结论是否可信 | 重试重复写入、资源未关闭、Mock 测试被当成真实链路验证 | [契约与生命周期](references/contracts-and-lifecycles.md)、[验证依据](references/evidence-and-verification.md) |

这些是检查方向，不是六个独立流程。一个异常分支可能同时涉及业务行为、注释、日志和验证，应结合起来判断。简单修改只读取相关细则。

## 哪些必须满足，哪些可以选择

| 性质 | 处理方式 | 例子 |
| --- | --- | --- |
| **必须满足的要求** | 根据已确认契约和实际影响识别问题 | 不擅自改变业务含义；不丢失必要的错误原因；正确管理事务和资源；如实报告验证 |
| **需要权衡的判断** | 比较完整写法和维护成本，允许多种合理方案 | 是否抽方法、集中异常文案、保留嵌套类型或使用三元表达式 |
| **可覆盖的偏好** | 没有更高优先级要求时作为默认建议 | 注释句号、方法空行、大括号、集合后缀和换行习惯 |

用户明确要求和正式项目规则优先；源码中的常见写法是参考，不自动成为强制规范。可选偏好不作为缺陷；违反当前适用的风格要求时最高按 P3，行为、数据、诊断和生命周期问题按实际影响分级。

例如，三个明显的必要字段判空不必补“校验参数”；`String name = user == null ? null : user.getName();` 可以保留。短异常工厂若维护一个真实共享的错误契约，也可以保留。判断依据是缺少什么信息、是否容易误用、是否增加维护成本。

同样准确时优先使用团队熟悉的词；必要的领域术语可保留。业务异常原因与有效恢复动作必须对应。项目已确认全量业务报文时遵循其约定，凭据原值的记录范围另行确认，不能仅凭“全量”推导授权。

## 在开发过程中怎样使用

| 阶段 | 应做的检查与交接 |
| --- | --- |
| 理解需求 | 确认目标、允许改变的行为、代表性输入与预期结果，查证重要假设 |
| 制定方案 | 比较职责、数据和失败路径、复用机会及成本，提前说明如何验证 |
| 编码过程 | 简单修改做局部预检和最终检查；复杂流程在有意义的阶段交接时核对 |
| 测试与审查 | 按已确认需求验证正常、边界、失败和兼容行为，说明 Mock 和环境限制 |
| 交付准备 | 涉及配置、数据格式、API 或事件时，检查必要的迁移、版本共存、发布顺序和回退兼容条件 |
| 反馈与维护 | 区分现象、可能路径和已证实原因，限定修复范围，并补充有价值的回归验证 |

阶段可以重叠或反复，不要求每个任务生成完整文档。普通改名不会启动发布方案、性能测试或安全审计。数据量、查询次数、权限和敏感信息等，只在改动实际涉及时按项目依据检查，不编造通用指标。

规划、分析和审查默认只读；修改需要任务授权。明确点名的既有方法、类或有限模块，即使没有 diff，也可以检查。实现和 diff 审查限于当前任务变更或选定对比；周边代码用于理解，不扩大为历史代码整改。

完整流程与交接边界见 [任务模式](references/task-modes.md)。PRD 理解、Git 操作和实际发布审批各有自己的流程；Java Skill 使用已确认的决定，检查其代码影响。识别交付风险不等于获准执行发布。

完成时简要说明本次相关检查、实际验证和重要缺口，例如“检查了命名、异常和远程日志；接口测试通过，生产日志可用性尚未验证”。不要求每次输出六栏清单。

## 调用与安装

在已安装后，可直接请求：

```text
使用 $java-code-design-and-development 分析这个 Java 方法的行为和可改进点，先不要修改
使用 $java-code-design-and-development 按已确认方案实现，并验证相关行为
使用 $java-code-design-and-development 审查这次 Java diff
```

`agents/openai.yaml` 允许隐式调用。需要稳定加载时，可在自己的 `AGENTS.md` 明确要求：在规划、分析、修改或审查具体 Java 后端代码时读取本 Skill，并按触发条件读取引用。通用 Java 问答和无关文档任务不触发。

从仓库根目录安装，或用当前文件更新本机同名副本：

```powershell
git clone git@github.com:Rayctl/Java-Dev-Skills.git
cd Java-Dev-Skills
Copy-Item -Recurse -Force ".\java-code-design-and-development" "$env:USERPROFILE\.codex\skills"
```

安装入口是 `~/.codex/skills/java-code-design-and-development/SKILL.md`。Git Bash 可在仓库根目录使用 `cp -R ./java-code-design-and-development "$HOME/.codex/skills/"`。

## 本地项目提示

可选的 `.codex/project-guidance.md` 保存稳定的日志入口、工具查找线索、验证入口和偏好。它只是参考，不保存类清单、调用关系、依赖版本或方法配方；使用时以当前证据为准。

只读取当前任务相关章节。实现任务涉及相关设施且文件缺失时询问一次，拒绝后继续正常检查；普通改名、注释和局部判断不询问初始化。创建或刷新需授权，通过 Git 本地排除保存，不修改仓库 `.gitignore`；已跟踪文件不能当作纯本地文件。

章节各自记录核实基线，不能因更新一节就把全部提示标为最新。Git 基线复用、失效检查、未提交基础设施及已有文件缺少章节的处理，统一以 [项目提示规则](references/project-guidance.md) 为准。

## 自动检查能证明什么

Python 检查器只检测六类固定模式：注释句号、方法空行、缺少大括号，以及 catch、入口判断组、复杂方法可能缺少说明的结构。后三类只能提醒进一步阅读，不能证明注释必须存在或写得正确。

默认结果为 `ADVISORY`；退出码 `0` 仍可能有候选项。仅显式选择的规则命中才返回 `1`，参数、输入或环境错误返回 `2`。旧门禁若确实需要全部规则，可使用 `--enforce-rule all` 恢复原阻断行为。不要为消除提示改写符合项目规范的代码。

```powershell
# 当前暂存、未暂存和未跟踪 Java 变更
py -3 ".\java-code-design-and-development\scripts\check_java_backend_style.py" --changed --repo "C:\path\to\repo"

# 项目明确要求大括号时，只将该规则作为阻断项
py -3 ".\java-code-design-and-development\scripts\check_java_backend_style.py" --changed --repo "C:\path\to\repo" --enforce-rule STYLE-BRACE-001

# 指定对比基线或行范围
py -3 ".\java-code-design-and-development\scripts\check_java_backend_style.py" --changed --base origin/main --repo "C:\path\to\repo"
py -3 ".\java-code-design-and-development\scripts\check_java_backend_style.py" --line-range "C:\path\to\Example.java:20-80"
```

完整参数、范围和规则编号见 [检查器说明](references/checker.md)。脚本通过不代表业务正确，AI 语义检查也需要实际代码、契约和测试证据。

## 详细规则在哪里

以下文件是细则的权威位置，README 负责解释能力和导航：

| 文件 | 负责内容 |
| --- | --- |
| [task-modes.md](references/task-modes.md) | 任务模式、读写范围、生命周期交接 |
| [evidence-and-verification.md](references/evidence-and-verification.md) | 上下文、验收依据、质量要求、诊断证据、最终回读 |
| [contracts-and-lifecycles.md](references/contracts-and-lifecycles.md) | 数据契约、事务、缓存、重试、补偿、锁、资源 |
| [method-design.md](references/method-design.md) | 方法、常量、参数、回调、类型及维护成本 |
| [naming.md](references/naming.md) | 职责命名、通俗词、集合、状态、枚举 |
| [control-flow.md](references/control-flow.md) | 分支、循环、三元表达式、大括号和换行 |
| [comments-and-javadoc.md](references/comments-and-javadoc.md) | 注释内容、位置、更新和格式 |
| [exception-communication.md](references/exception-communication.md) | 原因、错误分类、恢复动作、用户提示和内部诊断 |
| [remote-calls.md](references/remote-calls.md) | 第三方日志、错误保留、映射、超时与重试 |
| [structure-choice.md](references/structure-choice.md) | 有实际收益时的结构建议；纯审查不主动启动 |
| [project-guidance.md](references/project-guidance.md) | 本地提示的发现、授权、基线和失效处理 |
| [checker.md](references/checker.md) | 检查器范围、提示与阻断、能力边界 |

规则参考 Clean Code 作者公开文章、《程序员修炼之道》公开节选、Fowler 重构目录及相关官方文档，出处放在对应引用中。它们提供判断方法，不把书名、方法行数或个人习惯当成通用结论。

## 验证与维护

在仓库根目录执行：

```powershell
py -3 -m unittest discover -s ".\java-code-design-and-development\tests" -p "test_*.py"
py -3 "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\java-code-design-and-development"
py -3 ".\java-code-design-and-development\scripts\validate_semantic_evals.py"
py -3 ".\java-code-design-and-development\scripts\verify_skill_installation.py" --source ".\java-code-design-and-development" --target "$env:USERPROFILE\.codex\skills\java-code-design-and-development"
```

单元测试验证脚本行为；`quick_validate.py` 和语义场景 JSON 校验验证结构；安装比对验证文件清单及 SHA-256 一致。它们都不能代替独立模型行为评测。用 [语义场景](evals/semantic-cases.json) 和 [评测模板](evals/forward-evaluation-template.md) 记录实际决策、证据、加载引用和成本，具体方式见 [评测说明](evals/README.md)。

后续新增规则先归入现有能力，说明解决的问题、允许的例外和验证方法。细则只在对应引用维护，重复规则合并；只有出现独立任务和不同权限边界时，再考虑拆出顶层 Skill。
