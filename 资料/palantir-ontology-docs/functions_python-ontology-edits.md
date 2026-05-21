# Ontology 更改

> 来源: https://www.palantir.com/docs/zh/foundry/functions/python-ontology-edits/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# Ontology 更改

除了编写从 Ontology 读取数据的函数外，您还可以编写创建对象并编辑对象之间属性和链接的函数。 本页记录了函数中可用的对象编辑 API。 有关编辑函数如何工作的更多详细信息，请参阅概述页面。

为了使函数中创建的更改实际应用，Ontology 编辑函数必须配置为函数支持的操作。 以这种方式配置操作可以让您提供附加元数据、配置权限，并在各种操作接口中访问操作。 正如文档中所指出的那样，在操作之外运行编辑函数实际上不会修改任何对象数据。

警告

编辑后立即搜索对象可能会返回意外结果。 详情请参见注意事项部分。

## 定义编辑函数

编辑 Ontology 的函数必须：

- 使用从functions.api导入的@function(edits=[MyObjectType])装饰器来指定将要编辑的对象类型。
- 具有从functions.api导入的显式Array[OntologyEdit]返回类型提示。

## 构建 Ontology 编辑容器

要在 Python 函数中执行 Ontology 编辑，首先从OSDK 客户端构建一个 Ontology 编辑容器。例如：

```
1
2
3
4
5

```

这个容器用于跟踪在函数中所做的所有编辑。

## 更新属性

在Python函数中的Ontology对象默认是只读的。尝试修改其属性将引发异常。

为了编辑一个对象，首先需要使用Ontology编辑容器获取该对象的可编辑视图，可以从现有对象实例获取：

```
1
2

```

或给定一个Object主键：

```
1
2

```

一旦您有一个可编辑的Object，您可以通过重新指派Object的属性值来编辑属性值。例如：

```
1
2

```

在同一函数执行过程中，随后访问editable_employee的last_name属性值将返回刚刚设置的新值。然而，原始的不可编辑Object将不会反映这些更改。

可编辑Object上的数组属性是只读的。要修改数组，请创建其副本，修改副本，然后更新属性：

```
1
2
3
4
5
6

```

请注意，现有Object的主键属性值无法更新。

## 更新链接

单链接和多链接属性有多种方法可以用于更新链接：

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

与更新属性一样，在更新后访问editable_employee的链接将反映您所做的更新。

## 创建Objects

您可以使用Ontology编辑容器上的MyObjectType.create()方法创建新的Objects。创建新的Object时，必须为其主键指定一个值。

在此示例中，我们创建一个具有给定ID的新Ticket Object，设置其due_date属性，并通过修改assigned_tickets链接将其指派给给定的Employee。

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

```

此代码定义了一个函数create_new_ticket_and_assign_to_employee，用于创建一个新的工单并将其分配给指定的员工。通过使用FoundryClient创建和编辑本体对象，函数将新工单添加到员工的已分配工单列表中，并返回所有的编辑操作。
属性值也可以直接传递给创建方法，除了主键。例如：

```
1
2
3

```

## 删除Objects

您可以通过在Ontology编辑容器上调用MyObjectType.delete()方法来删除一个Object。

在此示例中，我们删除指派给指定员工的所有票据：

```
1
2
3

```

可以使用主键而不是实例来删除Objects：

```
1
2

```