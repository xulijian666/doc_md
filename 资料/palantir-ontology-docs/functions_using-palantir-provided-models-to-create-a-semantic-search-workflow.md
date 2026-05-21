# 使用Palantir提供的模型创建语义搜索工作流

> 来源: https://www.palantir.com/docs/zh/foundry/functions/using-palantir-provided-models-to-create-a-semantic-search-workflow/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 使用Palantir提供的模型创建语义搜索工作流

要使用Palantir提供的语言模型，必须先在您的注册中启用AIP。您还必须拥有使用AIP开发者功能的权限。使用自定义模型？请查看使用自定义模型创建语义搜索工作流。

本页说明了使用Palantir提供的嵌入模型构建概念性的端到端语义搜索工作流的过程。

## 说明

首先，您需要生成嵌入并将其存储在具有vector类型的对象类型中。然后，您可以在Workshop中设置语义搜索工作流，搭建一个AIP Agent增强的工作流，或创建一个自定义语义搜索函数以用于Workshop和AIP Logic。

前提条件：

- 生成嵌入并创建对象类型

选项：

- 在Workshop中使用KNN对象集（无代码）创建简单的语义搜索工作流
- 启用AIP Agent进行对象的语义搜索（无代码）
- 创建一个函数以在Workshop和/或AIP Logic中跨对象进行语义搜索

## 生成嵌入并创建对象类型

我们将使用Pipeline Builder将数据集中的文本嵌入为向量，使用Text to Embeddings表达式。该表达式接收一个字符串并使用一个Palantir提供的模型将其转换为向量 - 在我们的案例中使用text-embedding-ada-002嵌入模型。

然后可以将这些嵌入作为向量属性添加到Ontology中。

如果您希望对使用Palantir提供的模型生成嵌入有更多控制，请参见Python变换中的语言模型。

## 在Workshop中使用KNN对象集（无代码）创建简单的语义搜索工作流

在Workshop中配置一个KNN对象集是构建语义搜索工作流的简单无代码方法。

1. 创建一个对象集变量并选择包含嵌入属性的对象类型。
2. 选择筛选+ On a property选项，然后从菜单中的属性列表中选择您的嵌入属性。
3. 选择后，K-nearest-neighbors配置应出现。如果此配置未出现，请验证您选择的属性是嵌入属性。

在此面板中，您可以配置：

- K值：一个介于1-100之间的数字，用于指示在语义搜索中返回多少个对象。
- 查询：在执行语义搜索时用作查询的字符串变量。

1. 接下来，创建一个字符串选择器微件并将其输出变量添加到上述KNN查询选项中。
2. 最后，添加一个对象表微件并将其输入变量配置为新创建的KNN对象集。

有关更自定义的语义搜索逻辑，请参见函数部分。

## 使用AIP Agent（无代码）

在AIP Chatbot Studio中创建的AIP Agent非常适合起始跨对象的语义搜索，因为它们不需要任何代码。了解更多关于结合语义搜索以更好控制功能性。

按照入门指南中的说明创建一个AIP Agent，并添加Ontology上下文或一个Ontology语义搜索工具。此初始设置将使您能够请求AIP Agent进行对象的语义搜索。

## 创建一个函数以在Workshop或AIP Logic中使用

我们可以创建一个typescript代码库并创建一个函数来查询我们的对象类型。总体目标是能够接收一些用户输入，使用与之前相同的Palantir提供的模型生成向量，然后对我们的对象类型进行KNN搜索。有关如何导入Palantir提供的模型的更多信息，请查看函数中的语言模型。

替换

在下面的代码片段中，将每个ObjectApiName实例替换为您的唯一ObjectType。请注意，标识符有时可能以小写字母objectApiName出现。

为函数启用向量属性

在继续之前，确保在您的Functions代码库中的functions.json文件中存在条目"enableVectorProperties": true。如果此条目不存在，请将其添加到functions.json并提交更改以继续。如需进一步协助，请联系您的Palantir代表。

### functions-typescript/src/index.ts

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
25
26
27
28

```

此时，我们已经有一个可以运行语义搜索以使用自然语言查询Objects的函数。记得发布函数以便该函数可以在Foundry内的任何地方使用。

### 在Workshop中使用语义搜索函数

1. 首先创建一个Workshop应用。
2. 添加一个文本输入微件，它将用作已发布KNN文档获取函数的输入。
3. 添加一个对象列表微件，并使用从函数生成的对象集作为输入，如下所示：

![KNN函数生成对象集](/docs/resources/foundry/functions/semantic-search-workshop-function.png?width=450)
1. 将kValue设置为您希望返回的结果数量，受指定限制的约束。

### 在AIP Logic中使用语义搜索函数

将已发布的函数作为工具添加到AIP Logic中。使用类似以下的提示指示语言模型使用该工具：

> 使用fetchRelevantObjects工具并将kValue设置为5，以找到最相关的Objects。使用工具时，记得在查询周围添加引号。