# 模拟用户和组

> 来源: https://www.palantir.com/docs/zh/foundry/functions/unit-test-users-groups/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 模拟用户和组

### 用户模拟

您可以使用createUser创建用户的部分模拟，其中除了id和username之外的所有属性都是非必填的。您需要从"@foundry/functions-testing-lib"导入{ createUser }。

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

```

这可以被用于在测试以下函数：

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

### 分组模拟

您还可以使用createGroup创建一个部分分组模拟，其中除了id之外的所有属性都是非必填的。您需要从"@foundry/functions-testing-lib"导入{ createGroup }。

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