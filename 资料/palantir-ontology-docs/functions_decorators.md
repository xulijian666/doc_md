# 装饰器

> 来源: https://www.palantir.com/docs/zh/foundry/functions/decorators/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 装饰器

TypeScript ↗函数被声明为TypeScript 类 ↗的方法。发现和发布函数有一些要求：

- 方法必须是public
- 方法所属的类必须从functions-typescript/src/index.ts文件中导出
- 方法必须用从@foundry/functions-api包导入的以下装饰器之一进行装饰：通用函数使用@Function()。用于支持操作的函数使用@OntologyEditFunction()。使用@OntologyEditFunction()方法时，可以选择性地使用@Edits([object type])装饰器指定 Object 来源信息。如果缺少@Edits([object type])装饰器，Object 来源信息将通过代码的静态分析以尽力而为的方式推断。只读查询可以通过Foundry API执行的使用@Query({ apiName: "userDefinedAPIName"})。请注意，此装饰器不应与@Function装饰器同时使用；应单独使用。

以下是以这种方式正确导出的函数示例：

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

```

任何私有方法或未使用相关装饰器的装饰方法都不会发布到函数注册表。这允许用户创建辅助函数和实用工具以便重用或组织。

重新发布

请注意，每个TypeScript库中的函数都是由其类名和方法名唯一定义的——如果您更改类或方法的名称，该函数将以新的标识符发布。