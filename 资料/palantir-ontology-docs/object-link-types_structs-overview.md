# 概述

> 来源: https://www.palantir.com/docs/zh/foundry/object-link-types/structs-overview/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 概述

Struct 可用性

Struct 属性类型目前正在开发中，将于2024年9月普遍可用。

Struct是一种Ontology基础类型，允许用户创建具有多个字段的基于模式的属性。Struct 属性从 struct 类型数据集列创建。Struct 属性字段可以具有不同的数据源，只要在Ontology中定义之前将属性转换为单个 struct 类型列即可。

许多常见的 Object 属性可以建模为 struct。例如，具有First Name和Last Name字段的Full Name属性，或包含Street、City、Postal Code和Country字段的Address属性。

## Struct 配置

以下是 struct 属性约束和允许配置的列表：

- Struct 的深度为1，不能嵌套。
- Struct 必须至少有1个字段，最多可包含10个字段。
- 目前仅支持以下字段类型：BOOLEANBYTESHORTINTEGERLONGFLOATDOUBLEDECIMALSTRINGBINARYDATETIMESTAMPGEOHASH

## 当前支持水平

随着对 struct 属性类型支持的扩展，其可用性将在 Palantir 平台上有所不同。

Struct 目前在以下应用程序和服务中受到支持：

- Ontology Manager：定义和编辑 struct。
- Workshop：对 struct 的基本渲染支持。
- Marketplace：打包和安装 struct 属性。

Struct 目前在以下服务中尚不支持：

- Object Explorer：目前不支持通过 struct 属性值搜索 Object。
- Functions：Functions 中不支持使用 struct 属性。
- Actions：Actions 中不支持使用 struct 属性。
- Ontology SDK：Ontology SDK 应用程序中不支持使用 struct 属性。

Struct 将不支持 Object Storage V1 (Phonograph)。