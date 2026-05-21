# API：媒体

> 来源: https://www.palantir.com/docs/zh/foundry/functions/api-media/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# API：媒体

函数在具有严格内存限制的环境中执行。当处理文件数据时，超出这些内存限制可能会很快发生；我们建议仅与小于20MB的媒体进行交互。

如果一个对象有一个媒体引用属性，您可以使用函数与关联的媒体项交互。媒体项提供了许多方法，以便捷地与底层媒体进行交互。有许多内置操作允许您轻松地与不同类型的媒体进行交互，而无需外部库。以下文档解释了可用的功能以及如何使用它们。

如果您需要任何当前尚未提供的操作，您可能需要使用外部库或编写自己的自定义代码。了解更多关于向函数库添加NPM依赖项的信息。

## 通用操作

某些操作被所有媒体类型支持。

### 读取原始媒体数据

要从媒体项中读取原始数据，请在媒体项上使用readAsync方法。您可以通过选择对象上的媒体引用属性来访问媒体项。readAsync方法的签名如下：Blob是一种标准的JavaScript 类型 ↗，表示不可变的原始数据的类似文件的对象。如上所述，您可以将其与库一起使用，以超出默认功能的方式与媒体进行交互。

### 获取媒体元数据

要获取媒体项的元数据，请在媒体项上使用getMetadataAsync方法。getMetadataAsync方法的签名如下：

```
1
2

```

## 类型守卫

提供了几种类型守卫，这将允许您访问特定于某些媒体类型的功能。以下类型守卫可以用于媒体项元数据：

- isAudioMetadata()
- isDicomMetadata()
- isDocumentMetadata()
- isImageryMetadata()
- isVideoMetadata()

例如，您可以使用图像类型守卫提取图像特定的元数据字段：

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

您还可以在媒体项命名空间上使用类型保护，这样可以让您访问更多类型特定媒体项的方法。这里可以使用的类型保护是：

- MediaItem.isAudio()
- MediaItem.isDocument()
- MediaItem.isImagery()

## 文档特定操作

### 文本提取

要从文档中提取文本，您可以在媒体项上使用ocrAsync或extractTextAsync方法。

对于机器生成的PDF，提取嵌入PDF中的数字文本可能比使用光学字符识别（OCR）更快和/或更准确。以下是文本提取用法的示例：

```
1
2
3

```

以下内容可以作为 TypeScript 对象非必填提供：

- startPage: 起始页（包含），从零开始编号。
- endPage: 结束页（不包含），从零开始编号。

对于非机器生成的 PDF，最好使用 OCR 方法来提取文本。

```
1
2
3
4
5

```

以下内容可以选择性地作为 TypeScript 对象提供：

- startPage: 从零开始的起始页（包含）。
- endPage: 从零开始的结束页（不包含）。
- languages: 要识别的语言列表（可以为空）。
- scripts: 要识别的脚本列表（可以为空）。
- outputType: 指定输出类型为text或hocr。

请记住，您需要使用类型保护以访问特定媒体类型的操作。以下是使用isDocument类型保护然后执行 OCR 文本提取的示例：

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

```

## 音频特定操作

### 转录

音频媒体项支持使用transcribeAsync方法进行转录。其签名如下：

```
1
2

```

以下选项是非必填的，可以用来指定转录的运行方式。可用选项包括：

- language：要转录的语言，使用TranscriptionLanguage枚举传递。
- performanceMode：以More Economical或More Performant模式运行转录，使用TranscriptionPerformanceMode枚举传递。
- outputFormat：通过传递一个type为plainTextNoSegmentData（纯文本）或pttml的对象来指定输出格式。如果类型是plainTextNoSegmentData，pttml是一种类似于 TTML 的格式 ↗，该对象还可以接受一个布尔值addTimestamps参数。

以下是提供转录选项的示例：

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