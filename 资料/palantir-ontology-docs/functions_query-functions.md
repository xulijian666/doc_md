# 查询

> 来源: https://www.palantir.com/docs/zh/foundry/functions/query-functions/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 查询

查询是只读的 函数 子集，可以通过API 网关非必填地公开。它们不能有任何副作用，比如修改 Ontology 或更改外部系统。如果需要通过 API 网关进行这些额外的编辑功能，您应该使用操作。

## 查询装饰器

要使用Query装饰器，从@foundry/functions-api包中导入它。

```
1
2

```

装饰器还接受一个非必填参数apiName，类型为字符串，您可以用它来定义一个API名称。

### 示例：简单查询

这个简单查询的示例返回在特定时间后起飞的飞机数量。这里没有定义API名称。简单查询的行为类似于带有现有@函数装饰器的函数。

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

```

### 示例: API命名查询

为了通过Foundry的API访问查询，我们在Query装饰器中提供了一个名为apiName的非必填参数。下面的示例演示了如何通过API网关公开之前的查询：

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

该代码定义了一个类PublishedQueries，其中包含一个异步方法countAircraftTakingOffAfter。这个方法通过Objects.search().aircraft()获取所有飞机对象，并过滤出那些距离下次起飞时间大于给定分钟数的飞机，最后返回符合条件的飞机数量。

## API 名称验证

查询的apiName必须是符合以下要求的字符串：

- 使用lowerCamelCase格式。
- 少于 100 个字符。
- 不包含前导数字。
- 在导入到存储库的所有 ontologies 中唯一。如果apiName不唯一，标记过程将失败，您需要更改名称。

此外，包含 API 命名查询的存储库必须从至少一个 Ontology 导入实体。

## 版本和更新 API 命名查询

API 命名查询将始终使用已发布查询的最新标记版本，并且不遵循与其他 Foundry 函数相同的语义版本控制范式。

要取消 API 名称与查询的关联并在 API 网关中中断它，您必须从Query装饰器中删除 API 名称并从存储库发布新标签。

更改装饰器中的 API 名称并发布新标签将中断消费者。仅支持查询的最新发布版本。

为了使消费者可以在不中断的情况下随时升级，您可能希望支持同一 API 名称的多个版本。要做到这一点，您必须在存储库中复制查询代码，并为其指定不同的 API 名称（例如getReschedulableAircraftCountV2）。

## 搜索和查看查询

与其他函数一样，您可以在Ontology 管理器中搜索和管理您的查询。您可以按查询名称或 API 名称搜索。

在下面的示例中，查询的 API 名称为getReschedulableAircraftCount，查询名称为countAircraftTakingOffAfter。

您可能需要更新存储库中的functions.json文件，通过将enableQueries属性设置为 true 来启用查询：

```
1
2
3

```

## 在其他函数库中调用查询

将查询导入到其他函数代码库是一个测试功能，可能会发生更改。在此功能普遍可用之前，可能需要手动迁移。

您可以从函数代码库左侧边栏的资源导入选项卡中导入查询（包括由AIP Logic发布的查询函数）。

然后，可以像调用任何其他函数一样在代码中导入并调用导入的查询函数。

```
## 示例：由 AIP Logic 暴露的查询函数
# 下面的查询函数示例由 AIP Logic 暴露，API 定义为 "generateAText":
import { Objects, Queries } from "@foundry/ontology-api";

export class MyFunctions {

    @Function()
    public async myFunction(subject: string): Promise<string> {
        // 注意：下面的语句等同于 `Queries.generateAText({ subject: subject });`
        return Queries.generateAText({ subject });
    }

}

```

用户必须拥有所需权限以访问并触发AIP逻辑的依赖项，以成功运行导入的查询。