# PDF处理

> 来源: https://www.palantir.com/docs/zh/foundry/functions/pdf-handling/

本体
函数
Semantic search
PDF处理

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# PDF处理

本页面提供了一个基本指南，以使用Pipeline Builder解析PDF以进行语义搜索，并推荐在Workshop应用中展示信息的方法。

语义搜索是处理PDF的强大工具，特别是当内容被分解成更小的单独嵌入的“块”时，帮助用户和工作流找到可能难以访问的重要信息。这在考虑到PDF中大量未被注意的非结构化知识时尤其有用。

要使用此功能，只需将您的PDF上传到Foundry，提取文本，分块相同的文本，搜索这些块，并通过侧边呈现相应的PDF来为用户提供交叉验证的真实来源。

## 设置语义搜索以在PDF中进行搜索

按照以下步骤导入PDF并建立语义搜索，以从PDF中呈现内容：

1. 将PDF导入为媒体集
2. 将媒体集添加到Pipeline Builder中
3. 使用获取媒体引用面板。

1. 使用文本提取面板。

1. 遵循分块策略。
2. 创建具有媒体引用属性的块对象。
3. 在语义搜索工作流中搜索块。
4. 在Workshop中使用PDF查看器微件，注意配置选项。

←PREVIOUS分块
NEXTOntology edits /概述→