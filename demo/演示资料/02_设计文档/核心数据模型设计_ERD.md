---
文档编号: ERD-CORE-2026-001
版本: V3.0
编制人: 张伟（架构师）
编制日期: 2026-03-15
文档类型: 数据模型设计
业务域: 保险-核心系统
tags:
  - 数据模型
  - ERD
  - 核心系统
---

# 核心数据模型设计 (ERD)

| 项目 | 内容 |
|------|------|
| 文档编号 | ERD-CORE-2026-001 |
| 版本 | V3.0 |
| 编制日期 | 2026-03-15 |
| 编制人 | 张伟（架构师） |
| 数据库 | MySQL 8.0 / TiDB（分析库） |

---

## 1. 实体关系总览

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ Customer │───▶│ Proposal │───▶│  Policy  │───▶│ Coverage │
│  客户    │    │  投保单  │    │  保单    │    │  保障项  │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
                    │                │
                    ▼                ▼
              ┌──────────┐    ┌──────────┐
              │Underwrite│    │  Claim   │
              │  核保记录│    │  理赔案  │
              └──────────┘    └──────────┘
                    │                │
                    ▼                ▼
              ┌──────────┐    ┌──────────┐
              │  Payment │    │  ClaimPay│
              │  支付记录│    │  赔付记录│
              └──────────┘    └──────────┘

┌──────────┐    ┌──────────┐    ┌──────────┐
│  Product │───▶│ Coverage │───▶│  Rating  │
│  产品    │    │  保障定义│    │  费率表  │
└──────────┘    └──────────┘    └──────────┘

┌──────────┐    ┌──────────┐
│  User    │───▶│  Agent   │
│  用户    │    │  代理人  │
└──────────┘    └──────────┘
```

## 2. 核心实体定义

### 2.1 客户表 (t_customer)

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | bigint | PK | 主键 |
| customer_no | varchar(32) | UK | 客户编号 |
| customer_type | tinyint | 是 | 1-个人 2-企业 |
| name | varchar(100) | 是 | 客户姓名/企业名称 |
| id_type | varchar(20) | 是 | 证件类型 |
| id_number | varchar(50) | 是 | 证件号（加密存储） |
| mobile | varchar(20) | 是 | 手机号（加密存储） |
| email | varchar(100) | 否 | 邮箱 |
| address | varchar(500) | 否 | 联系地址 |
| gender | tinyint | 否 | 1-男 2-女 |
| birthday | date | 否 | 出生日期 |
| occupation | varchar(50) | 否 | 职业 |
| risk_level | tinyint | 否 | 风险等级 1-5 |
| status | tinyint | 是 | 1-正常 2-冻结 3-注销 |
| created_at | datetime | 是 | 创建时间 |
| updated_at | datetime | 是 | 更新时间 |

**索引：**
- UK: customer_no
- UK: id_type + id_number
- IDX: mobile
- IDX: name

### 2.2 产品表 (t_product)

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | bigint | PK | 主键 |
| product_code | varchar(32) | UK | 产品编码 |
| product_name | varchar(200) | 是 | 产品名称 |
| product_type | varchar(20) | 是 | CAR/HEALTH/LIFE/PROPERTY |
| category | varchar(20) | 是 | 主险/附加险 |
| status | tinyint | 是 | 1-在售 2-停售 3-开发中 |
| effective_date | date | 是 | 生效日期 |
| expire_date | date | 否 | 停售日期 |
| min_age | int | 否 | 最小投保年龄 |
| max_age | int | 否 | 最大投保年龄 |
| description | text | 否 | 产品说明 |
| created_at | datetime | 是 | 创建时间 |

### 2.3 保障项定义表 (t_coverage_def)

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | bigint | PK | 主键 |
| coverage_code | varchar(32) | UK | 保障项编码 |
| coverage_name | varchar(100) | 是 | 保障项名称 |
| product_id | bigint | FK | 关联产品 |
| coverage_type | varchar(20) | 是 | 身故/医疗/重疾/伤残 |
| calculation_type | varchar(20) | 是 | 定额/比例/实报实销 |
| min_amount | decimal(15,2) | 否 | 最低保额 |
| max_amount | decimal(15,2) | 否 | 最高保额 |
| deductible | decimal(15,2) | 否 | 免赔额 |
| reimbursement_rate | decimal(5,4) | 否 | 赔付比例 |

### 2.4 费率表 (t_rating)

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | bigint | PK | 主键 |
| coverage_id | bigint | FK | 关联保障项 |
| rate_table_code | varchar(32) | UK | 费率表编码 |
| age_min | int | 是 | 年龄下限 |
| age_max | int | 是 | 年龄上限 |
| gender | tinyint | 否 | 0-不限 1-男 2-女 |
| base_rate | decimal(10,6) | 是 | 基础费率 |
| effective_date | date | 是 | 生效日期 |
| status | tinyint | 是 | 1-有效 2-失效 |

### 2.5 投保单表 (t_proposal)

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | bigint | PK | 主键 |
| proposal_no | varchar(32) | UK | 投保单号 |
| product_id | bigint | FK | 关联产品 |
| customer_id | bigint | FK | 投保人 |
| channel_code | varchar(32) | 是 | 渠道编码 |
| status | varchar(20) | 是 | 状态 |
| total_premium | decimal(15,2) | 是 | 总保费 |
| effective_date | date | 是 | 生效日期 |
| expire_date | date | 是 | 失效日期 |
| quote_no | varchar(32) | 否 | 关联报价单号 |
| underwrite_result | varchar(20) | 否 | 核保结论 |
| underwrite_time | datetime | 否 | 核保时间 |
| payment_status | varchar(20) | 否 | 支付状态 |
| policy_no | varchar(32) | 否 | 出单后关联保单号 |
| created_at | datetime | 是 | 创建时间 |
| updated_at | datetime | 是 | 更新时间 |

**状态流转：**
```
DRAFT → QUOTED → SUBMITTED → UNDERWRITING → APPROVED → PAID → ISSUED
                                                ↓
                                           REJECTED
```

### 2.6 保单表 (t_policy)

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | bigint | PK | 主键 |
| policy_no | varchar(32) | UK | 保单号 |
| proposal_no | varchar(32) | UK | 投保单号 |
| product_id | bigint | FK | 产品 |
| customer_id | bigint | FK | 投保人 |
| status | varchar(20) | 是 | EFFECTIVE/LAPSED/SURRENDERED |
| total_premium | decimal(15,2) | 是 | 总保费 |
| paid_premium | decimal(15,2) | 是 | 已缴保费 |
| cash_value | decimal(15,2) | 否 | 现金价值（寿险） |
| effective_date | date | 是 | 生效日期 |
| expire_date | date | 是 | 失效日期 |
| issue_date | date | 是 | 出单日期 |
| pdf_url | varchar(500) | 否 | 电子保单URL |
| created_at | datetime | 是 | 创建时间 |
| updated_at | datetime | 是 | 更新时间 |

### 2.7 投保人/被保险人关联表 (t_policy_person)

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | bigint | PK | 主键 |
| policy_id | bigint | FK | 保单ID |
| customer_id | bigint | FK | 客户ID |
| role_type | varchar(20) | 是 | APPLICANT/INSURED/BENEFICIARY |
| relation | varchar(20) | 否 | 与投保人关系 |
| beneficiary_ratio | decimal(5,2) | 否 | 受益比例 |

### 2.8 保障项实例表 (t_policy_coverage)

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | bigint | PK | 主键 |
| policy_id | bigint | FK | 保单ID |
| coverage_def_id | bigint | FK | 保障项定义ID |
| insured_amount | decimal(15,2) | 是 | 保额 |
| premium | decimal(15,2) | 是 | 该项保费 |
| deductible | decimal(15,2) | 否 | 免赔额 |
| effective_date | date | 是 | 生效日期 |
| expire_date | date | 是 | 失效日期 |

### 2.9 理赔案件表 (t_claim)

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | bigint | PK | 主键 |
| claim_no | varchar(32) | UK | 案件号 |
| policy_id | bigint | FK | 保单ID |
| insured_id | bigint | FK | 出险人ID |
| accident_date | date | 是 | 出险日期 |
| accident_type | varchar(20) | 是 | DISEASE/ACCIDENT |
| hospital_code | varchar(32) | 是 | 医院编码 |
| diagnosis | varchar(200) | 是 | 诊断 |
| diagnosis_code | varchar(20) | 是 | ICD-10编码 |
| status | varchar(20) | 是 | 案件状态 |
| claim_amount | decimal(15,2) | 否 | 报案金额 |
| approved_amount | decimal(15,2) | 否 | 核定金额 |
| payable_amount | decimal(15,2) | 否 | 应付金额 |
| paid_amount | decimal(15,2) | 否 | 已付金额 |
| report_time | datetime | 是 | 报案时间 |
| review_time | datetime | 否 | 审核时间 |
| pay_time | datetime | 否 | 支付时间 |
| created_at | datetime | 是 | 创建时间 |

### 2.10 支付记录表 (t_payment)

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | bigint | PK | 主键 |
| payment_no | varchar(32) | UK | 支付单号 |
| order_no | varchar(32) | 是 | 关联业务单号 |
| order_type | varchar(20) | 是 | PREMIUM/REFUND/CLAIM |
| amount | decimal(15,2) | 是 | 金额 |
| payment_method | varchar(20) | 是 | 支付方式 |
| channel_txn_id | varchar(64) | 否 | 渠道交易号 |
| status | varchar(20) | 是 | PENDING/SUCCESS/FAILED |
| paid_time | datetime | 否 | 支付时间 |
| created_at | datetime | 是 | 创建时间 |

## 3. 分析库表设计（TiDB）

### 3.1 保费统计宽表 (d_premium_daily)

| 字段 | 类型 | 说明 |
|------|------|------|
| stat_date | date | 统计日期 |
| product_code | varchar(32) | 产品编码 |
| channel_code | varchar(32) | 渠道编码 |
| region_code | varchar(10) | 地区编码 |
| proposal_count | int | 投保单数 |
| policy_count | int | 出单数 |
| premium_amount | decimal(15,2) | 保费金额 |
| avg_premium | decimal(10,2) | 件均保费 |

### 3.2 理赔统计宽表 (d_claim_daily)

| 字段 | 类型 | 说明 |
|------|------|------|
| stat_date | date | 统计日期 |
| product_code | varchar(32) | 产品编码 |
| claim_count | int | 报案件数 |
| approved_count | int | 结案件数 |
| claim_amount | decimal(15,2) | 报案金额 |
| paid_amount | decimal(15,2) | 赔付金额 |
| loss_ratio | decimal(5,4) | 赔付率 |

---

> **变更记录**

| 版本 | 日期 | 变更内容 | 变更人 |
|------|------|----------|--------|
| V2.0 | 2026-01-20 | 初始版本 | 张伟 |
| V2.5 | 2026-02-20 | 增加理赔相关表 | 赵雨桐 |
| V3.0 | 2026-03-15 | 增加分析库宽表 | 黄晓明 |

---

## 关联文档

- 数据字典：[[数据字典_核心业务字段说明]]
- 架构设计：[[保险核心系统技术架构设计]]

### 需求来源
- [[车险投保业务需求规格说明书_BRD]]
- [[健康险理赔流程需求规格说明书_SRS]]
- [[寿险保全业务需求规格说明书_BRD]]
- [[团险投保与理赔需求规格说明书_BRD]]
