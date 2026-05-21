# 入门指南

> 来源: https://www.palantir.com/docs/zh/foundry/functions/unit-test-getting-started/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 入门指南

函数自带支持Jest ↗单元测试。按照本指南中的步骤为您的代码库设置单元测试工具。

默认情况下，函数包含一个位于测试文件functions-typescript/src/__tests__/index.ts中的单元测试。您可以在__tests__文件夹中的任何位置创建测试文件。

## 示例

例如，我们可能想要测试位于functions-typescript/src/index.ts中的以下函数addOne:

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

我们可以通过编写以下测试test add one来测试函数addOne:

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

```

请参考Jest API ↗了解完整的测试API。

## 运行测试

您可以通过点击右上角的Test按钮运行所有测试，或者通过点击每个测试行号旁边的三角形“播放”按钮来运行每个单独的测试。

当您点击Commit时，所有测试也将在 Checks 中运行：

![run-tests](/docs/resources/foundry/functions/run-tests.png?width=500)

## 下一步

接下来，了解用于测试与Ontology交互的函数的各种选项：

- 创建存根对象
- 验证Ontology编辑
- 存根Object搜索和聚合