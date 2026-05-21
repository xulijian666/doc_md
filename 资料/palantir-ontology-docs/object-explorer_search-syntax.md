# 搜索语法

> 来源: https://www.palantir.com/docs/zh/foundry/object-explorer/search-syntax/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 搜索语法

Object Explorer支持跨所有对象及其属性的搜索。为了帮助您找到所需内容，本页面描述了全局搜索栏的搜索语法。

### 引号

默认情况下，输入搜索栏的单个单词将独立进行搜索。例如，搜索yellow cab将返回所有属性值匹配yellow或cab的对象。

此行为可以通过使用引号来改变。在Object Explorer中搜索"yellow cab"将返回所有在一个或多个属性值中具有确切短语yellow cab的对象。像这样搜索短语通常会比搜索单个单词产生更少的结果。

### 逻辑运算符 (AND/OR)

运算符AND和OR可以用于增强Object Explorer中的文本搜索。例如，要搜索涉及曼哈顿和布鲁克林的出租车行程，可以搜索Manhattan AND Brooklyn。

类似地，要搜索涉及曼哈顿或布鲁克林的出租车行程，可以搜索Manhattan OR Brooklyn。

使用引号创建的短语也可以被纳入搜索。例如，"yellow cab" AND Manhattan是一个有效的表达式。

逻辑运算符也可以使用括号结构化为更复杂的表达式。例如，此搜索返回引用曼哈顿及黄色或绿色出租车的对象：("yellow cab" OR "green cab") AND Manhattan

### 通配符

- ?: 问号可用于替换单个字符搜索qu?ck会返回quick、quack、qu4ck等结果
- *: 星号可用于替换零个或多个字符搜索bro*会返回bro、brother、broadcasting等结果

无法在Object Explorer中搜索带有“前导通配符”的术语，即以?或*开头的术语。如果您需要执行此类查询，请考虑使用其他工具，例如Contour。

### 模糊搜索

在搜索词末尾使用~运算符可执行“模糊”匹配，除了确切匹配外还会匹配相似的术语。例如，quikc~会返回quick和quack的结果。