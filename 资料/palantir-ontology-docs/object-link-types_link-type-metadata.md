# 元数据参考

> 来源: https://www.palantir.com/docs/zh/foundry/object-link-types/link-type-metadata/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 元数据参考

一个链接类型在 Foundry Ontology 中由以下元数据表示：

- ID：链接类型的唯一标识符，主要用于在配置应用时引用此类型的链接。例如，employee-employer可能是定义在Employee和CompanyObject 类型之间的链接类型的 ID。
- RID：Foundry 中每个资源自动生成的唯一标识符。链接类型的 RID 将在平台上的出错信息中被引用。
- 状态：向用户和其他 Ontology 构建者指示链接类型处于开发过程中的哪个阶段。它可以是active、experimental或deprecated。默认情况下，Employee → Employer链接类型的状态为experimental。阅读更多关于状态的信息。
- Object 类型：通过链接类型定义相关的 Object 类型。例如，Employee → Employer链接类型将引用Employee和CompanyObject 类型。
- 基数：指示应用程序每个链接类型中的 Object 类型是一个还是多个对象。例如，在链接类型Employee → Employer中，Employee Object 类型的基数为many，而 Company Object 类型的基数为one，因为许多员工链接到一个雇主。如果直接报告可以有多个经理，而经理可以有多个直接报告，那么在链接类型Direct Report ↔ Manager中，每个 Employee Object 类型的基数将为many。
- 键：用于创建链接的属性或列。在一对一或一对多基数的链接类型中，一个 Object 类型的属性（外键）引用另一个 Object 类型的主键属性。外键和主键之间的引用定义了对象之间的链接。例如，在Employee → Employer链接类型中，EmployeeObject 类型可能有一个employer ID属性（外键），它引用CompanyObject 类型的company ID属性（主键）。在多对多基数的链接类型中，包含主键对的表定义了两个对象之间的链接。这些链接类型需要指定一个合并表，并映射这些键以告诉应用程序合并表中的哪些列引用链接类型中哪些 Object 类型的主键。例如，支持Direct Report ↔ Manager链接类型的合并表可能包含employee numbers对，每对代表一个Direct Report ↔ Manager链接。
- 显示名称：在用户应用程序中访问此类型链接的任何人显示的名称。链接类型的每一侧都有一个显示名称。链接类型的一侧代表链接到该 Object 类型。例如，在Employee → Employer链接类型中，EmployeeObject 类型的显示名称为Employee，而CompanyObject 类型的显示名称为Employer。
- 复数显示名称：在用户应用程序中访问此类型链接的多个链接 Object 类型的任何人显示的名称。例如，在Employee → Employer链接类型中，EmployeeObject 类型的复数显示名称为Employees，而CompanyObject 类型没有复数显示名称，因为每个员工只能有一个公司。
- API 名称：在代码中以编程方式引用链接类型时使用的名称。链接类型一侧的 API 名称可用于返回该类型的对象。例如，如果Employee → Employer链接类型的 Employee 侧的 API 名称是employee，那么调用Company.employee.get()将返回链接到这些Company对象的Employee对象。阅读更多关于API 名称的信息。
- 可见性：向用户应用程序指示链接类型一侧的显示重要程度（指链接到该侧 Object 类型的链接）。prominent的链接类型一侧将导致应用程序首先向用户显示该侧的链接类型。hidden的链接类型一侧将不会出现在用户应用程序中。默认情况下，链接类型的 Employee 和 Company 侧的可见性为normal。
- 类型类：用户应用程序解释的附加元数据。阅读更多关于类型类的信息。

了解更多关于在 Ontology 中创建和配置链接类型以及链接类型元数据的验证要求的信息。

了解更多关于属性（Object 类型的特征）的信息。