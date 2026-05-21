# 自动映射结构属性

> 来源: https://www.palantir.com/docs/zh/foundry/object-link-types/struct-automapping/

本体
对象链接类型
Struct types
自动映射结构属性

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 自动映射结构属性

Struct 可用性

结构属性类型目前正在开发中，将于2024年9月普遍可用。

自动映射允许用户自动映射所有列，而不是手动映射。

## 在Ontology Manager中自动映射结构类型

如果Object已经创建，用户可以使用自动映射全部功能自动映射所有列。

1. 在Ontology Manager中，进入属性标签并选择所需的属性。
2. 在列映射标签下，选择所需的列。

![‘列映射’标签和‘自动映射全部’按钮。](/docs/resources/foundry/object-link-types/automap-struct-oma.png?width=500)
1. 选择自动映射全部。

## 在Pipeline Builder中自动映射结构类型

如果Object尚未创建，可以在Object类型创建向导中进行初始Object创建时进行自动映射。

1. 在您的Pipeline Builder管道中，打开相关数据集并选择右上角的所有操作下拉菜单。

![数据集详细信息页面中的所有操作下拉菜单。](/docs/resources/foundry/object-link-types/automap-struct-pipelinebuilder.png?width=500)
1. 选择创建Object类型以创建新的Object。

![‘创建新Object’对话框中的属性标签。](/docs/resources/foundry/object-link-types/automap-struct-properties.png?width=500)
1. 在属性下，添加需要映射的属性。
2. 选择下一步并完成剩余步骤以创建自动映射的Object类型。

←PREVIOUS编辑结构属性类型
NEXT结构属性和共享属性类型→