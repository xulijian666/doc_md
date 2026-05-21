# 创建存根对象

> 来源: https://www.palantir.com/docs/zh/foundry/functions/unit-test-stub-objects/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 创建存根对象

您可以使用Objects.create()创建和定义您的模拟对象，这与使用常规函数的方式相同。然后，您可以在编写单元测试时使用这些模拟对象。以下是一个示例：

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

```

供参考，上述示例使用的是Jest语法expect(...).toEqual(...)↗。