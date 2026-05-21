# Ontology 操作

> 来源: https://www.palantir.com/docs/zh/foundry/map/integrate-actions/

注意：以下翻译的准确性尚未经过验证。这是使用AIP ↗从原始英文文本进行的机器翻译。

# Ontology 操作

您可以在 Ontology 中配置操作，以便用户可以在地图应用中应用于地理空间对象。例如，这些操作可能是基于选定的点、绘制的多边形或线条来创建或编辑对象。

## 点操作

当用户右键单击地图或点对象时，操作菜单将显示适用于地理空间点的所有 Ontology 操作。要定义适用于点的操作，需要具备以下之一：

- 一个字符串参数，类型类为：Kind:geoValue:geohash（数据将是纬度，经度的字符串），或

- 两个Double参数：一个传递纬度的，类型类为：Kind:geoValue:latitude，以及一个传递经度的，类型类为：Kind:geoValue:longitude。

## 形状操作

当用户选择一个多边形对象或在地图上绘制一个形状时，操作菜单将显示适用于地理空间形状的所有 Ontology 操作。要定义适用于形状的操作，该操作需要有一个字符串参数，类型类为：Kind:geo和 Value:geojson，其中数据将是一个 GeoJSON 几何字符串。

## 使用操作编辑对象geoshape属性

操作可以被配置为允许用户编辑地图上对象的geoshape属性。用户可以选择对象，从操作菜单中选择相关操作，然后根据需要修改形状（例如，通过添加或移动点、缓冲或平移形状）。

要配置一个操作以允许用户编辑地图上对象的geoshape属性，为所需的对象类型创建一个“修改对象”操作，并具有满足以下要求的参数：

- 是一个字符串参数
- 映射到您希望更新的对象上的geoshape属性
- 默认值禁用
- 类型类为：Kind:geo, Value:geojson
- 类型类为：Kind:geo, Value:prefill