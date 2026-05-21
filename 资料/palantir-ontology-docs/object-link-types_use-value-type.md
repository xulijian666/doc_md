# 使用值类型

> 来源: https://www.palantir.com/docs/zh/foundry/object-link-types/use-value-type/

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
Value types
使用值类型

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 使用值类型

一旦创建了一个值类型，您可以在Foundry中将其用作数据类型。值类型可以支持以下应用案例。

- 将值类型指派给Object类型属性。
- 将值类型指派给共享属性。
- 将值类型指派给Pipeline Builder管道属性，作为逻辑类型，使用logical type cast表达式，并在写入对象目标时在属性上选择值类型。

要将值类型指派给属性，在属性配置期间从下拉菜单中选择值类型。

![约束更新警告](/docs/resources/foundry/object-link-types/value-type-use.png?width=500)

如果您将值类型应用于包含出错验证的属性值的Object属性，该Object类型将无法索引。您可以在Ontology Manager中的Object类型健康状态中查看此类索引失败，您可以在其中更正数据或更新值类型以解决问题。

←PREVIOUS创建值类型
NEXT值类型版本→