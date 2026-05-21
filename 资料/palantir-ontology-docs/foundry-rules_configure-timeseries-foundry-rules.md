# 配置时间序列

> 来源: https://www.palantir.com/docs/zh/foundry/foundry-rules/configure-timeseries-foundry-rules/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 配置时间序列

2022年7月之前，Foundry Rules（以前称为Taurus）要求用户创建自己的变换来运行Foundry Rules。本节仅在您于2022年7月之前部署了Foundry Rules时相关。

这些说明假设您的平台已经设置了时间序列。了解更多关于在Foundry中使用时间序列的信息。

如果您正在创建一个新的工作流，请按照步骤部署Foundry Rules。如果您在2022年7月之前部署了Foundry Rules，则需要以下描述的额外步骤来启用时间序列支持。

## Workshop应用程序

在Workshop应用程序中开始编写时间序列规则有两个步骤：

1. 必须开启规则编辑器中的启用时间序列规则配置。要导航到此处，请编辑您的Workshop模块，点击规则编辑器微件，并找到标记为启用时间序列规则的选项。
2. 要创建时间序列规则，源Object必须是根Object类型。将所有需要的根Object类型添加到允许的Object类型集合中。这里添加的所有Object也需要添加到变换管道中。

## 变换管道

Foundry规则作为变换的一部分运行。确保您已经按照说明设置了管道。

## 额外输入

本节提供访问时间序列元数据的权限。为了运行时间序列规则，您必须将更多项目添加到额外输入中：

- 对于支持时间序列数据的每个时间序列同步，使用.addTimeseriesSyncRids添加同步RID。
- 对于上面时间序列同步中使用的每个tick数据集，使用.addBackingDatasetRids添加tick数据集的RID。这些是包含实际时间序列数据的数据集。
- 使用.addObjectRids添加根Object和传感器Object的RID。
- 使用.addLinkRids添加根Object和传感器Object之间关系的RID。

### 示例

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

```

此代码片段定义了一个additionalInputs集合，用于描述不同的对象、关系和数据集在本体论中的输入规格。注释中包含了对每个标识符的解释，例如根对象、传感器对象、时间序列同步等。

### 项目引用

还需要使用代码库的设置选项卡中的Ontology Imports助手，将根Object类型、传感器Object类型及其关系导入项目。

此外，如果时间序列同步或其支持的ticks数据集与变换不在同一项目中，则还必须使用项目视图的项目引用部分将它们导入项目。

![规则工作流项目视图](/docs/resources/foundry/foundry-rules/project_reference_compass_1.png?width=400)
![规则工作流引用](/docs/resources/foundry/foundry-rules/project_reference_compass_2.png?width=400)