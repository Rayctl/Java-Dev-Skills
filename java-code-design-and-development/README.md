# Java 代码设计与开发

用于规划、分析、编写和审查具体的 Java 后端代码。会在方案形成前、理解既有逻辑或评估优化点时应用对应规则，也在编码期间和完成后检查质量。根据任务读取命名、代码结构、方法设计、注释、异常和生命周期等详细规则。

## 什么时候使用

| 模式 | 请求示例 | 处理方式 |
| --- | --- | --- |
| 规划 | “这个需求应该怎么改？” | 确认相关现状，评估职责、契约、失败处理和复杂度，说明依据、方案取舍及待执行的验证 |
| 分析 | “梳理这个方法”“这里有没有值得优化的地方？” | 追踪实际行为；需要优化评估时，区分已证实问题、待核实风险和可选改进 |
| 实现 | “按这个方案修改” | 编辑前检查上下文，复杂逻辑逐阶段核对，完成后回读并验证 |
| 审查 | “检查这次 diff”“审查这个类” | 只检查选定范围，按证据和实际影响报告问题 |

规划、分析和审查默认只读，不因发现优化点就自动改代码。用户已经授权实现时，按原有决定继续，不重复询问。普通 Java 概念问答、无关文档工作不会启动仓库质量流程。

明确点名的既有方法、类或有限模块，即使没有修改，也可以分析和审查。只评估有实际收益的优化，保留现状也可以是合理结论；另一种写法本身不是质量问题。简单任务不扫描整个模块，也不加载所有详细规则。具体边界见 [任务模式](references/task-modes.md)。

## 适用范围

以下硬性质量门禁适用于任务范围内的 Java 生产代码、测试代码及拟定行为。规划时评估相关设计风险，不将尚未编写的 JavaDoc、注释或测试报告成缺陷：

- 保留当前任务未授权改变的空值、缺失、默认值、状态和异常行为；已确认的新行为同步调整调用方和测试，不把旧实现当成不可改变的规范
- 方法和变量名称应让人在使用位置看懂具体对象、动作、状态和关键副作用
- 公共方法及承载独立业务动作或处理阶段的方法具有有效 JavaDoc
- 多步处理逐阶段检查；名称和类型无法说明的原因、前置条件、结果去向、顺序和失败后果，在对应阶段补充说明
- 注释从当前有效行为和约束出发；只有旧字段或旧路径仍承担兼容职责，或明确排除它能避免错误修改时，才保留历史对照并说明其当前作用
- 对短私有方法和仅为复用而抽出的私有常量或字段，尝试把内容直接写回使用位置，并保留更容易读懂的写法；调用次数和“减少重复”不能单独证明拆分合理
- 改变控制流的 `catch` 在行为发生前说明后续路径和保留或跳过的保证
- 用户异常提示、错误类别和真实恢复动作保持一致
- 第三方调用区分业务拒绝和技术失败，保留可定位的第三方错误信息，并按仓库约定决定日志范围
- 修改既有代码前，从目标位置追踪相关调用、数据关系、日志、异常和测试；用户点名的字段或方法只是分析起点
- 重要判断区分权威约束、实际行为、外部契约、局部惯例和默认建议，不能把偏好写成项目事实
- formatter、代码生成、测试修复或 Git hook 改动文件后，重新读取最终 diff 和受影响文件，再报告验证结果

以下是默认编码偏好，不得覆盖项目 formatter、`AGENTS.md`、正式文档或用户明确规则：

- Java 注释结尾不使用中文或英文句号，方法声明之间只保留一行空行
- 控制语句使用大括号，集合变量在有助于调用点理解时使用 `List`、`Set`、`Map` 后缀
- 名称同样准确时优先使用常见词，保留项目业务术语和必要的 Java 技术词
- 三元表达式只用于短纯值选择，较长表达式按项目行宽和可读性换行
- 默认少用内部类、静态嵌套类、局部类和嵌套枚举；确实有助于集中理解，或 Builder、框架契约需要时可以保留

偏好只在没有更高优先级依据时作为默认建议；单纯偏好问题最高报告为 `P3`，不能把通用偏好写成所有 Java 项目的正式规范。只有有证据的违规或实际理解、行为问题才分级；存在另一种合理写法，或用户希望进一步优化，本身不构成质量问题。例如位置字符串已经清楚时，可以讨论改为枚举，但不因此认定原写法有问题。

实现和 diff 审查默认限于当前任务的暂存、未暂存和未跟踪 Java 变更，也可以指定文件、行范围、提交或对比分支。规划、分析及明确指定既有代码的审查包括所选目标；周边代码用于理解相关行为，不自动扩大整改范围。不报告无关历史、生成代码和第三方代码。

没有编辑 Java 源码时，不机械运行检查器或完整测试套件；只在能回答具体问题时做针对性验证。规划说明将如何验证，分析和审查说明实际查阅和执行了什么，以及尚未确认的部分，不能把旧代码的测试结果当成新方案已经正确。

## 按需读取详细规则

`SKILL.md` 只保存每次 Java 任务都要检查的规则。详细说明分别放在下列文件中，只有遇到对应代码时才读取：

| 详细规则文件 | 什么时候读取 |
| --- | --- |
| [task-modes.md](references/task-modes.md) | 规划、分析，或需要明确任务范围、只读边界及验证方式时 |
| [project-guidance.md](references/project-guidance.md) | 需要项目设施提示时，只读取并核实已有相关章节；仅实现任务询问初始化或刷新 |
| [method-design.md](references/method-design.md) | 短私有方法、复用常量或字段、方法拆分和包装、日志辅助结构、延迟执行、参数含义及新增或修改的嵌套类型 |
| [structure-choice.md](references/structure-choice.md) | 规划、编码中存在真实变化点，或用户明确要求评估相关结构优化；纯审查不启动设计模式建议流程 |
| [comments-and-javadoc.md](references/comments-and-javadoc.md) | 编辑类、方法、JavaDoc、注释和多步方法体，或分析说明覆盖；规划只识别独立动作和隐含契约的说明需求 |
| [naming.md](references/naming.md) | 名称宽泛或用词生僻、集合和状态命名、枚举查询、`normalize`、使用位置看不出职责 |
| [exception-communication.md](references/exception-communication.md) | 异常抛出或转换、用户可见文案及其常量、错误返回、失败日志、`catch` 或 `finally` |
| [remote-calls.md](references/remote-calls.md) | HTTP、Feign、RPC、外部 SDK、请求响应日志、第三方错误解析或映射 |
| [contracts-and-lifecycles.md](references/contracts-and-lifecycles.md) | 多阶段适配、关联结果、表示转换、事务、跨存储、异步调用、缓存、重试、补偿、锁和资源生命周期 |
| [control-flow.md](references/control-flow.md) | 三元表达式、重复判断与分支组织、结构数字含义、大括号及较长表达式换行 |
| [evidence-and-verification.md](references/evidence-and-verification.md) | 修改既有行为或数据含义、关联字段、关键业务变化和输入输出的排障记录、旧日志、证据冲突，以及工具可能改写最终代码 |
| [checker.md](references/checker.md) | 基线、行范围、排除路径、范围歧义、CLI 错误和规则编号 |

简单字段、协议常量或注解调整不需要读取异常和生命周期规则；用户能看到的异常文案常量属于异常处理的一部分，需要读取对应规则。代码涉及哪些情况，就要读取哪些详细规则，不能为了节省上下文而漏掉。

## 本地项目提示

各模式可以按需读取仓库中已有的本机专属 `.codex/project-guidance.md`，仅实现任务询问创建或刷新。它记录稳定提示，例如优先查看的日志入口、已有工具库、远程调用包装方式、常用验证命令和格式偏好；不是项目正式规范，也不保存类清单、调用关系、依赖版本或字段含义等容易随代码变化的事实。

文件不存在时，只有任务涉及日志、依赖、远程调用、异常处理或构建验证，Skill 才会询问是否初始化；如果编码中途才新增这类改动，也必须在编辑该部分前重新触发检查。询问内容应同时确认要初始化哪些章节、记录哪些稳定提示，以及仓库是否已有脱敏或报文记录约定；脱敏不是默认强制项。单纯重命名、注释、局部判断和普通 CRUD 不会打扰用户。拒绝后本次任务继续正常检查且不再询问。创建前通过 `git rev-parse --git-path info/exclude`、`git check-ignore -v --no-index` 和 `git ls-files --error-unmatch` 确认路径确实是未跟踪的本地文件，不会修改仓库 `.gitignore`。

文件中的所有内容都只是参考：当前构建配置、源码、测试、正式文档和用户要求优先。格式提示本身不会产生 `P2/P3`。Skill 先读取元数据和章节标题，再按任务只读取 `Logging`、`Dependencies And Utilities`、`Remote Calls`、`Exception Handling`、`Formatting And Naming` 或 `Build And Verification` 中需要的部分。

已有文件缺少当前任务相关章节时，仍要检查对应的仓库证据；需要补充稳定提示时先询问用户，不能把文件存在当成全部设施均已核实。用户已经明确授权本次补充时直接执行，不重复询问。

工具或日志入口名称可以作为查找线索，但不要记录具体方法签名、行为说明或调用配方，使用时检查当前实现。构建提示区分普通验证命令和环境条件：只有所需依赖已缓存且无需获取更新时才使用 Maven 离线模式；缓存假设和跳过步骤也应注明条件，不能把一次成功的临时命令变成默认流程。

单次功能的取舍也不写成长期提示。例如“这次接口只记录摘要，由测算调用方处理降级”属于本次方案；“优先检查项目统一日志入口及其正式规范”才是稳定查找提示。创建文件或同意某次实现，不等于确认了全项目日志政策。即使提交基线仍有效，新的用户要求或不同调用场景也可能让旧提示不再适用。

`schema_version: 2` 为每个提示章节记录独立的 `verified_commits`。章节 SHA 必须能解析为本地提交，且是当前 HEAD 的祖先；缺失、格式错误、提交不存在或不是祖先时，该章节未经核实，需直接检查相关当前证据。校验器只解析文件头元数据，不采用正文中的示例，也不接受重复键或格式含糊的受支持映射。元数据校验通过不代表提交有效或提示仍适用。

Skill 复用 `$git-safe-collaboration` 的任务提交和远端检查结果，不重复访问远端；使用提示时另读当前本地 HEAD。从章节 SHA 检查到当前 HEAD，并包含工作区变化，因此同一任务中后来提交的构建或日志改动也会使相关提示失效。`CURRENT`、`AHEAD` 和 `UPDATED` 确认检查当时的远端新鲜度，可以同时有 `dirty=true`，不保证远端持续不变。刷新要求当前 HEAD 等于任务提交或是其后代、相关基础设施已提交、章节已重新核实且用户授权；记录实际核实的当前 HEAD，保留其他章节基线。普通业务未提交改动不单独阻止刷新。旧版、缺失或未知版本只能作为迁移线索。若提示文件已被 Git 跟踪，停止本地登记或刷新并说明，不因此阻断本来允许继续的编码任务。

## 关键规则示例

### 参考资料怎么使用

规则参考了 *Clean Code* 作者公开的注释文章、Fowler 的重构目录、Google Java 风格指南、Oracle 资源关闭说明，以及 AWS 的超时和重试经验。详细引用放在对应规则中，不要求每次编码重新查阅。*Clean Code* 的出版社目录用于确定主题，不代表已经通读该书，也不把书名当作所有细则的依据。

这些经验用来改善判断，不能套成“方法越短越好”“参数越少越好”“重复就抽方法”或“数字都抽常量”。例如，日期起止值共同表达一个区间时，可以考虑区间对象；几个无关开关不应只为少传参数而包装。循环和 Stream 也按完整流程的可读性选择，不追求更少行数。你已确认的直接展开短包装、集合后缀等偏好继续保留，并遵循项目规则的优先级。

资源先确认归属，再决定谁关闭；超时只说明没有及时收到结果，不能证明第三方没有执行。需要重试时先检查客户端已有尝试、幂等契约和总耗时，不自动添加重试或统一次数。异常转换保留原始原因，关闭或补偿失败也不能把最初的故障覆盖掉。

### 编码期间按复杂度检查

简单改动通常是局部改名、直接赋值、getter、纯转换、孤立分支或测试数据调整，没有外部调用、持久化状态、跨字段约束、异常策略或生命周期变化。这类任务做一次局部上下文预检，完成后回读方法和最终 diff，不逐行停顿，也不加载无关规则。

出现多业务阶段、数据库/缓存/文件/消息/远程调用、事务或异步边界、状态生命周期、重试补偿、日志异常变化，或多个字段共同表达一个契约时，按复杂改动处理。编码前梳理阶段和交接；每完成一个阶段或边界调用，就核对输入来源、结果去向、顺序、失败分类、日志责任和下一步前提。新增日志、异常、远程调用、辅助方法或参数时，先加载对应规则再继续。

如果中途发现需求、数据关系、错误含义或旧逻辑理解有变化，先停在当前阶段，说明证据、影响和选项；会改变行为时向用户确认。简单任务一旦引入这些边界就升级为复杂检查，最终检查不能替代中途检查。

完成各阶段后还要连起来读一遍正常流程。为了最后一条日志而提前声明多个空变量、沿途更新状态，再用大段 `finally` 汇总，可能让真正的业务动作难找；没有实际诊断收益的重复异常包装也应简化。实际承担审计、资源关闭、错误转换或必要上下文补充的结构可以保留，不按变量数、`try` 数或方法行数机械判断。具体标准见 [方法设计](references/method-design.md)。

### 修改前理解相关代码

用户要求修改字段 A 时，不能只搜索字段 A 并改动命中的代码。先确认它从哪里产生、经过哪些转换、参与哪些校验和输出，以及日志、缓存、异常和测试如何使用它。如果字段 B 与 A 共同表达一个业务状态或共同定位一次失败，即使二者没有直接引用，也要明确判断 B 和这层关系是否需要同步变化。

旧日志中的字段不是默认可以删除的装饰。先确认日志服务什么排障场景、各字段如何关联、哪一层负责记录，以及修改后是否仍能定位原问题。当前代码和测试无法解释日志意图，并且不同处理方式会影响诊断能力时，应展示已检查的证据、具体疑点、选项和建议，再等待用户决定；不要笼统询问“这里的业务逻辑是什么”。简单局部改名不需要通读整个模块或查询 Git 历史。

### 跨阶段检查数据和职责

涉及适配、兼容、聚合或职责迁移时，用一个具体输入走到最终结果：调用方到底传了什么、默认值从哪里来、经过哪些过滤和转换、后来是否被覆盖、最终字段是否仍表达同一个结果。不能只看一个 setter 或同名 DTO 字段就概括整条链路。金额与明细、数值与单位、身份与状态等关联信息应一起核对。

“没有返回”要区分省略条目、空列表元素、对象保留但字段为空、空集合和明确失败。多个输入合并成一个内部对象时，也要确认原始身份如何返回；某个结果取首项，不代表其他输入没有执行。比较和汇总前核实单位、币种、时间口径及分组，不能用一条示例日志替代通用保证，也不自行增加换算或兜底规则。

结构合法、当前操作所需、允许缓存或复用、业务成功和事务提交分别按自己的契约判断。通用模型中的可选字段，在特定操作中仍可能必需；只有检查对象、时点、空值和失败后果一致时才共用判断。历史快照与当前配置、转换前对象与实际发送内容也要区分，存储格式变化应同时核对写入、读取和旧数据兼容。

方法通过修改传入 Map 为后续流程提供数据时，检查是否隐藏了输出职责；优先复用已有查询结果，不为移除参数再造一套结构。职责迁移要核对调用次数、批量范围、异常捕获、事务和消费方兼容性。日志阶段尽量由能同时观察开始与结束的位置负责，业务代码避免反向依赖日志模块内部快照。错误提示按需要说明对象、方向和失败阶段，不能把观察到的缺失直接说成未经证实的根因。

这些检查只随相关变更触发，不要求普通字段映射生成长文档。详细判断见 [契约与生命周期](references/contracts-and-lifecycles.md)、[方法设计](references/method-design.md) 和 [异常沟通](references/exception-communication.md)。

### 名称在使用位置是否清楚

只看所属对象、方法名、参数和返回值的使用方式，不打开方法实现或 JavaDoc，也应能理解操作对象、结果和关键副作用：

```text
build(config, request)       -> buildOutboundRequestUrl(config, request)
saveBatch(changes)           -> saveApiConfigChanges(changes)
normalizeCodes(codes)        -> trimAndDeduplicateCodes(codes)
convert(source)              -> convertToApiUpdateBO(source)
```

`Batch`、`List`、`Data`、`Info`、`Context`、`Item` 和 `Result` 只能表达形态，不能替代业务对象。应用内部集合默认在有助于阅读时使用 `List`、`Set`、`Map` 后缀，用户明确要求和正式项目规范优先。名称还应表达必要的对象、状态、来源、键关系和一对一或一对多基数。索引构建必须明确重复键策略。

同样准确时，优先使用常见词。例如实际只从已有数据补齐地址缺失字段，`fillMissingAddressFields` 比 `hydrateAddress` 更直接；实际构造发货请求，使用 `buildShipmentRequest` 即可。不要为了显得专业选择生僻同义词，也不要把名字写成一句实现说明。

这些不是机械替换关系。`reconcileSchemaRevision` 只有实际职责就是修复修订号时，才适合改成 `repairSchemaRevision`；涉及双向比较和冲突处理时不能丢失这些含义。`serialize`、`rollback`、`commit`、项目通用业务词和框架签名可以保留。完成后从调用位置再读一遍，判断是否存在同样准确但更容易理解的说法；仅用词偏难最高按 `P3`，不使用词汇黑名单。

### 规划和编码前判断是否需要调整结构

编码生产逻辑前，先看当前需求是否增加了新的实现方式，或者同一种类型、状态、协议和渠道判断是否已经散落在多个位置。这个步骤只是帮助选择结构，不是要求每次都使用设计模式。

- 一个只在当前方法出现的简单 `if`、单一实现或直接枚举映射，保持直接写法
- 多个位置反复按渠道选择不同处理逻辑时，可以建议把各渠道行为放到独立策略中
- 同一类对象的创建规则散落在多个调用方时，可以建议由一个工厂集中选择和创建
- 状态同时决定可执行行为和合法流转时，可以建议让不同状态负责自己的规则
- 多条流程顺序相同但部分步骤不同，或者多个处理器具有明确的执行和停止规则时，再评估组合流程、模板方法或处理链

只有当前代码已经存在变化点、调整后能减少重复修改位置，并且新增接口和类比原有分支更容易理解时，才向用户提出建议。没有明显收益时不输出结论，直接继续编码。只是沿用项目已有扩展点时也正常继续；需要新建接口、增加一组实现类或重组流程时，先说明简单方案与结构化方案的成本和收益，等待用户选择。用户拒绝后按简单方案实现，不记录质量问题。

普通单元测试、Mock 和测试数据准备不执行这项判断；共享测试工具本身出现相同变化点时才检查。规划可以提前比较选项；用户明确要求结构优化分析时，也可以说明保留现状与调整方案各自的成本。只读比较无需为展示建议等待批准，真正实施重大结构调整前才需要已有授权或用户选择。纯代码审查不执行这项建议步骤，具体缺陷仍按实际影响检查。

### 短私有方法和复用常量

短方法或复用型私有常量即使使用多次，也先尝试把方法里的代码或常量值直接写回主要使用位置，再比较哪种写法更容易读懂。直接写回后能看到空值规则、字段来源、真正调用的对象或完整异常文案，并且当前分支更容易理解时，应采用直接写法；不能只按方法行数决定：

```java
// 使用位置看不到空值规则和实际比较的字段
if (isCatalogReference(field)) {
    validateReference(field);
}

// 类中的另一个位置
private boolean isCatalogReference(Field field) {
    return field != null
            && FieldCatalog.isReference(field.getCode(), field.getPath());
}
```

改为直接写在判断处，读者不需要跳到其他方法：

```java
if (field != null
        && FieldCatalog.isReference(field.getCode(), field.getPath())) {
    validateReference(field);
}
```

仅为了复用用户可见异常文案而抽出的私有字符串常量通常也应展开：

```java
// 常量名隐藏了需要与当前校验和错误码一起核对的真实提示
throw new BusinessException(
        ErrorCode.STATE_CONFLICT,
        FIELD_DEFINITION_MISMATCH_MESSAGE);

// 在失败分支直接展示错误类别、原因和有效恢复动作
throw new BusinessException(
        ErrorCode.STATE_CONFLICT,
        "字段定义已更新，请刷新页面后重新配置");
```

较复杂的算法、事务边界、资源生命周期、副作用顺序、补偿、需要根据上下文区分失败原因的逻辑，以及框架要求的独立方法都可以保留。协议和持久化标识、框架编译期常量、国际化 key、稳定公共标识、结构化模板及错误码枚举本身有固定含义或外部要求，也可以保留。引用次数、JavaDoc、统一文案、长常量名或方法名清晰不能单独作为保留理由。

短方法也可能有保留价值。例如 `isXmlContentType` 把 application/xml、text/xml 和 +xml 后缀的识别归为“XML 类型”，`isJsonContentType` 把 JSON 兼容匹配与 +json 后缀识别归为“JSON 类型”。调用方只需据此选择编码或解析路径，直接展开反而会打断主流程阅读，因此即使只有两行或一个调用点，也可以保留。

差异在于方法是否真正组合了有用的判断规则。判空取字段、给已有同名判断再包一层、固定异常构造，仍优先直接写在使用位置。多个条件或一个好名字本身不能证明抽取合理；不同失败原因也不能被一个布尔方法掩盖。保留的判断方法应说明必要的匹配范围和空值行为，不因本次可读性调整改变原有行为。完整判断标准见 [method-design.md](references/method-design.md)。

### 初始化入口和递归方法

一个方法只准备参数，再调用另一个方法完成同一操作时，要比较完整写法，不能因为分别叫“入口”和“节点处理”就保留两层。合成一个方法后仍然清楚、行为不变，且减少跳转时，优先一个方法；只转发现成参数的入口通常没有保留价值。

递归需要区分整棵树的固定信息与每个节点的变化信息。例如 Body 位置保持不变，但进入子节点后，“是否为 Body 根节点”必须变为否，错误路径也会变化。入口负责一次性初始化这些信息，能让调用方少接触递归细节时，可以保留两个方法，但应说明相比合并具体清楚在哪里。

不能为合并引入“首次调用”判断、特殊空值、无意义参数对象，或把每个 Body 后代都误当作根节点；也不能把初始化散到所有调用方。校验顺序、祖先状态、空值和首个报错必须保持。详细判断由 [方法设计规则](references/method-design.md) 按需加载，不按方法数量机械决定。

### 参数应在调用处看得懂

`validateNode(node, false, true, false)` 需要靠位置猜三个开关的含义，应检查是否能删除恒定参数、使用对象真正拥有的属性，或用轻量枚举表达固定调用位置。对象属性、调用位置和祖先递归状态是不同信息，不能为了少传参数混在一起。

`validateNode(node, NodeLocation.REQUEST_BODY, outboundRequest)` 能直接表达固定区域和真实动态条件。枚举不必同时负责选取节点或自动遍历；原本清晰的几个入口可以继续显式调用。单个明确开关、动态布尔状态和框架签名可以保留，不按布尔数量机械改写。调整遍历时还要验证校验顺序、父子状态、空值和报错行为。

### 默认少用嵌套类型

仅为装几个开关创建内部参数类，通常会增加跳转。先考虑局部变量和已有类型；有独立职责时使用独立文件，并保持最小必要可见性，不自动改成 `public`。

如果静态嵌套类型与外部类共同封装非平凡算法，放在一起更易理解，或确有 Builder、框架要求，可以保留；不需要外部实例时优先使用静态形式。该偏好同样覆盖局部类和嵌套枚举，只检查本次新增或修改的类型，不整改无关历史代码。单纯偏好问题最高为 `P3`，实际生命周期或行为风险按影响判断。

### JavaDoc 与阶段注释

写注释前，先根据已确认的需求、当前实现、调用方和测试确认当前规则，再看当前文件中同类方法或代码块的注释，参考其布局、详略、业务用语和必要标签。已有方法普遍用多行 JavaDoc 时，新方法也优先保持这种形式；简单方法的一行注释已经清楚时，可以沿用。没有可参考内容，再看同包的相似代码，不扫描整个项目。

这些写法是参考，用户要求和正式仓库规范优先。遇到混合风格，选择清楚且适合当前职责的写法；不照搬含糊的“清旧、设新”、过时说明或无关标签。完成后把新注释放回文件中检查是否协调，不为了统一格式改动无关旧注释。

行为变化时，把受影响的整条注释重新组织为完整的当前规则，不默认保留旧句再追加例外。例如当前规则是优先使用订单指定的发件地址、缺失时使用仓库地址，就直接写明这个优先级，不写成“使用仓库地址，特殊情况支持订单地址”。同步检查方法 JavaDoc、所在阶段和分支的说明，即使它们不在最初的修改行中。

重写后对照旧注释，保留仍有效的空值、兼容、顺序和失败保证；准确且未受影响的注释可以保留。最终让没有看过旧代码和讨论过程的人也能读懂当前规则。实现与已确认需求冲突时先处理差异，不能只改注释把意外行为合理化。详细维护步骤见 [注释规则](references/comments-and-javadoc.md#comment-maintenance)。

方法名说明“做什么”，JavaDoc 说明调用前提、返回结果、异常和副作用等方法名看不出的规则。即使方法逻辑是线性的、方法是私有的或名称已经清晰，只要它负责一个独立业务动作、处理阶段、生命周期时点或副作用，就需要 JavaDoc。

方法 JavaDoc、写在处理阶段开头的注释和分支内注释不能互相替代。准备或转换、远程执行、持久化和响应构造要分别检查；名称和类型无法表达的结果去向、顺序或失败规则，应在对应位置说明。不要求给显然的赋值、getter 或契约已经清楚的调用机械添加正文注释。

检查注释时同时看两点：它补充了什么信息，以及读者能否一遍读懂。使用具体对象和动作，少写“处理该阶段”“消费结果”等缺少具体含义的句子；必要的领域术语可以保留。原因、顺序和失败保证必须有代码或契约依据，不为了显得有深度编造解释。

删掉正文注释后没有丢失信息，可以删除这条重复说明；必需的 JavaDoc、入口校验说明、行为变化的 catch 和关键阶段说明应改写得更具体。一个注释可以说明执行同一规则的一组语句，准备、远程调用和保存等不同阶段仍要按各自的隐藏规则检查。

主状态写入后如果紧接着多行拼装前后值、来源等诊断日志，在写入与日志块之间说明日志记录的是什么，避免真正的状态变化被日志准备遮住；简单写入后直接跟一条一眼能看懂的日志，不强制加注释。日志契约要求先记录时，保留真实顺序并说明原因。

```java
Object previousFromAddress = orderParams.get("from_address");
orderParams.put("from_address", shipFromParams);

// 记录本次下单参数采用的发件地址及覆盖前后值，便于排查地址选择结果
Map<String, Object> shipFromOverrideLog = new LinkedHashMap<>();
shipFromOverrideLog.put("before", previousFromAddress);
shipFromOverrideLog.put("after", shipFromParams);
Loggers.BIZ.info(JSONUtil.toJsonStr(shipFromOverrideLog), "carrier.order.ship_from.override");
```

注释只描述已发生的参数覆盖和日志用途，不暗示订单已持久化或请求已发送。

例如，假设代码确实在全部明细通过校验后才保存：

```java
// 空泛：完成校验后执行后续持久化逻辑
// 具体：全部明细校验通过后再保存，任一明细无效时不写入订单
```

一句先说明一个重点，复杂条件可以分行解释，不机械套用“为了……先……避免……”句式。详细判断、JavaDoc 写法和参考资料见 [注释规则](references/comments-and-javadoc.md)。

### 注释说明当前规则

行内注释应让没有参与本次修改的人直接理解当前有效行为，不要围绕已经放弃的实现或旧字段组织句子。例如：

```java
// 不推荐：读者不知道 legacyFormat 为什么会被特意排除
// 只有解析后的 Content-Type 决定编码，legacyFormat 不参与运行时选择

// 当前规则已经完整时，直接正向说明
// 根据解析后的 Content-Type 选择请求编码方式
```

如果旧字段仍然存在并承担真实的兼容职责，则保留它，但要说明现在用来做什么：

```java
// 根据解析后的 Content-Type 选择请求编码方式，legacyFormat 仅用于读取历史配置
```

这不是禁止否定句。失败后跳过缓存、禁止发布、明确不支持某种输入等信息，只要属于当前契约并会影响调用方或后续修改，就必须保留。纯粹记录“以前怎么实现、这次为什么没采用另一方案”的内容应放在 Git 历史、迁移说明或决策记录中。

### 异常原因与恢复动作

同一提示必须对所有到达路径的失败条件都真实。不同原因具有不同错误类别或恢复动作时，不能只润色一个合并提示：

```java
// 两类失败被压成一句无法执行的提示
if (!Objects.equals(request.getDefinitionVersion(), currentDefinitionVersion)
        || field.isGroup() && field.hasValueRule()) {
    throw new BusinessException(
            ErrorCode.INVALID_ARGUMENT,
            "字段配置不正确，请刷新后重试");
}
```

应保留可以区分的失败原因：

```java
if (!Objects.equals(request.getDefinitionVersion(), currentDefinitionVersion)) {
    throw new BusinessException(
            ErrorCode.STATE_CONFLICT,
            "字段定义已更新，请刷新页面后重新配置");
}

if (field.isGroup() && field.hasValueRule()) {
    throw new BusinessException(
            ErrorCode.INVALID_ARGUMENT,
            "字段分组不可配置取值规则，请删除该规则后重新保存");
}
```

只有当刷新、重试、重新保存或重新配置确实能解决当前原因时，才能给出对应建议。无法区分原因时使用真实的组合描述，不提供只适用于部分路径的动作，并在内部保留可诊断信息。用户提示优先使用业务名称；技术标识只在目标受众能据此定位时作为辅助锚点。

### 异常文案要让人知道哪里不符合要求

先使用界面或 API 文档中的实际名称，说清“哪项配置、在哪个位置、需要满足什么条件、可以执行什么操作”，不要把多个限定词挤在一起。括号可以帮助识别配置项，但不是强制格式。改写后要逐项对照触发条件，不能为了通顺漏掉启用状态、字段名、类型或位置等关键限制。

例如某个选项只允许用于请求正文中已启用且有字段名的对象字段，“仅请求正文中的对象字段支持文本传输”就漏掉了两个条件。完整范围可以写成“仅支持将请求正文中已启用且有字段名的对象字段配置为文本传输”；能确定实际原因时，“当前字段未启用，启用后才能配置文本传输”更直接。

说明允许范围不等于指出当前错误。不同原因需要不同处理动作时，按前面的原因拆分规则处理；只改文案不能擅自改变校验顺序、错误码或首个报错。不要把全部内部判断和敏感信息塞进用户提示。详细写法及条件核对见 [异常沟通规则](references/exception-communication.md)。

### 关键业务变化和输入输出日志

编码前及每个关键阶段完成时，判断现有记录能否解释“使用了什么输入、依据什么规则、发生了什么变化、最终得到什么结果”。普通业务处理也适用：参数覆盖记录相关前后值和来源，计算或映射记录决定结果的输入与实际输出，自动修复记录原状态和原因，校验失败说明实际值与预期条件。只为具体排障缺口补充日志，不给每次赋值和每个循环元素机械打印。

例如替换发件地址时，先保存需要比较的原值，再完成替换并记录变化。对象原地修改时，保存同一个对象引用不能代表“修改前”；异步日志也要避免后续修改污染快照。一条日志可以同时记录前后值，也可以用现有标识关联同一次操作的多条日志。内存赋值、请求发送、数据库调用返回和事务提交要分清，不能提前宣告整体成功。

沿用仓库日志入口和已确认的字段范围、级别及报文政策，统一设施已有完整记录时不重复打印。范围不明确时说明具体字段与风险再询问，不默认全量记录或强制脱敏，也不只为拼装日志增加大段控制结构。验证时检查快照、关联关系和失败路径；日志用于观察和排障，输入输出是否正确仍由校验和测试保证。详细规则见 [上下文与验证](references/evidence-and-verification.md#trace-important-business-changes-and-results)。

### 第三方调用日志和错误

接入第三方接口前，先查看仓库是否已有客户端拦截器、统一 Wrapper、日志切面、脱敏工具和错误映射。不能只因为控制台能看到 HTTP DEBUG 日志，就认为生产环境已经具有安全且完整的调用日志。

下面的处理同时丢失了第三方正常业务响应中的具体原因：

```java
if (response.isError()) {
    Loggers.BIZ.warn("carrier.order,errorCategory:{}", "BUSINESS_REJECTED");
    throw new BusinessException("承运商下单失败");
}
```

第三方业务错误至少要在调用方错误或内部诊断中的一处保留错误码、错误信息、请求 ID 等可定位内容。是否返回原始第三方文案，或者映射为本地错误，只能根据仓库已有 Wrapper 或映射表、本地接口契约、第三方明确错误码语义、调用方测试或用户确认来决定，不能根据文案相似度临时猜测。

完整 URL、请求响应体、文件和鉴权信息也不做统一禁止或统一要求。先检查仓库日志规范、脱敏和访问控制、运行环境、报文大小以及实际排障收益；规则不明确时，说明具体字段和风险，给出关键字段、脱敏完整报文、原始完整报文或仅失败记录等方案，等待用户选择。应优先建议不记录凭据和可重放信息原值，但不能把建议冒充成仓库规则。

业务拒绝、HTTP 非成功、响应无法解析和网络异常需要分别处理。技术异常包装时保留 `cause`，或由唯一负责诊断的层记录一次完整异常，避免每层都记录后再抛出。

验收时按实际失败场景追踪：鉴权失败尚未发请求、成功返回、第三方拒绝、响应无法解析、网络中断，分别留下什么证据，能否关联同一次调用。只有账号、状态和耗时的摘要不一定足够；如果统一日志已有可关联的请求和响应记录，则无需重复打印。总耗时和 HTTP 耗时要分清，报文仍按已确认的范围记录。日志捕获测试、代表性链路或只读检查各自证明什么，应在结果中说清楚。

### 证据与最终状态

代码附近的常见写法不一定是项目规范，测试通过也不一定代表公开契约正确。做出会影响接口兼容、数据、安全、日志披露、事务或架构的判断时，应区分：

- 用户和仓库明确规定的约束
- 当前源码、测试、配置和调用链体现的实际行为
- 对应版本的第三方正式文档
- 附近代码形成但未声明的惯例
- Skill 自身提供的默认建议

这些来源冲突时，先说明冲突和影响，不能自行挑选最方便的一项。普通局部可读性问题可以按 Skill 默认处理；会产生不同外部结果且没有足够依据时，再向用户说明选项并等待选择。

新增超时配置、账号选择或本地校验前，先确认当前层为什么需要它、已有机制是否能满足需求。附近接口的取值或做法需要核对适用条件；“配置应放在哪里”和“是否需要新增配置”是两个判断。

排障时区分“代码存在缺陷”“可能经过该路径”和“本次故障已证实由它导致”。耗时接近、相邻成功日志或缺失一条分支日志都不能单独证明根因。测试也要说明边界：Mock 了鉴权入口的接口测试，能证明返回值和异常处理，却不能证明真实缓存刷新或锁竞争正确；没有检查日志的测试，也不能证明排障记录完整。

所有验证都以最终磁盘状态为准。formatter、代码生成、测试自动修复、IDE、Git hook 或其他工具运行后，需要重新读取 `git status`、最终 diff、受影响文件和新增文件，并重新运行被改动影响的检查。不能用工具执行前的 diff 或旧测试结果证明最终代码已经通过。

### 三元表达式、控制流与换行

三元表达式只保留简单的纯值选择，例如：

```java
String statusText = enabled ? "启用" : "停用";
```

如果一行同时包含赋值、比较、空值判断和方法调用，拆成带大括号的 `if` 更容易看懂：

```java
String userName = null;
if (user != null) {
    userName = user.getName();
}
```

同一个条件先用来校验，隔一段代码又用来执行时，先比较能否把这条路径的校验、取值和执行集中在一个分支，减少来回对应。例如拆分后的两部分分别是“前缀”和“本地名称”，可以在两部分分支内完成名称校验、前缀解析和结果创建。只把两个判断都改成 `hasPrefix` 并没有解决流程分散的问题。

统一校验全部输入后再执行、必要的共享预校验，或中间状态已经变化时，可以保留重复判断。整理流程不得改变错误先后、空值、调用次数或副作用顺序；另一种合理写法本身不构成质量问题。

`parts.length == 2` 中的 `2` 不必机械抽成常量。用 `prefix`、`localName` 等局部名称和必要注释说明结构；协议标识、独立限制或跨职责共享的约定仍可以使用常量。检查器不自动判断重复条件是否应该合并、数字含义是否清楚。最后回读代码时仍要检查这些内容和复杂三元表达式，不能只凭自动检查通过就结束。

所有 `if`、`else`、`for`、`while` 和 `do while` 都使用大括号，即使分支只有一条语句。三元表达式是否影响业务理解由 Skill 结合语义判断，检查器只自动检查缺少大括号。

增强 `for` 的数据来源是数据库查询、远程调用或非平凡的数据准备时，默认先取得结果，再遍历：

```java
List<ApiSchemaDocument> activeSchemaList =
        apiSchemaRepository.queryActiveByApiCodes(apiCodeCollection);

for (ApiSchemaDocument schema : activeSchemaList) {
    // 原有处理逻辑
}
```

这让查询结果可以单独阅读和调试；增强 `for` 中的查询本来就只执行一次，不是每轮查询。已有集合和简单的内存 getter（如 `order.getItems()`）可以直接遍历，不为拆行新增包装方法或机械注释。保留原来的执行位置、空值和异常行为；游标、Stream 和惰性结果不能强行转成 List，也不能移出原有关闭范围。`while` 中每轮取下一页等调用仍按原频次执行。该项是默认可读性偏好，单纯违反最高为 `P3`，由 Skill 语义检查，不增加 Python 规则。

换行先遵循项目 formatter 或明确的最大行宽。没有项目约定时，能在当前 IDE 常见视口内完整展示且结构清楚的短调用保持一行；超过行宽、参数边界不清或一行包含多个独立动作时再换行。不要因为变量名或方法名较长就机械拆开，也不要为了避免换行而保留难以扫描的长表达式。

## 安装

克隆仓库并进入根目录：

```bash
git clone git@github.com:Rayctl/Java-Dev-Skills.git
cd Java-Dev-Skills
```

Windows PowerShell：

```powershell
Copy-Item -Recurse -Force ".\java-code-design-and-development" "$env:USERPROFILE\.codex\skills"
```

Git Bash：

```bash
cp -R ./java-code-design-and-development "$HOME/.codex/skills/"
```

复制后可用只读脚本比较仓库副本和安装副本的文件清单及 SHA-256：

```powershell
py -3 ".\java-code-design-and-development\scripts\verify_skill_installation.py" `
  --source ".\java-code-design-and-development" `
  --target "$env:USERPROFILE\.codex\skills\java-code-design-and-development"
```

退出码 `0` 表示完全一致，`1` 表示存在缺失、多余或内容不同的文件，`2` 表示输入或环境错误。目录读取失败时返回错误，不把未能枚举的文件当作不存在并误报一致。脚本忽略 `__pycache__` 和 `.pyc` 等运行缓存，不复制、覆盖或删除任何文件。

安装后的入口为：

```text
~/.codex/skills/java-code-design-and-development/SKILL.md
```

更新已有安装时，用当前目录替换此前安装的同一 Skill，并将用户级 `AGENTS.md` 的路径和调用名称同步为本文示例，避免旧目录与新目录并存、重复加载。现有质量规则、检查器脚本、CLI 参数、规则编号和退出码保持不变。

## 调用方式

`agents/openai.yaml` 已允许隐式触发。为了在具体 Java 代码的规划、分析、实现和审查中稳定加载，可以在用户级 `~/.codex/AGENTS.md` 中加入：

```markdown
## Java 代码设计与开发

Before planning, analyzing, implementing, or reviewing specific Java backend code or a proposed implementation, explicitly read and follow `$java-code-design-and-development` once for the task. Include explicitly requested existing code even without a diff; keep implementation and diff review scoped to task-owned changes. Planning, analysis, and review are read-only unless edits are authorized. Load references for the concerns under assessment, not the entire repository. After Java edits, reread changed methods and the final diff, run the deterministic checker, and perform appropriate verification. Without edits, use focused checks only when relevant and distinguish proposed verification from executed results. Generic Java questions do not trigger this workflow. Explicit project and user instructions take precedence.
```

也可以显式调用：

```text
Use $java-code-design-and-development to plan, analyze, implement, or review the Java backend code currently in scope
```

## 目录结构

```text
java-code-design-and-development/
|-- README.md
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- evals/
|   |-- README.md
|   |-- forward-evaluation-template.md
|   `-- semantic-cases.json
|-- references/
|   |-- checker.md
|   |-- comments-and-javadoc.md
|   |-- contracts-and-lifecycles.md
|   |-- control-flow.md
|   |-- evidence-and-verification.md
|   |-- exception-communication.md
|   |-- method-design.md
|   |-- naming.md
|   |-- project-guidance.md
|   |-- remote-calls.md
|   |-- structure-choice.md
|   `-- task-modes.md
|-- scripts/
|   |-- check_java_backend_style.py
|   |-- validate_semantic_evals.py
|   |-- validate_project_guidance.py
|   `-- verify_skill_installation.py
`-- tests/
    |-- test_check_java_backend_style.py
    |-- test_project_guidance.py
    `-- test_skill_quality_assets.py
```

README 面向安装和快速理解，引用文件保存完整规则，Python 脚本负责可确定的自动检查，`evals/` 保存需要结合语义判断的代表性场景和独立评测模板。

## 样式检查器

检查当前工作区相对 `HEAD` 的暂存、未暂存和未跟踪 Java 变更：

```powershell
py -3 "$env:USERPROFILE\.codex\skills\java-code-design-and-development\scripts\check_java_backend_style.py" --changed --repo "C:\path\to\repo"
```

常用范围参数：

```powershell
py -3 "$env:USERPROFILE\.codex\skills\java-code-design-and-development\scripts\check_java_backend_style.py" --changed --base origin/main --repo "C:\path\to\repo"
py -3 "$env:USERPROFILE\.codex\skills\java-code-design-and-development\scripts\check_java_backend_style.py" --line-range "C:\path\to\Example.java:20-80"
py -3 "$env:USERPROFILE\.codex\skills\java-code-design-and-development\scripts\check_java_backend_style.py" "C:\path\to\Example.java"
```

检查器保持只读，退出码为 `0` 表示通过、`1` 表示发现违规、`2` 表示参数、输入或环境错误。规则编号包括：

- `STYLE-COMMENT-001`：注释以中文或英文句号结尾
- `STYLE-METHOD-001`：相邻方法声明之间不是一行空行
- `STYLE-CATCH-001`：改变行为的 `catch` 缺少说明后续处理的注释
- `STYLE-GUARD-001`：至少三个用于提前退出的入口判断前，没有说明整组校验目的的注释
- `STYLE-INTENT-001`：明显复杂的方法中，主要处理阶段前完全没有意图注释
- `STYLE-BRACE-001`：`if`、`else`、`for`、`while` 或 `do while` 的执行体缺少大括号

检查器不会判断自然语言是否清楚、语义邻域是否检查完整、关联字段是否应同步变化、旧日志为何记录某些内容、处理阶段是否说明完整、三元表达式是否应该改写、私有方法或复用型异常文案常量是否应该写回使用位置、当前变化是否值得采用设计模式、错误原因是否应拆分、恢复动作是否有效、错误码是否匹配或是否泄露敏感信息。第三方调用的日志覆盖、完整报文策略、失败分类、错误映射依据和诊断信息保留也由 Skill 结合代码含义检查。

方法名的用词是否通俗且准确、业务日志是否保留正确时点的前后值、输入输出及同次操作关联信息，也由语义审查判断；不新增按单词或日志数量判错的规则。

## 语义评测

[`evals/semantic-cases.json`](evals/semantic-cases.json) 覆盖短私有方法、阶段注释、注释文案与删除测试、历史兼容、命名、参数与快照、控制流、Map 重复策略、第三方错误、资源关闭和重试、JavaDoc、结构选择、关联字段、证据冲突、编码循环及工具改写后的最终回读。每个场景记录必须出现和不能出现的决策，不比较固定文案。

校验场景文件结构：

```powershell
py -3 ".\java-code-design-and-development\scripts\validate_semantic_evals.py" `
  ".\java-code-design-and-development\evals\semantic-cases.json"
py -3 ".\java-code-design-and-development\scripts\validate_project_guidance.py" `
  ".\.codex\project-guidance.md"
```

该命令只证明评测数据结构有效。要验证 Agent 行为，需要在没有继承原讨论结论的新会话或独立评测环境中运行场景，并按含义检查决策。使用 [独立评测模板](evals/forward-evaluation-template.md) 记录有 Skill、无 Skill或旧版本的输出、断言证据、Token、耗时和实际加载的引用文件。重点覆盖语义邻域、分章节提示基线、日志和工具复用、异常原因拆分、短辅助方法、简单任务的按需加载及编码前结构建议。

## 验证

```powershell
py -3 -m unittest discover -s "$env:USERPROFILE\.codex\skills\java-code-design-and-development\tests" -p "test_*.py" -v
py -3 "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "$env:USERPROFILE\.codex\skills\java-code-design-and-development"
py -3 "$env:USERPROFILE\.codex\skills\java-code-design-and-development\scripts\validate_semantic_evals.py"
```

在未授予 Windows 符号链接权限的环境中，越界符号链接用例会跳过。
