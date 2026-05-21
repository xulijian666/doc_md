# 只读模式

> 来源: https://www.palantir.com/docs/zh/foundry/vertex/read-only-mode/

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
顶点
Graphs
只读模式

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 只读模式

在某些情况下，Vertex 图形可以以只读模式打开。 在只读模式下，应用以下限制：

- 无法向图形中添加新的Object（包括通过搜索周边）。
- 图形节点无法重新排列（无论是通过拖放还是其他方法）。
- 页面顶部的工具栏被隐藏。

## 何时以只读模式打开 Vertex 图形？

以下是一些在只读模式下打开图形的情况的非详尽列表。

- 当图形嵌入在 Workshop 中并且在微件配置中明确启用只读模式设置时。
- 当图形在Carbon中打开时。

←PREVIOUS在Workshop模块中嵌入图形
NEXTEvents and time series /概述→