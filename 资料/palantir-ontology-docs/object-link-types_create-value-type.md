# 创建值类型

> 来源: https://www.palantir.com/docs/zh/foundry/object-link-types/create-value-type/

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
创建值类型

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 创建值类型

按照以下步骤创建一个值类型，以便在您的平台空间中使用。

1. 从平台侧边栏导航到值类型管理器应用程序。
2. 从左上角的下拉菜单中选择您希望创建值类型的空间。
3. 从右上角选择创建新值类型。
4. 为您的值类型提供一个清晰的名称、描述和唯一的API名称。

![值类型元数据创建](/docs/resources/foundry/object-link-types/value-type-create-metadata.png?width=500)
1. 为您的值类型选择一个基类型。
2. （非必填）为您的值类型定义一个约束。验证器可以是字符串类型的正则表达式、枚举、范围或其他验证方法，具体取决于基类型。
有关基类型支持的约束的完整列表，请查看我们的值类型约束文档。

![值类型约束创建](/docs/resources/foundry/object-link-types/value-type-create-constraint.png?width=500)
1. （非必填但推荐）为您的值类型提供一个示例预览值。

![值类型预览创建](/docs/resources/foundry/object-link-types/value-type-create-preview.png?width=500)
1. 保存您的值类型。

←PREVIOUS概述
NEXT使用值类型→