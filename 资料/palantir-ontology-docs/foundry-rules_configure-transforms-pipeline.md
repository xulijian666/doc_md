# 配置变换管道

> 来源: https://www.palantir.com/docs/zh/foundry/foundry-rules/configure-transforms-pipeline/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 配置变换管道

2022年7月之前，Foundry Rules（以前称为Taurus）要求用户创建自己的变换来运行Foundry Rules。本节仅与2022年7月之前部署Foundry Rules的情况相关。

一旦在Workshop应用中编写和审核规则后，编码逻辑将作为变换的一部分应用。本节解释变换的各种组件以及如何为您的应用案例配置它们。大部分变换通过默认部署自动配置；然而，工作流的扩展可能需要额外的步骤。

## 示例变换

在部署Foundry Rules变换之后，变换将类似于下面的示例：

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
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50

```

In this code, comments are added to explain the purpose and usage of various methods and parameters within the Java class. These comments have been translated into Chinese for better understanding in a Chinese context.

## 使用@AdditionalInputs添加Ontology输入

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

这个Java代码片段定义了一个使用ImmutableOntologyInputs构建器模式创建的静态集合additionalInputs。它包含对本体对象和关系的引用，可以用于指定输入规范。代码中有注释说明了每个方法调用的作用，其中包括了一个关于员工对象的示例。
您可以使用@AdditionalInputs来提供访问Foundry Rules中使用的对象类型的元数据的权限。任何配置用于Foundry Rules Workshop应用程序的对象类型必须在此添加。第一个对象类型RID将默认填写，但作为部署工作流模板部分添加的任何其他对象，必须作为额外的.addObjectRids()条目添加。

此外，任何将在Workshop应用程序中使用的_关系_必须在此作为.addLinkRids()条目添加。RID可以通过Ontology管理器分别在对象类型和关系页面中获取。

添加这些条目后，还需要使用代码仓库的设置选项卡中的Ontology导入助手将对象类型和关系导入项目中。

## 输入和输出数据集

```
1
2
3
4
5
6

```

本节提供应用中Foundry规则使用的所有输入的数据。这包括Foundry规则中使用的任何Object和多对多合并表的基础数据集。默认情况下，其中一些将会预先填充。

然而，在部署工作流模板时添加的任何其他Object或数据集，必须在此处添加为新的@Input条目。这些数据集将在后续作为TaurusRuleRunner.Args的一部分所需。

此外，您必须为rule_status_output的输出提供路径。该数据集包含任何未成功运行的规则的详细信息，是一个有用的调试工具。

## Foundry规则运行器

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

```

本节配置规则运行器 (TaurusRuleRunner)，最终将运行在rulesDataset中提供的 Foundry 规则。本节大部分情况下默认是预配置的，但如输入和输出数据集中所述，任何额外的输入必须通过添加额外的.putSources()条目来注册到TaurusRuleRunner中。此外，任何在配置了 Foundry 规则的对象之间使用的多对多合并表，必须在此使用.manyToManyJoinTables()注册，如上例所示。

## 规则操作数据集

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

规则操作作为一组 Foundry 规则的通用输出架构。在使用.runRules()运行所有规则后，可以通过调用.actionReadyMergedDataset()并使用所需操作的操作类型 RID来获取特定规则操作的所有结果行。此 RID 可以在Ontology 管理器的操作类型视图中找到。

返回的数据集可以写入如上例所示的变换输出。该数据集将包含每个操作参数的一个列，以及一个包含该行来源规则 ID 的Foundry Rules_rule_id列。

可以通过复制示例并更换操作类型 RID 以及添加新的输出数据集，将额外的规则操作添加到 Workshop 应用中，如输入和输出数据集部分所述。

如果在运行变换或 CI 检查时遇到任何出错，请查看故障排除参考。

### 参考实现

如果由您的 Palantir 代表配置，可能会有上述变换的参考实现可用。搜索Business Rules with Rules Workflow文件夹或导航到Foundry 训练和资源项目，然后到参考示例 → Workshop 中的应用开发 → Business Rules with Rules Workflow。

在这里，您将找到一个在示例航空 Ontology 上实现的模板工作流应用和变换管道。