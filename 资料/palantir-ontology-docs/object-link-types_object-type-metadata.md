# 元数据参考

> 来源: https://www.palantir.com/docs/zh/foundry/object-link-types/object-type-metadata/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 元数据参考

在Ontology中，一个Object类型由以下元数据表示：

- ID：Object类型的唯一标识符，主要用于在配置应用程序时引用此类型的对象。例如，employee可能是EmployeeObject类型的ID。
- RID：Foundry中每个资源自动生成的唯一标识符。Object类型的RID将在平台上的错误消息中引用。
- 图标：用于作为Object类型的视觉标识符的图片和颜色，当用户查看此类型的对象时将在用户应用程序中出现。例如，人物图标可能用于描绘EmployeeObject类型。
- 显示名称：在用户应用程序中访问此类型对象的任何人显示的名称。例如，EmployeeObject类型的显示名称可能是Employee。
- 复数显示名称：在用户应用程序中访问多个此类型对象的任何人显示的名称。例如，EmployeeObject类型的复数显示名称可能是Employees。
- 描述：关于Object类型的解释性文本，任何人都可以在用户应用程序中阅读。例如，EmployeeObject类型的描述可能是Organization X的所有全职和兼职员工。
- 组：组是帮助您对Object类型进行分类的标签。例如，EmployeeObject类型可能属于组HR和Employee 360。
- API名称：在代码中以编程方式引用Object类型时使用的名称。例如，EmployeeObject类型的API名称可能是Employee。阅读更多关于API名称。
- 可见性：向用户应用程序指示如何重要地显示Object类型。一个重要的Object类型将使应用程序首先向用户显示此Object类型。一个隐藏的Object类型将不会出现在用户应用程序中。默认情况下，EmployeeObject类型的可见性为normal。
- 状态：向用户和其他Ontology构建者发出Object类型在开发过程中的位置的信号。它可以是active，experimental或deprecated。默认情况下，EmployeeObject类型的状态为experimental。阅读更多关于状态。
- 索引状态：Object类型及其支持数据源的最后一次重新索引状态。它可以是success，失败或not started。阅读更多关于索引状态。
- 数据输出：指示Object类型是否生成了数据输出数据集，以及是否允许最终用户对这种类型的对象进行编辑是enabled还是disabled。阅读更多关于数据输出数据集。

了解更多关于在Ontology中创建和配置Object类型以及Object类型元数据的验证要求。

了解更多关于属性（Object类型的特征）。