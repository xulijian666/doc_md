# 抛出用户界面错误

> 来源: https://www.palantir.com/docs/zh/foundry/functions/user-facing-error/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 抛出用户界面错误

在平台的其他部分运行函数时，例如Workshop或操作，您可能希望抛出带有详细信息的错误。为此，请从@foundry/functions-api包中抛出一个UserFacingError。例如：

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

```

当在Workshop 应用程序中以函数支持的操作运行此操作且员工数量不正确时，用户将看到以下错误：

通过添加详细的用户界面错误信息，您可以帮助您的函数的其他用户快速识别和解决问题。