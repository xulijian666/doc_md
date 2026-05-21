# 通过旋转探索关联对象

> 来源: https://www.palantir.com/docs/zh/foundry/object-explorer/pivot-linked/

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
对象浏览器
Analyze and compare
通过旋转探索关联对象

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 通过旋转探索关联对象

在进行探索时，可以将探索的主要对象类型转移到任何关联对象类型。让我们通过下面的具体示例来看一下。

如何找到从美国东部大型机场出发的未来30天内的所有航班？

值得注意的是，可以通过探索航班并对其关联机场的属性进行筛选来实现这一点筛选关联属性。也就是说，回答这个问题的另一种方法是从探索机场开始，并筛选这些机场，仅保留位于美国东部且拥有大量独特承运商的机场：

![对机场的探索](/docs/resources/foundry/object-explorer/charts_cluster_map.png)

从这里，我们现在想要旋转到关联的出发航班。我们可以通过点击右下角“关联对象”部分中的此选项来实现。这样做将更改我们探索的主要对象类型为航班，并筛选出仅从我们之前筛选出的那些大型东部机场出发的航班：

![探索旋转到航班](/docs/resources/foundry/object-explorer/pivot_flights.png)

我上面探索的结果现在不再是机场，而是航班（您可以从右侧的预览面板中看到）。可以通过多个链接进行旋转，从而允许您灵活地跨越Ontology进行探索。

←PREVIOUS查看结果
NEXT比较对象集→