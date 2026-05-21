# 输入和输出类型

> 来源: https://www.palantir.com/docs/zh/foundry/functions/input-output-types/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 输入和输出类型

本参考提供了在TypeScript ↗函数中的输入和输出类型的详细文档。

为了发布到注册表，TypeScript 函数必须对所有输入参数具有显式类型注解，并指定显式返回类型。

请注意，从 TypeScript 函数中调用外部 API 是不可用的。要作为操作的一部分调用外部 API，请使用webhooks。

目前，这些是函数中支持的所有输入和输出类型：

### 标量类型

- boolean
- string
- Integer、Long、Float和Double请注意，在 JavaScript 和 TypeScript 中，只有一种number类型。然而，为了提供进一步的类型验证和结构，我们仅支持从@foundry/functions-api导出的上述别名。导入这些类型以在您的函数定义中将它们用作输入和输出。
- LocalDate和Timestamp类型用于时间信息。与数字类型一样，JavaScript 本机支持Date类型。然而，为了区分日期和时间戳，我们提供从@foundry/functions-api导出的更具体的类型。LocalDate表示日历日期，而Timestamp表示瞬间时间。

### 非必填类型

对于输入参数，非必填参数声明为varName?: <type>。例如，一个具有非必填整数参数名为value的函数将有一个参数value?: Integer。

函数可以通过指定类型为<type> | undefined来声明一个非必填返回类型。例如，一个可能返回Integer或没有值的函数将有一个返回类型Integer | undefined。

### 集合

- 列表支持使用ES6 数组 ↗（例如，string[]是字符串值的列表）请注意，支持嵌套列表（例如，Integer[][]是整数值列表的列表）
- 集合支持使用ES6 集合 ↗（例如，Set<string>是字符串值的集合）
- 映射支持使用@foundry/functions-api包中的FunctionsMap。可以使用FunctionsMap<K, V>表示法声明，其中K是键类型，V是值类型。键可以是标量类型或Ontology对象（例如，FunctionsMap<Employee, string>）。值可以是任何支持的类型。

### 聚合

聚合是从Ontology对象上的分桶聚合中检索时返回的类型，它们可以从函数返回以用于平台的其他部分，如在Workshop中的图表中。

支持两种聚合类型：

- TwoDimensionalAggregation从单个桶键映射到一个数值，该数值表示为Double。例如，TwoDimensionalAggregation<string>从string桶键映射到每个桶的数值。这可以用来表示一个聚合，例如具有特定任务标题的员工计数。
- ThreeDimensionalAggregation从两个桶键映射到一个数值。例如，ThreeDimensionalAggregation<string, string>从string桶键映射到嵌套桶的数组。这些嵌套桶每个都有一个映射到数值的string键。这可以用来表示一个聚合，例如按每个员工的任务标题和家庭办公室统计员工数。

两种聚合类型都可以从函数返回，并可以在平台的其他部分使用，特别是在 Workshop 图表中。

聚合可以通过几种类型进行键控：

- boolean桶表示值是true还是false
- string桶可用于表示分类值
- IRange（来自@foundry/functions-api）桶表示桶键是值范围的聚合。这些可用于在图表中表示直方图或日期轴。数字范围，包括Integer和Double，表示数值上的分桶聚合日期和时间范围，包括在LocalDate和Timestamp上，表示日期范围上的分桶聚合

### Ontology类型：Objects 和对象集

Ontology 导入

在生成接口之前，必须将对象类型导入到您的存储库中。了解更多关于Ontology导入的信息。

配置在您的Ontology中的每个对象类型都将转换为 TypeScript 接口，以用于函数代码中。所有生成的类型都从@foundry/ontology-api包导出。请参阅 TypeScriptOntology API的详细文档以获取更多信息。

- 当 Object 类型用作输入类型时，执行函数的客户端必须传递objectRid或对象类型和客户端希望对其执行函数的对象的主键
- 当 Object 类型用作输出类型时，将返回对象的定位器（对象类型和对象的主键）

有两种方法可以将对象集合传入和传出函数：具体的对象集合，如数组和集合，或对象集。

- 向函数传递对象数组或集合可以在具体的对象列表上执行逻辑。例如，您的函数可以接收employees: Employee[]或employees: Set<Employee>以接收员工对象的数组或集合。对于对象数组参数，客户端必须传递应加载的对象的objectRids或对象定位器列表
- 从@foundry/ontology-api导出的ObjectSet<>接口允许将对象集传递给函数。例如，您的函数可以接收employees: ObjectSet<Employee>以接收员工的对象集。对象集支持筛选、搜索和聚合操作。了解更多关于对象集 API 的信息。对于对象集参数，客户端必须传递指向已保存对象集的objectSetRid。对象集服务允许对象集在一段时间内保存，以便创建短期对象集用作函数参数

提示

使用ObjectSet<>接口通常比数组更可取，因为它能够实现更好的性能，并允许超过 10,000 个对象传递给函数。

### 主体、用户和组

主体表示 Foundry 用户账户或组。这些类型可以传递给函数，以允许访问与用户或组相关的信息，例如组名或用户的名字、姓氏或电子邮件地址。所有主体类型都从@foundry/functions-api包导出。

- User始终具有用户名，并且可能具有firstName、lastName或email。它还包括与主体相关的所有字段。
- Group具有名称。它还包括与主体相关的所有字段。
- Principal可以是User或Group。您可以检查type字段以确定给定的主体是User还是Group。除了User和Group特定的字段之外，主体还有一个id、realm和attributes字典。

#### 搜索 Foundry 用户

除了将User、Group或Principal作为参数传递给函数之外，您还可以使用从@foundry/functions-api导出的Users对象按需检索用户或组。

- getUserByIdAsync方法接收一个 userId 作为string并返回一个Promise<User>
- getGroupByIdAsync方法接收一个 groupId 作为string并返回一个Promise<Group>

### 通知

通知类型可以从函数返回，以便灵活配置应该在平台中发送的通知。例如，您可以编写一个函数，该函数接收参数，如User和对象类型，并返回具有已配置消息的通知。

- Notification由两个字段组成：ShortNotification和EmailNotificationContent。
- ShortNotification表示通知的摘要版本，它将在 Foundry 平台中显示。它包括一个简短的heading、content和一组Link。
- EmailNotificationContent表示可以通过电子邮件外部发送的通知的丰富版本。它包括一个subject、一个由无头 HTML 组成的body，以及一组Link。
- Link具有用户可见的label和一个linkTarget。LinkTarget可以是 URL、OntologyObject，或 Foundry 中任何资源的rid。

有关如何使用通知 API 的示例，请参阅操作指南。

### 自定义类型

您还可以为函数定义自定义输入和输出类型。自定义类型定义为 TypeScript 接口，也可以定义为行内匿名类型。

- 自定义类型的字段可以是上述任何其他类型、另一个自定义类型或自引用。
- 通过?非必填词元支持非必填字段，或者字段的类型与undefined的联合。

自定义类型示例：

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24

```

在代码中，EmployeeGraph接口用于表示员工之间的关系图，EmployeeFilter接口用于过滤员工。myEmployeeSearchAround函数用于基于特定条件搜索员工关系，而getAverageAndMedianAge函数用于计算一组员工的平均年龄和中位数年龄。

### 其他类型

- ES6 Promises ↗可以从一个函数返回，以支持函数异步加载数据的工作流。在运行时，函数执行器会等待 Promise 被解析后再向客户端返回值。注意，Promise 类型在发布到函数注册表时会被忽略，因此一个返回Promise<Integer>的函数在函数注册表中将显示为仅返回一个Integer。

## 参数选项

除了声明函数参数的数据类型外，还有一些关于如何处理参数的其他选项。

### 非必填参数和默认值

TypeScript 函数支持非必填参数和具有默认值的参数。如果一个函数参数是非必填的，它将在函数注册表中以此形式发布，允许客户端在不传入该参数的情况下执行函数。这对于提供简单的默认值的函数很有用，这些默认值可以为特定应用案例覆盖。

以下是一个具有非必填参数的函数示例：

```
1
2
3
4
5
6
7
8
9
10

```

这是一个具有默认值的函数示例：

```
1
2
3
4
5
6
7

```

weight的值将默认为0.75，除非客户端传递了特定的值。

### 文档

如果一个函数定义包含符合JSDoc ↗规范的文档，则这些文档将被发现并发布到函数注册表中。这使得用户可以根据描述搜索函数，并且可以用于提供关于每个输入参数对函数的意义的更多详细信息。

以下是一个包含文档的函数示例，这些文档会发布到注册表中：

```
1
2
3
4
5
6
7
8
9
10
11

```