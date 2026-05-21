# 使用函数生成图表

> 来源: https://www.palantir.com/docs/zh/foundry/vertex/generate-graph-functions/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 使用函数生成图表

函数可以被用于在编写复杂的搜索周边函数，起始于一个或多个对象，返回一个结果图。这些函数可以从搜索周边工具栏菜单、右键菜单，或通过URL参数创建图表时执行。每个函数必须有且只有一个参数，该参数是一个Ontology对象类型或Ontology对象列表，并且函数必须具有返回类型IGraphSearchAroundResultV1，具体如下所述。

通过工具栏或右键菜单使用时，函数可能有其他类型为Integer、Double、Float、字符串、boolean、Timestamp或Date的参数。在运行这些搜索周边时，将生成一个表单供用户输入这些参数。

![Parameters](/docs/resources/foundry/vertex/graph_generation_and_search_around-parameters.jpg?width=300)

### 搜索周边函数

搜索周边函数是在TypeScript函数库中编写的。有关更多信息，请参见函数文档。

一个搜索周边函数必须声明一个返回类型为IGraphSearchAroundResultV1或Promise<IGraphSearchAroundResultV1>。Vertex 将使用返回类型的名称和结构来发现搜索周边函数，因此它必须如下所示准确声明：

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
15
16
17
18
19
20
21
22
23
24
25

```

- directEdges将在图上表示为两个对象之间的直接边。如果此边基于链接，可以提供其在 Ontology 中找到的linkTypeRid，以显示此边沿的链接类型显示名称，并使 Vertex 了解边的方向。
- intermediateEdges允许您基于事件或其他中间对象在两个对象之间创建边。中间边将表示为两个对象之间的边，并将中间对象分组到该边中。如果在相同的两个对象之间返回多个中间边，所有中间对象将被分组到单个边上。与直接边一样，如果表示的关系是基于一对链接（一个从源对象到中间对象，另一个从中间对象到目标对象），则可以提供这些链接类型 RID。
- orphanObjectRids允许您返回在响应中没有与其他对象链接的对象。参与directEdges或intermediateEdges中的任何对象不需要在此返回。
- objectRidsToGroup允许通过返回一组数组来将对象分组为单个节点，其中每个组是对象 RID 的数组。
- label允许您为在源对象和目标对象之间生成的功能链接指定自定义标签。
- direction允许您更改通过搜索功能产生的功能链接的方向性。提供的值必须是NONE、FORWARD或REVERSE之一。如果省略，则默认为FORWARD。由于存在linkTypeRid而出现的链接不受direction影响。
- layout允许您更改将结果对象添加到图时使用的设计。提供的值必须是auto、auto-grid、grid、linear-row、linear-column或circular之一。如果省略，则默认为层次设计。

## 提示与故障排除

- 为了最大化性能，所有代码应尽可能是异步的。
- Vertex 将使用函数的最新发布版本。要发布您的函数，您需要使用 semver 版本标记您想要的分支/提交，例如 1.0.0。
- 您的存储库需要访问您希望在函数中使用的所有 Ontology 对象和链接。这可以在Repository Settings的Ontology部分进行配置。
- 如果对象类型及其支持的数据集在与存储库不同的项目中定义，则包含存储库的项目将需要引用支持的数据集和这些对象类型。

## 参考示例：

以下示例包含两个Search Around函数。

第一个函数allFlights返回沿航线的所有航班，合并到机场之间的单个边上。例如，当在航线 "SAN -> FAT" 上运行时，它生成以下结果：

第二个函数destinations允许用户选择距离，并返回从初始机场起一定航班数内的所有机场。例如，当在机场 "[ADK] Adak + Adak Island, AK" 上运行，距离为 2 时，它生成以下结果：

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
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99

```

这段代码定义了一些接口和一个类，用于处理图搜索相关的逻辑。IGraphSearchAroundResultV1接口用于表示图搜索的结果，其中包括直接边和中间边的信息。VertexSearchArounds类提供了两个方法：allFlights用于获取航班信息并返回中间边的结果，destinations用于根据给定的机场和距离查找目的地并返回直接边的结果。