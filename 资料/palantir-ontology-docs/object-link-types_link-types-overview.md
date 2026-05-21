# 概述

> 来源: https://www.palantir.com/docs/zh/foundry/object-link-types/link-types-overview/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 概述

链接类型是两个Object类型之间关系的模式定义。一个链接指的是在同一个Ontology中两个Object之间的关系的单个实例。

例如，在Ontology管理器中，您可以在EmployeeObject类型和CompanyObject类型之间创建一个链接类型，以定义Employee和Employer之间的关系。一个链接指的是Employee → Employer链接类型的单个实例，比如虚构员工“Melissa Chang”和她的雇主“Acme, Inc.”之间的关系。

同样地，在Ontology管理器中，您可以在FlightObject类型和AircraftObject类型之间创建一个链接类型，以定义Scheduled Flight和Assigned Aircraft之间的关系。一个链接指的是Scheduled Flight → Assigned Aircraft链接类型的单个实例，比如“JFK → SFO 24-02-2021”和其分配的飞机“Boeing 737-123”之间的关系。

链接也可以存在于同一类型的两个Object之间。可以在EmployeeObject类型和其自身之间定义一个链接类型Direct Report ↔ Manager。

注意，不支持跨不同Ontology的Object类型之间的链接。在这种情况下，您可能更倾向于利用共享的Ontology。

支撑Ontology的概念在数据集的结构中有类似的概念。在Ontology中链接类型的定义类似于两个数据集之间的合并，而链接的定义类似于在另一个数据集中与同一行字段合并的一行。例如，您可以将Employee数据集与Company数据集合并，以探索Employees和他们的Employers之间的关系。在合并的数据集中，合并“Melissa Chang”和她的雇主“Acme, Inc.”的一行代表一个链接。

Foundry Ontology并非抽象的数据模型，而是将每个本体概念映射到组织的实际数据，使该数据资产能够支持实际应用。通过在Ontology管理器中向链接类型中引用的Object类型添加支持数据源来创建和显示用户应用程序中的链接。对于具有多对多基数关系的链接类型，数据源支持链接类型本身。要创建Employee → Employer类型的链接，组织将向Employee和CompanyObject类型添加支持数据源，并将其员工目录和其他企业数据连接到Ontology中。

通过学习如何创建新的链接类型开始。