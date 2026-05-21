# 创建结构属性类型

> 来源: https://www.palantir.com/docs/zh/foundry/object-link-types/create-struct-type/

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
Struct types
创建结构属性类型

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 创建结构属性类型

结构可用性

结构属性类型目前正在开发中，将于2024年9月正式发布。

从Ontology Manager中的Object类型页面创建和配置一个新的结构属性。有关结构属性的更多信息，请参见概述。

1. 在Ontology Manager中，打开左侧边栏的Object类型选项卡，并选择一个现有的Object类型。
2. 在Object类型详细信息页面，打开左侧边栏的属性选项卡，并在属性表的右上角选择创建属性按钮。

![Object类型属性表和'属性编辑器'面板。](/docs/resources/foundry/object-link-types/create-struct-from-ontology-manager.png?width=500)
1. 在属性编辑器面板中，添加名称和描述，并从基础类型下拉菜单中选择结构。

![基础类型下拉菜单中选择了'结构'。](/docs/resources/foundry/object-link-types/name-struct-from-ontology-manager.png?width=500)
1. 向下滚动到数据部分，并从下拉菜单中选择一个支持列。

![在属性编辑器的数据部分选择一个支持列。](/docs/resources/foundry/object-link-types/backing-column-struct-ontology-manager.png?width=500)
1. 在结构字段部分，选择添加字段，然后选择新字段。

![结构属性类型中的示例结构字段。](/docs/resources/foundry/object-link-types/struct-field-ontology-manager.png?width=500)
1. 为新结构字段命名，并非必填添加描述。
2. 最后，将数据源中的一列映射到新的结构字段。

←PREVIOUS概述
NEXT编辑结构属性类型→