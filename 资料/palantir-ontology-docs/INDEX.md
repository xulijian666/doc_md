# Palantir Foundry Ontology 完整文档索引

> 来源: https://www.palantir.com/docs/zh/foundry/ontology/overview
> 共 210 个页面 | 爬取时间: 2026-05-20
> 格式: Markdown (适合 AI embedding/RAG 检索)

## 概述

Palantir Ontology 是 Palantir Foundry 平台的核心语义层，将底层数据集映射为业务语义对象(Objects)、属性(Properties)、链接(Links)，并通过操作(Actions)和函数(Functions)赋予动力，支撑 Workshop、Object Explorer、Vertex 等上层应用。本质是组织的"数字孪生"中间层。

---

## 1. Ontology 核心概念

| 文件 | 说明 |
|------|------|
| [ontology_overview.md](ontology_overview.md) | Ontology 搭建总览 |
| [ontology_why-ontology.md](ontology_why-ontology.md) | 为什么创建 Ontology |
| [ontology_models.md](ontology_models.md) | Ontology 中的模型 |
| [ontology_core-concepts.md](ontology_core-concepts.md) | 核心概念 |
| [ontology_applications.md](ontology_applications.md) | 基于 Ontology 的应用程序 |

## 2. Ontology 资源占用

| 文件 | 说明 |
|------|------|
| [ontologies_volume-usage.md](ontologies_volume-usage.md) | Ontology 占用量 |
| [ontologies_compute-usage.md](ontologies_compute-usage.md) | 计算使用：Ontology 索引 |
| [ontologies_query-compute-usage.md](ontologies_query-compute-usage.md) | 使用 Ontology 查询计算使用情况 |

## 3. Object 类型

| 文件 | 说明 |
|------|------|
| [object-link-types_object-types-overview.md](object-link-types_object-types-overview.md) | Object 类型概览 |
| [object-link-types_create-object-type.md](object-link-types_create-object-type.md) | 创建 Object 类型 |
| [object-link-types_edit-object-type.md](object-link-types_edit-object-type.md) | 编辑 Object 类型 |
| [object-link-types_copy-object-type-config.md](object-link-types_copy-object-type-config.md) | 选择要复制的 Object 类型 |
| [object-link-types_enable-gotham-integration.md](object-link-types_enable-gotham-integration.md) | 通过类型映射启用 Gotham 集成 |
| [object-link-types_object-type-metadata.md](object-link-types_object-type-metadata.md) | Object 类型元数据参考 |

## 4. 属性 (Properties)

| 文件 | 说明 |
|------|------|
| [object-link-types_properties-overview.md](object-link-types_properties-overview.md) | 属性概览 |
| [object-link-types_edit-properties.md](object-link-types_edit-properties.md) | 编辑 Object 类型属性 |
| [object-link-types_value-formatting.md](object-link-types_value-formatting.md) | 支持的值格式化 |
| [object-link-types_conditional-formatting.md](object-link-types_conditional-formatting.md) | 添加条件格式化 |
| [object-link-types_property-metadata.md](object-link-types_property-metadata.md) | 属性元数据参考 |
| [object-link-types_edit-only-properties.md](object-link-types_edit-only-properties.md) | 仅编辑属性 |
| [object-link-types_required-properties.md](object-link-types_required-properties.md) | 必填属性 |

## 5. 共享属性 (Shared Properties)

| 文件 | 说明 |
|------|------|
| [object-link-types_shared-property-overview.md](object-link-types_shared-property-overview.md) | 共享属性概述 |
| [object-link-types_create-shared-property.md](object-link-types_create-shared-property.md) | 创建共享属性 |
| [object-link-types_edit-shared-property.md](object-link-types_edit-shared-property.md) | 编辑共享属性 |
| [object-link-types_use-shared-property.md](object-link-types_use-shared-property.md) | 在对象类型上使用共享属性 |
| [object-link-types_shared-property-metadata.md](object-link-types_shared-property-metadata.md) | 共享属性元数据参考 |

## 6. 链接类型 (Link Types)

| 文件 | 说明 |
|------|------|
| [object-link-types_link-types-overview.md](object-link-types_link-types-overview.md) | 链接类型概述 |
| [object-link-types_create-link-type.md](object-link-types_create-link-type.md) | 创建链接类型 |
| [object-link-types_edit-link-types.md](object-link-types_edit-link-types.md) | 编辑链接类型 |
| [object-link-types_link-type-metadata.md](object-link-types_link-type-metadata.md) | 链接类型元数据参考 |

## 7. 值类型 (Value Types)

| 文件 | 说明 |
|------|------|
| [object-link-types_value-types-overview.md](object-link-types_value-types-overview.md) | 值类型概述 |
| [object-link-types_create-value-type.md](object-link-types_create-value-type.md) | 创建值类型 |
| [object-link-types_use-value-type.md](object-link-types_use-value-type.md) | 使用值类型 |
| [object-link-types_value-types-versions.md](object-link-types_value-types-versions.md) | 值类型版本 |
| [object-link-types_value-types-permissions.md](object-link-types_value-types-permissions.md) | 值类型权限 |
| [object-link-types_value-type-constraints.md](object-link-types_value-type-constraints.md) | 值类型约束 |

## 8. 结构属性 (Struct Types)

| 文件 | 说明 |
|------|------|
| [object-link-types_structs-overview.md](object-link-types_structs-overview.md) | 结构属性概述 |
| [object-link-types_create-struct-type.md](object-link-types_create-struct-type.md) | 创建结构属性类型 |
| [object-link-types_edit-struct-type.md](object-link-types_edit-struct-type.md) | 编辑结构属性类型 |
| [object-link-types_struct-automapping.md](object-link-types_struct-automapping.md) | 自动映射结构属性 |
| [object-link-types_struct-shared-properties.md](object-link-types_struct-shared-properties.md) | 结构属性和共享属性类型 |

## 9. 元数据 (Metadata)

| 文件 | 说明 |
|------|------|
| [object-link-types_metadata-typeclasses.md](object-link-types_metadata-typeclasses.md) | 类型类 |
| [object-link-types_metadata-render-hints.md](object-link-types_metadata-render-hints.md) | 渲染提示 |
| [object-link-types_metadata-statuses.md](object-link-types_metadata-statuses.md) | 状态 |

## 10. 操作类型 - 参数 (Action Parameters)

| 文件 | 说明 |
|------|------|
| [action-types_parameter-overview.md](action-types_parameter-overview.md) | 参数概述 |
| [action-types_parameters-default-value.md](action-types_parameters-default-value.md) | 设置参数默认值 |
| [action-types_parameters-filter.md](action-types_parameters-filter.md) | 筛选参数下拉菜单的结果 |
| [action-types_dropdown-security.md](action-types_dropdown-security.md) | 对象下拉菜单安全注意事项 |
| [action-types_parameters-override.md](action-types_parameters-override.md) | 覆盖 |

## 11. 操作类型 - 函数操作 (Function Actions)

| 文件 | 说明 |
|------|------|
| [action-types_function-actions-overview.md](action-types_function-actions-overview.md) | 函数操作概述 |
| [action-types_function-actions-getting-started.md](action-types_function-actions-getting-started.md) | 函数操作入门 |

## 12. 操作类型 - 副作用 (Side Effects)

| 文件 | 说明 |
|------|------|
| [action-types_side-effects-overview.md](action-types_side-effects-overview.md) | 副作用概述 |
| [action-types_notifications.md](action-types_notifications.md) | 通知 |
| [action-types_set-up-notification.md](action-types_set-up-notification.md) | 设置通知 |
| [action-types_webhooks.md](action-types_webhooks.md) | Webhooks |
| [action-types_set-up-webhook.md](action-types_set-up-webhook.md) | 设置 Webhook |

## 13. 函数 - TypeScript

| 文件 | 说明 |
|------|------|
| [functions_input-output-types.md](functions_input-output-types.md) | 输入和输出类型 |
| [functions_decorators.md](functions_decorators.md) | 装饰器 |
| [functions_undefined-values.md](functions_undefined-values.md) | 处理未定义值 |
| [functions_debug.md](functions_debug.md) | 调试函数 |
| [functions_add-dependencies.md](functions_add-dependencies.md) | 添加 npm 依赖项 |

## 14. 函数 - Python

| 文件 | 说明 |
|------|------|
| [functions_python-getting-started.md](functions_python-getting-started.md) | Python 函数起始步骤 |
| [functions_python-function-types.md](functions_python-function-types.md) | 类型参考 |
| [functions_python-functions-on-objects.md](functions_python-functions-on-objects.md) | 对象上的函数 |
| [functions_python-functions-api-calls.md](functions_python-functions-api-calls.md) | 从 Python 函数进行 API 调用 |
| [functions_python-ontology-edits.md](functions_python-ontology-edits.md) | Ontology 更改 |
| [functions_python-functions-builder.md](functions_python-functions-builder.md) | 在 Pipeline Builder 中使用 Python 函数 |
| [functions_python-functions-workshop.md](functions_python-functions-workshop.md) | 在 Workshop 中使用 Python 函数 |
| [functions_python-functions-advanced-usage.md](functions_python-functions-advanced-usage.md) | 高级用法 |

## 15. 函数 - 对象上的函数 (Functions on Objects)

| 文件 | 说明 |
|------|------|
| [functions_functions-on-objects.md](functions_functions-on-objects.md) | 概述 |
| [functions_foo-getting-started.md](functions_foo-getting-started.md) | 入门 |
| [functions_object-identifiers.md](functions_object-identifiers.md) | Object 标识符 |
| [functions_create-custom-aggregation.md](functions_create-custom-aggregation.md) | 创建自定义聚合 |
| [functions_ontology-imports.md](functions_ontology-imports.md) | 导入 Object 和链接类型 |
| [functions_api-objects-links.md](functions_api-objects-links.md) | API: Object 和链接 |
| [functions_api-object-sets.md](functions_api-object-sets.md) | API: 对象集 |
| [functions_api-attachments.md](functions_api-attachments.md) | API: 附件 |
| [functions_api-media.md](functions_api-media.md) | API: 媒体 |

## 16. 函数 - 语义搜索 (Semantic Search)

| 文件 | 说明 |
|------|------|
| [functions_overview-semantic-search.md](functions_overview-semantic-search.md) | 语义搜索概述 |
| [functions_using-palantir-provided-models-to-create-a-semantic-search-workflow.md](functions_using-palantir-provided-models-to-create-a-semantic-search-workflow.md) | 使用 Palantir 模型创建语义搜索 |
| [functions_using-custom-models-to-create-a-semantic-search-workflow.md](functions_using-custom-models-to-create-a-semantic-search-workflow.md) | 使用自定义模型创建语义搜索 |
| [functions_chunking.md](functions_chunking.md) | 分块 |
| [functions_pdf-handling.md](functions_pdf-handling.md) | PDF 处理 |

## 17. 函数 - Ontology 编辑

| 文件 | 说明 |
|------|------|
| [functions_edits-overview.md](functions_edits-overview.md) | Ontology 编辑概述 |
| [functions_edits-generate-id.md](functions_edits-generate-id.md) | 为新 Objects 生成唯一 ID |
| [functions_user-facing-error.md](functions_user-facing-error.md) | 抛出用户界面错误 |
| [functions_api-ontology-edits.md](functions_api-ontology-edits.md) | API: Ontology 编辑 |
| [functions_query-functions.md](functions_query-functions.md) | 查询函数 |
| [functions_model-functions.md](functions_model-functions.md) | 创建模型函数 |

## 18. 函数 - 单元测试

| 文件 | 说明 |
|------|------|
| [functions_unit-test-getting-started.md](functions_unit-test-getting-started.md) | 单元测试入门指南 |
| [functions_unit-test-stub-objects.md](functions_unit-test-stub-objects.md) | 创建存根对象 |
| [functions_unit-test-ontology-edits.md](functions_unit-test-ontology-edits.md) | 验证 Ontology 编辑 |
| [functions_unit-test-object-searches.md](functions_unit-test-object-searches.md) | 存根对象搜索和聚合 |
| [functions_unit-test-dates-timestamps.md](functions_unit-test-dates-timestamps.md) | 模拟日期、时间戳和 UUID |
| [functions_unit-test-users-groups.md](functions_unit-test-users-groups.md) | 模拟用户和组 |
| [functions_unit-test-debugging.md](functions_unit-test-debugging.md) | 调试 |
| [functions_enforced-limits.md](functions_enforced-limits.md) | 强制限制 |
| [functions_optimize-performance.md](functions_optimize-performance.md) | 优化性能 |

## 19. 接口 (Interfaces / Logic)

| 文件 | 说明 |
|------|------|
| [logic_evaluations-overview.md](logic_evaluations-overview.md) | 评估概述 |
| [logic_evaluations-getting-started.md](logic_evaluations-getting-started.md) | 评估入门 |
| [logic_evaluations-create-suite.md](logic_evaluations-create-suite.md) | 创建评估套件 |
| [logic_evaluations-metrics-dashboard.md](logic_evaluations-metrics-dashboard.md) | 评估指标仪表盘 |

## 20. Object Explorer

| 文件 | 说明 |
|------|------|
| [object-explorer_search-objects.md](object-explorer_search-objects.md) | 搜索 Objects |
| [object-explorer_search-syntax.md](object-explorer_search-syntax.md) | 搜索语法 |
| [object-explorer_filter-results.md](object-explorer_filter-results.md) | 筛选结果 |
| [object-explorer_explore-charts.md](object-explorer_explore-charts.md) | 使用图表进行探索 |
| [object-explorer_view-results.md](object-explorer_view-results.md) | 查看结果 |
| [object-explorer_pivot-linked.md](object-explorer_pivot-linked.md) | 通过旋转探索关联对象 |
| [object-explorer_compare-object-sets.md](object-explorer_compare-object-sets.md) | 比较对象集 |
| [object-explorer_save-explorations.md](object-explorer_save-explorations.md) | 保存探索 |
| [object-explorer_save-lists.md](object-explorer_save-lists.md) | 保存列表 |
| [object-explorer_apply-actions.md](object-explorer_apply-actions.md) | 应用操作 |

## 21. Object Monitor

| 文件 | 说明 |
|------|------|
| [object-monitors_monitor.md](object-monitors_monitor.md) | 监控 |
| [object-monitors_input.md](object-monitors_input.md) | 输入 |
| [object-monitors_condition.md](object-monitors_condition.md) | 条件 |
| [object-monitors_evaluation.md](object-monitors_evaluation.md) | 评估 |
| [object-monitors_activity.md](object-monitors_activity.md) | 活动 |
| [object-monitors_notifications.md](object-monitors_notifications.md) | 通知 |
| [object-monitors_actions.md](object-monitors_actions.md) | 操作 |

## 22. Object 视图 (Object Views)

| 文件 | 说明 |
|------|------|
| [object-views_config-overview.md](object-views_config-overview.md) | Object 视图概述 |
| [object-views_config-tabs.md](object-views_config-tabs.md) | 配置标签页 |
| [object-views_config-workshop-tabs.md](object-views_config-workshop-tabs.md) | 配置 Workshop 标签页 |
| [object-views_config-widgets.md](object-views_config-widgets.md) | 配置微件（旧版） |
| [object-views_config-app-sidebar.md](object-views_config-app-sidebar.md) | 配置应用程序侧边栏 |
| [object-views_config-profiles.md](object-views_config-profiles.md) | 配置配置文件 |
| [object-views_manage-versions.md](object-views_manage-versions.md) | 管理 Object 视图版本 |
| [object-views_widgets-properties-links.md](object-views_widgets-properties-links.md) | 属性和链接微件 |
| [object-views_widgets-visualization.md](object-views_widgets-visualization.md) | 可视化微件 |
| [object-views_widgets-filtering.md](object-views_widgets-filtering.md) | 筛选微件 |
| [object-views_widgets-layout.md](object-views_widgets-layout.md) | 设计/布局 |
| [object-views_widgets-apps-files.md](object-views_widgets-apps-files.md) | 应用程序和文件微件 |

## 23. Ontology 管理器

| 文件 | 说明 |
|------|------|
| [ontology-manager_save-changes.md](ontology-manager_save-changes.md) | 保存对 Ontology 的更改 |
| [ontology-manager_restore-changes.md](ontology-manager_restore-changes.md) | 审查和恢复更改 |

## 24. Vertex - 图分析

| 文件 | 说明 |
|------|------|
| [vertex_graphs-explore.md](vertex_graphs-explore.md) | 探索现有图表 |
| [vertex_explore-object-relationships.md](vertex_explore-object-relationships.md) | 探索 Object 关系 |
| [vertex_graphs-display-options.md](vertex_graphs-display-options.md) | Object 和边显示选项 |
| [vertex_save-share.md](vertex_save-share.md) | 保存、共享和协作 |
| [vertex_graphs-template.md](vertex_graphs-template.md) | 创建图模板 |
| [vertex_generate-graph-apps.md](vertex_generate-graph-apps.md) | 从其他应用生成图表 |
| [vertex_generate-graph-functions.md](vertex_generate-graph-functions.md) | 使用函数生成图表 |
| [vertex_derive-property-functions.md](vertex_derive-property-functions.md) | 使用函数派生属性 |
| [vertex_embed-graph-workshop.md](vertex_embed-graph-workshop.md) | 在 Workshop 模块中嵌入图形 |
| [vertex_read-only-mode.md](vertex_read-only-mode.md) | 只读模式 |

## 25. Vertex - 事件与时间序列

| 文件 | 说明 |
|------|------|
| [vertex_events-overview.md](vertex_events-overview.md) | 事件概述 |
| [vertex_configure-events.md](vertex_configure-events.md) | 配置事件 |
| [vertex_explore-related-events.md](vertex_explore-related-events.md) | 探索相关事件 |
| [vertex_explore-time-series.md](vertex_explore-time-series.md) | 探索相关时间序列 |
| [vertex_use-time-selection.md](vertex_use-time-selection.md) | 使用时间选择 |
| [vertex_configure-thresholds.md](vertex_configure-thresholds.md) | 配置阈值 |
| [vertex_timeline.md](vertex_timeline.md) | 查看和筛选时间轴上的事件 |

## 26. Vertex - 场景 (Scenarios)

| 文件 | 说明 |
|------|------|
| [vertex_scenarios-overview.md](vertex_scenarios-overview.md) | 场景概览 |
| [vertex_scenarios-getting-started.md](vertex_scenarios-getting-started.md) | 场景入门指南 |
| [vertex_scenarios-options.md](vertex_scenarios-options.md) | 场景选项 |
| [vertex_chained-models.md](vertex_chained-models.md) | 配置链式模型 |
| [vertex_vertex-settings-control-panel.md](vertex_vertex-settings-control-panel.md) | 在控制面板中配置 Vertex 设置 |
| [vertex_link-merging.md](vertex_link-merging.md) | 配置链接合并 |

## 27. Foundry Rules - 核心概念

| 文件 | 说明 |
|------|------|
| [foundry-rules_core-concepts.md](foundry-rules_core-concepts.md) | Foundry Rules 概述 |
| [foundry-rules_object-model.md](foundry-rules_object-model.md) | Object 模型 |
| [foundry-rules_workshop-application.md](foundry-rules_workshop-application.md) | Workshop 应用 |
| [foundry-rules_rule-logic.md](foundry-rules_rule-logic.md) | 规则逻辑 |
| [foundry-rules_foundry-rules-workflow-configuration.md](foundry-rules_foundry-rules-workflow-configuration.md) | 工作流配置 |

## 28. Foundry Rules - 部署与配置

| 文件 | 说明 |
|------|------|
| [foundry-rules_deploy-foundry-rules.md](foundry-rules_deploy-foundry-rules.md) | 部署 Foundry Rules |
| [foundry-rules_deploy-workflow.md](foundry-rules_deploy-workflow.md) | 部署工作流 |
| [foundry-rules_configure-workflow.md](foundry-rules_configure-workflow.md) | 配置工作流 |
| [foundry-rules_author-and-run-a-rule.md](foundry-rules_author-and-run-a-rule.md) | 编写并运行规则 |

## 29. Foundry Rules - 定制

| 文件 | 说明 |
|------|------|
| [foundry-rules_customization.md](foundry-rules_customization.md) | 定制 Foundry Rules |
| [foundry-rules_enable-optional-features.md](foundry-rules_enable-optional-features.md) | 启用非必填功能 |
| [foundry-rules_add-a-custom-property.md](foundry-rules_add-a-custom-property.md) | 添加自定义属性 |
| [foundry-rules_rule-permissions.md](foundry-rules_rule-permissions.md) | 编辑规则的权限 |
| [foundry-rules_permitted-and-default-output-values.md](foundry-rules_permitted-and-default-output-values.md) | 允许和默认输出值 |
| [foundry-rules_customize-foundry-rules-pipeline.md](foundry-rules_customize-foundry-rules-pipeline.md) | 自定义流水线 |

## 30. Foundry Rules - 时间序列

| 文件 | 说明 |
|------|------|
| [foundry-rules_timeseries-concepts.md](foundry-rules_timeseries-concepts.md) | 时间序列规则 |
| [foundry-rules_deploy-timeseries-foundry-rules.md](foundry-rules_deploy-timeseries-foundry-rules.md) | 部署时间序列规则 |
| [foundry-rules_configure-timeseries-foundry-rules.md](foundry-rules_configure-timeseries-foundry-rules.md) | 配置时间序列 |

## 31. Foundry Rules - 迁移与高级配置

| 文件 | 说明 |
|------|------|
| [foundry-rules_legacy-foundry-rules-setup-taurus.md](foundry-rules_legacy-foundry-rules-setup-taurus.md) | 旧版设置 (Taurus) |
| [foundry-rules_migrate-to-foundry-rules.md](foundry-rules_migrate-to-foundry-rules.md) | 迁移到 Foundry Rules |
| [foundry-rules_configure-workshop-app.md](foundry-rules_configure-workshop-app.md) | 配置 Workshop 应用程序 |
| [foundry-rules_configure-transforms-pipeline.md](foundry-rules_configure-transforms-pipeline.md) | 配置变换管道 |
| [foundry-rules_configure-rule-actions.md](foundry-rules_configure-rule-actions.md) | 配置规则操作 |
| [foundry-rules_upgrade-to-use-rule-actions.md](foundry-rules_upgrade-to-use-rule-actions.md) | 升级以使用规则操作 |

## 32. 地图 - 基础操作

| 文件 | 说明 |
|------|------|
| [map_map-overview.md](map_map-overview.md) | 地图界面概述 |
| [map_create-save-maps.md](map_create-save-maps.md) | 创建、保存和导出地图 |
| [map_add-to-map.md](map_add-to-map.md) | 将数据添加到地图 |
| [map_layer-management.md](map_layer-management.md) | 图层管理 |
| [map_navigation.md](map_navigation.md) | 导航 |
| [map_selection.md](map_selection.md) | 选择 |
| [map_annotations.md](map_annotations.md) | 注释 |
| [map_shapes.md](map_shapes.md) | 形状 |
| [map_histogram.md](map_histogram.md) | 直方图 |
| [map_actions.md](map_actions.md) | 操作 |

## 33. 地图 - 时间与事件

| 文件 | 说明 |
|------|------|
| [map_time-overview.md](map_time-overview.md) | 地图中的时间和时间数据 |
| [map_time-selection.md](map_time-selection.md) | 时间选择 |
| [map_timeline.md](map_timeline.md) | 时间轴 |
| [map_events.md](map_events.md) | 事件 |
| [map_time-series.md](map_time-series.md) | 时间序列 |

## 34. 地图 - 可视化 Object

| 文件 | 说明 |
|------|------|
| [map_visualize-objects.md](map_visualize-objects.md) | 可视化概述 |
| [map_visualize-points.md](map_visualize-points.md) | 点几何图形 |
| [map_visualize-polygons-lines.md](map_visualize-polygons-lines.md) | 多边形和线几何图形 |
| [map_visualize-tracks.md](map_visualize-tracks.md) | 轨迹几何 |
| [map_objects-high-scale.md](map_objects-high-scale.md) | 显示高规模对象数据 |

## 35. 地图 - Ontology 集成

| 文件 | 说明 |
|------|------|
| [map_integrate-objects.md](map_integrate-objects.md) | Ontology Object 集成 |
| [map_integrate-searcharound-functions.md](map_integrate-searcharound-functions.md) | 地图搜索周围函数 |
| [map_integrate-actions.md](map_integrate-actions.md) | Ontology 操作集成 |
| [map_layer-editor.md](map_layer-editor.md) | 地图图层编辑器 |
| [map_templates.md](map_templates.md) | 地图模板 |
| [map_widget.md](map_widget.md) | 在 Workshop 模块中嵌入地图模板 |
| [map_settings.md](map_settings.md) | 地图设置 |
| [map_control-panel.md](map_control-panel.md) | 控制面板 |

## 36. 动态调度

| 文件 | 说明 |
|------|------|
| [dynamic-scheduling_scheduling-calendar-overview.md](dynamic-scheduling_scheduling-calendar-overview.md) | 日程安排日历微件 |
| [dynamic-scheduling_scheduling-calendar-widget.md](dynamic-scheduling_scheduling-calendar-widget.md) | 微件配置 |
