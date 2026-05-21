# 配置事件

> 来源: https://www.palantir.com/docs/zh/foundry/vertex/configure-events/

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
Events and time series
配置事件

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 配置事件

## 事件配置

要在Vertex中使用事件，需创建一个时间序列事件Object类型，并添加一个额外的Vertex类型类以设置警报的颜色和/或严重性（这可以在任何列上，但通常是主键）：

- 橙色:kind:vertex,name:event_intent.warning
- 红色:kind:vertex,name:event_intent.danger
- 蓝色:kind:vertex,name:event_intent.primary
- 绿色:kind:vertex,name:event_intent.success

可以在本体管理器的功能选项卡中为事件Object配置这些类型类，或直接在Object属性的类型类中配置。

←PREVIOUS概述
NEXT探索相关事件→