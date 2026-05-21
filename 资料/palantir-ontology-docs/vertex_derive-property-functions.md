# 使用函数派生属性

> 来源: https://www.palantir.com/docs/zh/foundry/vertex/derive-property-functions/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 使用函数派生属性

函数被用于在对象上创建派生属性。这些属性可以显示在对象视图中，显示在扩展节点标签中，并用于在图层样式选项中为节点着色。

任何符合以下条件的函数都可用作派生属性：

- 方法是public。
- 方法使用了@Functions()装饰器。
- 方法返回一个 FunctionsMap。
- FunctionMap中的所有键都是对象。
- FunctionsMap中的所有值都是原始类型或具有原始类型的自定义类型。
- 方法已被标记为发布。
- 方法操作于对象集（例如ExampleDataRoute[]），而不是单个对象（例如ExampleDataRoute）。这确保了函数不会针对图中每个对象单独调用，从而避免在大型图中导致非常慢的性能。

例如：

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

此代码定义了一个类VertexDerivedPropertyFunctions，其中包含一个异步函数flightCancellationPercentage，用于计算每个给定航线的航班取消百分比。函数使用FunctionsMap来存储每个ExampleDataRoute对应的取消百分比。通过Promise.all并行获取航线的所有航班信息，提高了效率。