# API: Ontology编辑

> 来源: https://www.palantir.com/docs/zh/foundry/functions/api-ontology-edits/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# API: Ontology编辑

除了编写基于Ontology返回衍生值的函数外，您还可以编写函数以编辑Ontology中对象的属性和链接。本页面记录了可用于函数的对象编辑API。有关编辑函数如何工作的详细信息，请参阅概述页面。

为了在操作环境中实际使用，Ontology编辑函数必须配置为操作，称为函数支持的操作。以这种方式配置操作可以让您提供额外的元数据、配置权限，并在各种操作界面中访问操作。如文档中所述，在操作之外运行编辑函数实际上不会修改任何对象数据。

警告

在编辑对象后搜索它们可能会返回意外结果。详情请参阅注意事项部分。

## 声明编辑函数

编辑Ontology的函数必须：

- 使用从@foundry/functions-api导入的@OntologyEditFunction()装饰器进行装饰
- 使用从@foundry/functions-api导入的@Edits([object type])装饰器进行装饰，以指定将要编辑的对象类型
- 明确具有void返回类型

## 更新属性

您可以通过简单地重新指派对象的属性值来编辑属性值。例如：

```
1

```

如果在同一函数执行过程中访问lastName属性值，将返回您刚刚设置的新值。

对象上的数组属性是使用ReadOnlyArray类型生成的。要修改数组，请创建它的副本，修改该副本，然后更新属性：

```
1
2
3
4
5
6

```

请注意，您无法更新现有Object的主键属性值。

## 更新链接

SingleLink和MultiLink接口有多种方法可用于更新链接：

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

正如更新属性一样，在更新后访问链接将反映出您所做的更新。

## 创建对象

您可以使用@foundry/ontology-api中提供的Objects.create()接口创建新对象。在创建新对象时，您必须为其主键指定一个值。

在此示例中，我们创建一个新的 Ticket 对象，指定其 ID，设置其dueDate属性，并通过修改assignedTickets链接指派给指定的 Employee。

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

```

## 删除Objects

您可以通过调用.delete()方法删除一个Object。

在这个例子中，我们删除指派给指定员工的所有工单。

```
1
2

```