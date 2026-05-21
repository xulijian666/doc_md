# 为新Objects生成唯一ID

> 来源: https://www.palantir.com/docs/zh/foundry/functions/edits-generate-id/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 为新Objects生成唯一ID

在编写创建Objects的Ontology编辑函数时，您可能需要为新创建的Object生成一个唯一ID。您可以通过使用@foundry/functions-utils包在函数中设置这一点，以生成全局唯一标识符。

## 导入包

默认情况下，@foundry/functions-utils包已安装，但如果package.json文件中不存在该包：

- 在"dependencies"部分添加"@foundry/functions-utils": "0.1.0"

如添加依赖项的文档中所述，请记得重启Code Assist以使新包可用于自动补全。

## 在代码中使用包

要生成唯一ID，您可以使用@foundry/functions-utils包中的Uuid.random()工具函数。下面的代码示例展示了如何在一个示例Ontology编辑函数中使用random函数。

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