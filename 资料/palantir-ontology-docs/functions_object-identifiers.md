# Object标识符

> 来源: https://www.palantir.com/docs/zh/foundry/functions/object-identifiers/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# Object标识符

在Foundry中，Object的身份有几种不同的表示方式，理解这些不同的表示对于在函数中编写正确的代码非常重要。本节解释了对象标识的各种方式以及对代码的影响。

## 标识符类型

### Object RIDs

"RID"指的是资源标识符 ↗，这是Palantir用于标识实体的开源规范。Ontology对象在创建时会被指派一个RID，创建方式可以是通过索引支持的数据集，或者作为操作的一部分。

在函数中，每个Ontology对象都有一个类型为string | undefined的rid字段。RID可能未定义的原因是可以使用对象创建API在函数中创建新对象。新创建的对象总是具有undefined的rid值，而现有对象总是具有已定义的rid。

### 主键

Object还可以通过其对象类型和主键唯一标识。主键是唯一的propertyId和值对。例如，Employee对象类型可以通过一个名为employeeId的字符串属性唯一标识。

所有Ontology对象总是具有typeId和primaryKey字段，包括新创建的对象。这是因为在创建新对象时必须提供主键。

## 对代码的影响

### 检查相等性

在函数中，每个Ontology对象都使用JavaScript对象 ↗表示。一个Ontology对象可能会被表示为多个JavaScript对象。例如，如果您多次从Object搜索加载Ontology对象，或者在对象搜索中加载对象以及将其作为参数传入，这种情况就可能发生：

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

```

此代码片段用于比较员工对象。虽然employee和employee2是不同的对象实例（因此==和===比较都返回false），但它们的id属性相同（因此employee.id === employee2.id返回true）。
即使在上述示例中，employee和employee2都指的是相同概念的Ontology对象，用==和===运算符比较它们会返回false，因为变量指向两个不同的 JavaScript 对象。简单地比较rid字段可能会有问题，因为新创建的对象的rid为undefined。

因此，比较两个Ontology对象是否相等的最佳方法是比较typeId和primaryKey:

```
1
2
3
4
5

```

### Object 映射

将 Object 映射到某个值通常是有用的。例如，您可能希望遍历一个对象数组并存储值以便更高效地查找。

由于上述相等性检查问题，您不能简单地使用 JavaScript Map 来为每个 Object 存储值。相反，您可以使用FunctionsMap，它专门设计用于支持 OntologyObjects 作为键。