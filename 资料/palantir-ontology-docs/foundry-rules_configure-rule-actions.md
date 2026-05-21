# 配置规则操作

> 来源: https://www.palantir.com/docs/zh/foundry/foundry-rules/configure-rule-actions/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 配置规则操作

在2022年7月之前，Foundry Rules（以前称为Taurus）使用Foundry操作作为规则输出。仅当您在2022年7月之前部署了Foundry Rules时，此部分才相关。

规则操作是在Foundry Rules中用于对规则的输出实施输出模式的一种方法。这是通过使用Foundry操作作为指定列名和类型的机制来实现的。规则操作是将被用于Foundry Rules中的Foundry操作。

![配置用于Foundry Rules的Foundry操作](/docs/resources/foundry/foundry-rules/example_rule_action_configuration.png?width=500)

上面截图中的操作仅被用于在变换内，不会自行运行。方便的是未为操作配置任何操作规则（上面截图中的1），因此即使操作被运行，也不会产生任何效果。

操作的参数将在Foundry Rules Workshop应用程序中呈现给最终用户，并可用于映射到规则逻辑输出的列（上面截图中的2）。

- 参数类型将被用于实施正确的列类型。例如，如果使用日期类型参数，则只有日期和时间戳类型的列可用于映射到此参数。此外，如果参数ID与您的规则中的列名或Object属性ID匹配，它将用于预填充此列/属性的参数。
- 任何标记为必需的参数在Foundry Rules Workshop应用程序中也将是必需的。同样，非必填参数可以留空，没有列映射到它们，这等同于为参数提供null值。
- 参数名称将在Foundry Rules Workshop应用程序中用作标签，参数ID将在变换中的结果数据集中用作列名。
- 除了参数ID外，输出数据集还将包含一个taurus_rule_id列，以指示行所来源的规则ID。

定义提交标准（3）是保存操作的要求。规则操作最常见的提交标准是检查当前用户是否属于具有编辑Foundry Rules工作流程权限的用户组。在Foundry Rules应用程序中编辑规则时将应用此验证。