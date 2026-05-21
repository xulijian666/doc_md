# 高级用法

> 来源: https://www.palantir.com/docs/zh/foundry/functions/python-functions-advanced-usage/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 高级用法

## 发布查询函数

要注册一个可从其他 TypeScript 或 Python 函数调用的 Python 函数，必须为您的 Python 函数提供一个 API 名称。为此，请在@function装饰器中提供api_name字段：

```
1
2
3
4
5

```

## 调用查询函数

在发布您的 TypeScript 或 Python 查询函数后，导航到您希望使用该函数的代码库，并使用资源导入侧边栏导入它。

然后，您的函数将可以从使用该函数的代码库中调用。例如，要从 Python 函数中调用它：

```
1
2
3
4
5
6
7

```

从TypeScript函数调用它：

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

```

从Python函数调用TypeScript查询函数看起来完全相同；使用API名称发布TypeScript查询函数，然后如上所示从Python中使用它。