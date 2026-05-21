# 类型参考

> 来源: https://www.palantir.com/docs/zh/foundry/functions/python-function-types/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 类型参考

Beta

Python 函数目前处于测试阶段，可能无法在所有注册中使用。

以下是当前支持的函数 API 类型的完整列表，它们对应的 Python 类型，以及是否可以使用其对应的 Python 类型而不是函数 API 类型进行声明：

| 函数 API 类型 | 可以声明为 Python 类型吗？ | 对应的 Python 类型 |
| --- | --- | --- |
| Array | 是 | list |
| Binary | 是 | bytes |
| Boolean | 是 | bool |
| Byte | 否 | int* |
| Date | 是 | datetime.date |
| Decimal | 是 | decimal.Decimal |
| Double | 否 | float* |
| Float | 是 | float |
| Integer | 是 | int |
| Long | 否 | int* |
| Map | 是 | dict |
| Set | 是 | set |
| Short | 否 | int* |
| 字符串 | 是 | str |
| Timestamp | 是 | datetime.datetime |
| 结构体/自定义类型 | 是 | dataclass.dataclass  (示例) |

虽然Integer和Long都对应于 Python 类型int，但在函数签名中直接标记为int的字段将注册为Integer类型。因此，我们建议使用 API 中的Integer或Long类型来注册数值数据类型。类似的指导适用于Float和Double；如果 Python 类型float直接在您的函数签名中，则默认将注册为Float。

下面显示了另一个带有输入的函数示例：

```
1
2
3
4
5
6
7

```

如上面的类型表所示，此函数也可以仅使用内置Python类型声明：

```
1
2
3
4
5
6
7

```

在这个代码片段中，我们定义了一个装饰函数@function，并创建了一个函数get_end_day_of_week，它接受两个参数：start_time（类型为datetime）和elapsed_millis（类型为整数，表示经过的毫秒数）。该函数应该返回一个字符串类型的结果，表示一周中的结束日期。函数的具体实现逻辑尚未编写。
此外，您可以结合使用内置类型和API类型：

```
1
2
3
4
5
6
7

```

### 自定义类型和结构体

由其他支持类型组成的自定义Python类也可以被用于在函数签名中。API包没有明确的Custom类型；相反，自定义类型被声明为用户定义的Python类。

要成为有效的自定义类型，类必须符合以下要求：

- 类的所有字段必须有类型注解。
- 字段类型必须是支持的类型；可以使用原始的API类型或原生Python类型（如上表所定义）。
- __init__方法必须仅接受与字段具有相同名称和类型注解的命名参数。

dataclasses.dataclass↗装饰器可用于自动生成符合这些要求的__init__方法。

#### 使用dataclasses.dataclass的自定义类型示例

以下是使用dataclasses.dataclass的示例：

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

```

#### 使用API类型的自定义类型示例（不使用dataclass.dataclass）

以下是不使用dataclass.dataclass而使用API类型的示例：

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

```

此代码定义了一个Event类，用于表示带有时间戳和消息的事件。get_event_message函数用于从Event对象中提取和返回消息。

### 下一步

了解如何设置Python函数库，或了解更多关于在Pipeline搭建器或Workshop中使用Python函数的信息。