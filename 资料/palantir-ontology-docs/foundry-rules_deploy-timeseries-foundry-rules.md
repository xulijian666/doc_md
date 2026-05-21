# 部署时间序列 Foundry 规则

> 来源: https://www.palantir.com/docs/zh/foundry/foundry-rules/deploy-timeseries-foundry-rules/

本体
Foundry规则
Time series
部署时间序列 Foundry 规则

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 部署时间序列 Foundry 规则

这些说明假设您的平台中已设置时间序列。了解更多关于在 Foundry 中使用时间序列的信息。

要在 Foundry 规则中启用时间序列功能，请首先按照步骤部署 Foundry 规则。一旦您部署了 Foundry 规则，下面描述的步骤是启用时间序列支持所必需的：

1. 要创建时间序列规则，其中一个工作流输入必须是时间序列根Object类型。对于所有您希望编写时间序列规则的输入Object类型，切换启用时间序列开关。
2. 如果您的时间序列数据是使用时间序列属性设置的，则无需额外配置步骤，您可以开始编写基于时间序列的规则。然而，如果您的时间序列数据是使用测量值配置的，您必须完成以下步骤：

- 切换启用时间序列开关时，将打开一个对话框，提示您选择从系列Object类型到根Object类型的链接。
- 然后，在变换配置部分，您必须添加支持这些测量值的所有时间序列同步。

←PREVIOUS时间序列规则
NEXTLegacy Foundry Rules Setup (Taurus) /旧版 Foundry 规则设置 (Taurus)→