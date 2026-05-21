# 概述

> 来源: https://www.palantir.com/docs/zh/foundry/object-link-types/shared-property-overview/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 概述

测试版功能

共享属性并非在所有Foundry注册中都可用。请联系您的Foundry代表以获取更多信息。

共享属性是可以在您的Ontology中用于多个Object类型的属性。共享属性允许在Object类型之间进行一致性的数据建模，并集中管理属性元数据。尽管属性元数据在Objects之间共享，但底层的Object数据并不共享。

例如，在Ontology管理器中，您可能有Employee和ContractorObject类型，它们都有属性start date。通过创建一个start date共享属性并将其用于这两种Object类型，您可以使用一致的属性来建模数据，并在一个地方更新start date元数据，而不是在每个Object类型上进行更新。

共享属性可以直接创建，或者现有的Object类型属性可以转换为共享属性。添加到您的Ontology后，共享属性可以在Object类型上使用，作为Ontology化数据的一部分，并以类似于常规属性的方式编辑。

Objects上的共享属性在其名称旁边标有一个地球图标。

![Ontology管理器中的共享属性页面](/docs/resources/foundry/object-link-types/shared-property-menu-option.png?width=800)