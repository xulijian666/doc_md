> 来源: https://www.palantir.com/docs/zh/foundry/object-link-types/copy-object-type-config/

Search
Palantir
Documentation
搜索文档
Search
karat

+

K

API 参考 ↗
Send feedback
ZH
en
jp
kr
zh
ABXY
ABXY
ABXY
ABXY
ABXY
ABXY
ABXY
- 功能数据连接与集成用例开发分析模型集成开发运维安全本体管理
- 入门
- 平台概述

本体
对象链接类型
Object types
选择要复制的Object类型

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

Object类型有时可能具有相似的模式。例如，Car和Truck的模式可能非常相似，仅有少数不同的属性。为了减少设置TruckObject类型所花费的时间，您可以从CarObject类型复制配置。

## 选择要复制的Object类型

您可以通过以下步骤复制Object类型的配置：

1. 在Object类型视图侧边栏的右上角选择三个点。
2. 从下拉菜单中选择复制配置到另一个Object类型选项。这将打开复制Object类型配置对话框。

## 复制Object类型配置

复制Object类型配置对话框将为您提供以下选项：

- 选择一个现有的Object类型作为复制的目标Object类型配置，或
- 创建并命名一个带有复制的Object类型配置的新Object类型。

![复制Object类型配置对话框](/docs/resources/foundry/object-link-types/copy-object-type-configuration-dialog.png?width=300)

选择确认将复制所有起始Object类型的属性及其元数据（例如状态、渲染提示等）。

警告

如果选择的现有Object类型作为复制目标已经存在属性，可能会发生以下情况：

- 现有Object类型上的现有属性将被起始Object类型复制过来的属性覆盖。
- 如果列名称与复制的属性名称匹配，复制的属性将自动映射到现有Object类型的支持数据源。

因此，当选择现有Object类型作为复制目标时，请确保目标Object类型与您要复制的Object类型具有相同的模式。

←PREVIOUS编辑Object类型
NEXT通过类型映射启用 Gotham 集成→