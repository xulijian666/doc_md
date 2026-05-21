# API: Object和链接

> 来源: https://www.palantir.com/docs/zh/foundry/functions/api-objects-links/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# API: Object和链接

导入到项目中的每个Object类型都会转换为TypeScript API，以便您可以轻松访问和操作Foundry中可用的Object。

### 属性

每个Object类型的属性都会转换为为每个Object类型生成的TypeScript接口上的字段。生成的字段名称使用Ontology中指定的API名称。

您可以通过简单的点符号访问每个属性的字段：

```
1

```

请注意，由于属性可能没有设置具体值，因此访问属性值时返回的类型可能是undefined。TypeScript编译器会给出错误，除非您明确处理undefined情况。有关详细信息，请参阅此指南。

#### 数组属性

对象类型上的数组属性会转换为ReadOnlyArray类型。这是为了使编辑数组属性的语义清晰——修改数组属性值的唯一方法是用一个全新的数组值更新它。

如果您想操作数组属性的值，请制作它的副本：

```
1
2
3
4

```

### 链接类型

Object类型之间的链接类型也被转换为每个Object类型的TypeScript接口中的字段。要遍历链接，请访问该字段，然后调用用于加载Object的方法之一。链接类型字段名称是使用Ontology中指定的API名称生成的。

Foundry Ontology支持定义1对1、1对多和多对多的链接类型。当访问链接的1端时，生成的字段为SingleLink类型。您可以使用get()或getAsync()方法访问链接的Object：

```
1

```

与属性一样，当您遍历一对一或多对一链接时，如果没有链接的Object，返回值可能是undefined。请遵循指南以处理这些链接的undefined值。

当访问链接的many端时，生成的字段是MultiLink类型。您可以使用all()或allAsync()方法访问链接对象的数组。如果没有链接对象，这些方法将返回一个空数组。

```
1

```

遍历链接可能开销较大，因为这需要在后端加载哪些对象被链接。有关如何更高效地执行链接遍历的详细信息，请参见此部分。

从调用.all()或.allAsync()返回的链接对象数组是一个ReadOnlyArray。如果您想修改该数组，请先制作其副本：

```
1
2

```

您可以将链接作为对象集遍历，以避免在内存中加载链接的Object实例。当在Ontology中创建链接时，将在此类型的对象集上生成API，以“搜索周围”其他链接的对象集。

```
1
2
3
4
5
6
7
8

```

以上代码片段展示了如何从员工对象集中查找与其他对象类型相关的对象集。searchAroundToOtherObjectType方法可以用于检索这些关联对象。
如果您操作一个Object的单一实例并从那里进行搜索，您将得到一个MultiLink<objectType>。您不能将这个MultiLink转换为对象集；您必须将Object实例转换为对象集以便转向其他对象集。

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

### Ontology 元数据

函数通过提供对象和属性列表来访问可用的Ontology。可以通过访问每个对象类型的常量类型来获取Ontology元数据信息。请参阅以下部分以获取更多详细信息。

#### Object 属性元数据

Object 属性也包括类型元数据，这提供了对每个属性类型的程序化访问。您可以使用此功能进行高级工作流，例如识别给定类型的所有属性或验证给定属性名称是否具有特定类型。

例如，对于包含员工对象类型的Ontology，您可以按如下方式访问该对象类型属性的类型信息：

```
1
2
3
4
5
6

```

在这种情况下，如果firstName是Employee对象类型上的一个字符串属性，那么其类型将是StringPropertyBaseType。

可用的属性类型如下：

- BooleanPropertyBaseType
- BytePropertyBaseType
- DatePropertyBaseType
- FloatPropertyBaseType
- TimestampPropertyBaseType
- ShortPropertyBaseType
- GeohashPropertyBaseType
- DecimalPropertyBaseType
- StringPropertyBaseType
- LongPropertyBaseType
- IntegerPropertyBaseType
- DoublePropertyBaseType
- ArrayPropertyBaseType
- VectorPropertyBaseType