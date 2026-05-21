# 对象上的函数

> 来源: https://www.palantir.com/docs/zh/foundry/functions/python-functions-on-objects/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 对象上的函数

您可以使用Python Ontology SDK编写与Ontology交互的函数。

## 生成Python Ontology SDK

要生成Python Ontology SDK客户端，请导航到资源导入侧边栏并选择添加 > Ontology。从那里，选择您想要的Ontology，并导入您希望在函数中交互的任何对象和链接。在保存以确认您的选择后，将为您生成一个Python OSDK客户端，以便您在函数中使用。

## 示例

对于一个名为Aircraft的示例对象类型，具有属性brand和capacity，您可以编写一个接受Aircraft对象并总结它的函数，如下所示：

```
1
2
3
4
5
6
7

```

此外，如果您想搜索满足某个容量阈值的Aircraft对象，您可以编写以下内容：

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

Python OSDK还提供了测试功能，例如与pandas DataFrame的互操作性：

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

```

请查看Python Ontology SDK 文档以获取更多信息。