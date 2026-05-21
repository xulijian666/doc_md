# 类型类

> 来源: https://www.palantir.com/docs/zh/foundry/object-link-types/metadata-typeclasses/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# 类型类

类型类可应用于属性、链接类型和操作类型。它们定义了可由与Ontology交互的用户应用程序解释的附加元数据。例如，某些hubble属性类型类的规范会影响属性值在Object视图中的呈现方式。其他类型类的规范，如analyzer，会影响属性值在Object存储V1 (Phonograph)中被索引时的处理方式。

下表提供了已知类型类的列表。此表中的列如下：

- 已弃用列指示类型类是否仍受支持。已弃用列还指示是否应在功能页面中配置类型类。在Ontology管理器中，对象类型现在有一个功能页面，用于配置历史上定义为类型类的特性。所有受支持的类型类的配置将移至功能页面。
- 类型列指示类型类是应用于属性、链接类型（以前称为关系）还是操作类型。
- 种类和名称列包含在Ontology管理器中添加类型类时设置的两个用户定义字段的字符串值。这些值被Foundry产品用于标记类型类。

![添加类型类 - 种类和名称字段](/docs/resources/foundry/object-link-types/typeclasses-kind-name.png?width=300)
- 描述列描述了用户应用程序在与添加了列出的类型类的属性值、链接或操作交互时的预期行为。Object Explorer是一个使用hubble类型类的应用程序。Object存储V1 (Phonograph)是一个使用analyzer类型类的服务。Quiver是一个使用timeseries类型类的应用程序。

| 已弃用 | 类型 | 种类 | 名称 | 描述 |
| --- | --- | --- | --- | --- |
|  | 属性 | hubble | media_url | 当属性出现在Object视图中时，将其呈现为媒体项目。 |
| 已弃用 | 属性 | hubble | editable | 允许用户在Object视图中编辑属性。请改用行内编辑。 |
|  | 属性 | hubble | icon | 指示存储为属性值的URL包含Object的图标。 |
| 已弃用 | 关系 | hubble | creatable | 允许用户从Object视图内的Linked Objects视图微件中创建特定链接类型的新Object。类型类放置在关系上，允许用户在一对多关系的“多”侧创建对象。有关支持用户创建新链接的方式，请参阅操作。 |
| 已弃用 | 属性 | hubble | endorsement_status:endorsed | 在Object Explorer和Object视图中，将Object标记为endorsed，当添加到对象类型的主键属性时。 |
| 已弃用 | 属性 | hubble | endorsement_status:not_endorsed | 在Object Explorer和Object视图中，将Object标记为工作进展中，当添加到对象类型的主键属性时。 |
| 已弃用 | 属性 | hubble | thumbnail | 使用存储为属性值的URL作为搜索结果卡片中的缩略图。这仅在之前的Object Explorer版本中相关。 |
| 已弃用 | 属性 | hubble | array | 此类型类以前用于确保属性格式化为数组，但数组现在在Ontology管理器中被正确支持为属性基本类型。 |
| 已弃用 | 属性 | hubble | default_sort_descending | 会自动在Object Explorer中按降序排序列。这仅在之前的Object Explorer版本中相关。 |
| 已弃用 | 属性 | hubble | quick_filter | 在Object Explorer列表视图中，这些属性可用作默认筛选。这仅在之前的Object Explorer版本中相关。 |
|  | 关系 | hierarchy | parent | 表示在链接类型中，链接方向代表层次结构中的父级。Object视图将在层次结构的Object视图顶部显示面包屑（例如，'Europe -> France -> Paris -> Rue Cler'）。 |
|  | 属性 | choropleth_map_config_id | <map_config_id> | 可以为包含地理区域值（即国家代码）的任何属性类型创建等值线图，这些值可以在地图上绘制。所需的类型类kind是choropleth_map_config_id，而name取决于属性包含的区域代码类型。例如：- 对于国家，使用countries- 美国州 →us_states- 美国县 →us_counties- 美国邮政编码 →us_zip_codes有关其他区域边界选项或添加此类型类的其他帮助，请联系您的Palantir代表。配置选项包括更改聚合类型以及使用的颜色比例。要使用此类型类，必须将selectable或sortable渲染提示应用于属性。 |
| 已弃用 | 属性 | oe_home_page_object_type_group | <your_object_type_group_name> | 将此类型类添加到对象类型的主键属性中，以将所述对象类型添加到一个组中。确保拼写正确以避免组重复。这些配置的对象类型组显示在Object Explorer的主页上。如果您配置了组，任何未添加到组的非隐藏对象类型将被放置在页面底部的“其他”组下。这已被对象类型组功能所取代。 |
|  | 操作类型 | hubble-oe | hide-action | 隐藏Object Explorer和Object视图中的操作类型；否则它们会自动在操作按钮下拉菜单中被发现。 |
|  | 操作类型 | hubble-oe-object-set-rid | <object_type_RID> | 实验性功能，允许创建动态对象集。 |
|  | 操作类型 | hubble-oe-security-rid | <compass_RID> | 实验性功能，允许创建动态对象集。 |
|  | 操作类型 | actions | generate_uuid | 用UUID替换字符串参数。 |
|  | 操作类型 | actions | prefill_current_user | 用当前用户替换字符串参数。 |
|  | 操作类型 | actions | view_object_with_type | 在成功提示中显示创建/修改的Object。 |
|  | 属性 | analyzer | not_analyzed | 阻止Phonograph/Elasticsearch对属性进行词元化；用于包含破折号等标识符属性。类型类中支持的几个ES内置分析器 ↗，包括：-simple-standard-whitespace-french-japanese-arabic-combined_arabic_english |
| 已弃用 | 属性 | analyzer | not_indexed | 阻止Phonograph/Elasticsearch对属性进行索引；用于不需要可搜索或可聚合的属性。此类型类不再用于管理属性是否应被索引，因为这种功能现在由searchable渲染提示管理。 |
| 已弃用 | 属性 | multipass | user_id | 当应用于包含Multipass UID的属性时，属性将在Object Explorer和Object视图中呈现为用户的用户名（由multipass和multipass属性组成）。此类型类不再用于确保属性格式化为用户名，Multipass UID现在在Ontology管理器中的值格式化功能中支持。 |
| 已弃用 | 属性 | global | <your_property_id> | 可以被用于在将属性标记为全局。这允许通过一个公共属性筛选多个对象类型，只要这些属性在每个应通过此属性筛选的对象类型上具有相同的property_id和全局类型类。这仅在之前的Object Explorer版本中相关。 |
| 已弃用 | 属性 | geo | geojson | 表示属性包含GeoJSON数据（例如，多边形、线条等）。Map应用程序将在地图上呈现此GeoJSON。已弃用：请改用geoshape属性类型。 |
| 已弃用 | 属性 | geo | latitude | 表示属性包含在Map应用程序中使用的纬度。已弃用：请改用geohash属性类型。 |
| 已弃用 | 属性 | geo | longitude | 表示属性包含在Map应用程序中使用的经度。已弃用：请改用geohash属性类型。 |
| 在对象类型的功能页面中配置 | 属性 | geo | altitude | 表示属性包含在Map应用程序中3D模式下使用的海拔/高度（以相对于海平面的米为单位）。 |
|  | 属性 | vertex | link_merge | 对于Vertex & Vortex相关对象搜索周围，总是将此对象视为中介——此对象将不再出现在相关对象列表中，但其第二度链接将会出现，并在图表上呈现为一条边。在对象的主键上放置类型类。 |
|  | 关系 | vertex | link_merge_incoming | 与link_merge相同，但仅针对此特定关系——链接合并对象是此关系的目标/至侧。 |
|  | 关系 | vertex | link_merge_outgoing | 与link_merge相同，但仅针对此特定关系——链接合并对象是此关系的源/从侧。 |
|  | 关系 | vertex | component | 对于Vertex图表，指示链接到基对象的对象将在图表中使用。 |
|  | 属性 | vertex | component_subtype | 对于Vertex，允许比对象类型更细粒度的分组。在对象的主键上放置类型类。 |
|  | 属性 | vertex | event_intent.<intent_> | 将此设置在事件的主键属性上，以在Vertex & Vortex中使用，其中intent表示事件/警报的颜色/严重性（危险、警告、主要或成功）。例如：event_intent.danger |
|  | 属性 | vertex | event_value | 表示事件的数值的属性。 |
|  | 属性 | vertex | event_value_unit.<unit_> | 与event_value一起设置，其中unit是事件数值的度量单位。例如：event_value_unit.Kilograms |
|  | 属性 | vertex | event_property | 在Vertex & Vortex事件卡片中显示此属性。 |
|  | 属性 | vertex | min | 对于时间序列对象：当系列值低于此最小值时，Vertex将发出警报。 |
|  | 属性 | vertex | max | 对于时间序列对象：当系列值超过此最大值时，Vertex将发出警报。 |
|  | 属性 | vertex | threshold_measure.<measure_> | 对于Vertex，将此设置在对象的主键属性上以指示用于阈值的度量。例如：threshold_measure.Temperature |
|  | 属性 | vertex | threshold_high_limit | 与threshold_measure一起使用以指示哪个属性代表上阈值界限。 |
|  | 属性 | vertex | threshold_low_limit | 与threshold_measure一起使用以指示哪个属性代表下阈值界限。 |
|  | 属性 | vertex | threshold_exceed_intent.<intent_> | 在对象的主键属性上与threshold_measure一起设置，其中intent表示阈值突破的颜色/严重性（危险、警告、主要或成功）。例如：threshold_exceed_intent.danger |
|  | 属性 | vertex | key_measure.<measure_> | 列在这里的度量将在Vertex主页上显示。例如：key_measure.Temperature |
| 已弃用 | 属性 | vertex | enum_values | 对于时间序列对象：从数值到字符串值的JSON映射。类型类不再受支持。 |
| 在对象类型的功能页面中配置 | 属性 | timeseries | timeseries_id | 当应用于时间序列对象的主键时，此类型类指定该对象的系列标识符(seriesId)。该属性在所有时间序列对象中必须是全局唯一的，并且是您的对象在Quiver中可发现的唯一必需类型类。 |
| 在对象类型的功能页面中配置 | 属性 | timeseries | timeseries_measure | 指定时间序列对象度量的属性。注意：类型类timeseries.timeseries_sensor_type以前用于相同目的；这将继续有效，但使用timeseries.timeseries_measure以保持一致性。 |
| 已弃用 | 属性 | timeseries | timeseries_sensor_type | 请参阅上面的timeseries_measure。 |
| 在对象类型的功能页面中配置 | 属性 | timeseries | timeseries_units | 指定时间序列对象值单位的属性（例如，股票价格时间序列可能将美元作为值单位）。 |
| 在对象类型的功能页面中配置 | 属性 | timeseries | timeseries_internal_interpolation | 指定时间序列对象默认内部插值的属性。内部插值是Quiver在相邻数据点之间推断系列值的方式。 |
| 在对象类型的功能页面中配置 | 属性 | timeseries | timeseries_root_object_id | 指定时间序列对象根对象的属性。每个时间序列对象只能有一个根对象。 |
| 在对象类型的功能页面中配置 | 属性 | timeseries | timeseries_is_enum | 任何具有枚举值的时间序列必须设置为true的布尔属性。注意：此要求是临时的，可能会在未来更改。 |
| 在对象类型的功能页面中配置 | 属性 | timeseries | timeseries_is_deprecated | 当设置为true时，布尔属性将从Object Explorer和Object视图搜索结果中过滤出时间序列。注意：这只会在Quiver中后筛选出这些时间序列。这不会影响其他应用程序的搜索结果。 |
|  | 关系 | timeseries | parent | 描述时间序列对象与每个父级之间的链接，类似于hierarchy.parent。 |
|  | 属性 | timeseries | timeseries_is_value_inverted | 当设置为true时，此布尔属性将自动反转Quiver中时间序列的y轴值，使得值向下上升。这对于绘制时间与深度序列非常有用，例如在跟踪地下钻探操作的进展时。 |
|  | 属性 | timeseries | timeseries_depth_units | 放置在包含复杂序列（深度序列、完井序列和光纤序列）深度单位的属性上。常规的timeseries.timeseries_units属性用于深度序列和完井序列的值单位。 |
| 在对象类型的功能页面中配置 | 属性 | timeseries | event_id | 指定事件对象事件标识符（eventId）的属性。应在所有事件对象中全局唯一。 |
| 在对象类型的功能页面中配置 | 属性 | timeseries | event_start_time | 指定事件对象起始时间的属性。该字段应为时间值（例如TIMESTAMP）。 |
| 在对象类型的功能页面中配置 | 属性 | timeseries | event_end_time | 指定事件对象结束时间的属性。该字段应为时间值（例如TIMESTAMP）。 |
| 在对象类型的功能页面中配置 | 属性 | timeseries | event_description | 指定事件对象字符串描述的属性。如果事件对象类型将被用于注释数据输出，这是必需的。 |
| 在对象类型的功能页面中配置 | 属性 | timeseries | event_root_object_id | 指定事件对象根对象的属性。每个事件对象只能有一个根对象。 |
| 在对象类型的功能页面中配置 | 属性 | timeseries | event_linked_series_id | 指定事件对象关联的系列对象的属性。支持字符串数组和单个字符串。 |