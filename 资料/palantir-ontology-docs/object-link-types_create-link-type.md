# 创建链接类型

> 来源: https://www.palantir.com/docs/zh/foundry/object-link-types/create-link-type/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 创建链接类型

要创建新的链接类型，您可以：

- 从主页标题中的链接类型卡片选择新建链接类型；或者，
- 导航到您想要链接的Object类型，并在该Object类型的概览页面中的链接类型图中选择创建新链接类型按钮。

## 配置新链接类型

创建新链接类型后，必须配置并保存链接类型。在保存新链接类型之前，需要进行以下配置步骤：

![配置新链接类型](/docs/resources/zh/foundry/object-link-types/create-new-link-type-configure-a-new-link-type-annotated.png?width=500)
1. ID:选择链接类型的唯一标识符，主要用于在配置应用程序时引用此类型的链接。ID可以包含小写字母、数字和短划线。ID的第一个字符必须是小写字母。一旦ID被保存，ID就不能更改。
2. Object类型:选择您想要链接到起始Object类型的Object类型。
3. 基数:选择链接类型每一侧的基数。Object类型可以通过四种不同类型的基数进行关联：一对一、一对多、多对一和多对多。在下面的示例中，假设有两个通过基数相关的Object类型：AircraftObject类型和FlightObject类型。一对一基数:这表示一个Aircraft应该链接到一个Flight。注意，一对一基数作为预期关系的指示，但不强制执行一对一映射。一对多基数:这表示一个Aircraft可以链接到多个Flights。多对一基数:这表示多个Aircraft可以链接到一个Flight。多对多基数:这表示一个Aircraft可以链接到多个Flights，并且一个Flight可以链接到多个Aircraft。注意，当您选择多对多基数时，系统会提示您上传一个数据源，其中包含第一个Object类型的主键（在此示例中为Aircraft）和第二个Object类型（在此示例中为Flight）之间所有链接组合。多对多基数，需要一个支持的数据源，以便用户能够编辑或回写链接类型。了解更多关于允许用户编辑数据的信息。
4. 键:选择用于创建链接的属性或列。在一对一或一对多基数链接类型中，一个Object类型的外键属性必须引用另一个Object类型的主键属性。例如，Aircraft ID属性是AircraftObject类型的主键。FlightObject类型上的assigned aircraft ID属性是外键。当Aircraft的Aircraft ID与Flight的assigned aircraft ID匹配时，将在Aircraft和FlightObject类型之间创建链接。在多对多基数链接类型中，选择链接类型支持的数据源中映射到每个链接的Object类型的主键的列。如果Object类型的主键属性的基本类型与在链接类型支持的数据源中映射主键的列的类型不同，将会导致出错，阻止您保存。
5. 显示名称:填写链接类型每一侧的显示名称。链接类型的一侧表示到该Object类型的链接。在本例中，您可以选择显示名称Assigned Aircraft，因为一个Flight具有一个Assigned Aircraft。
6. 复数显示名称:对于基数为多的链接类型的侧面，您还需要填写一个复数显示名称，以便用户应用程序在显示链接对象时能够显示正确的名称。在我们的示例中，FlightObject类型的复数显示名称将描述从Aircraft到Flight的链接。我们可能选择复数显示名称为Scheduled Flights，因为一个Aircraft有多个Scheduled Flights。
7. API名称:填写在代码中以编程方式引用链接类型时使用的API名称字段。链接类型一侧的API名称可以用于返回该类型的Object。例如，如果链接类型Aircraft侧的API名称是assignedAircraft，那么调用Flight.assignedAircraft.get()将返回链接到这些Flight对象的Aircraft对象。链接类型API名称必须：以小写字符开头，并仅由字母数字字符组成。使用驼峰命名法。在与同一Object类型关联的所有链接类型中必须是唯一的。了解更多关于API名称的信息。

填写这些字段后，您将能够保存您的链接类型。要执行此操作，请按照如何保存Ontology更改中的说明进行操作。

## 故障排除

### 出错:Phonograph2:DatasetAndBranchAlreadyRegistered

如果您收到错误Phonograph2:DatasetAndBranchAlreadyRegistered，则您尝试保存的链接类型所支持的数据源已经支持Ontology中的其他链接类型，无法再次使用。