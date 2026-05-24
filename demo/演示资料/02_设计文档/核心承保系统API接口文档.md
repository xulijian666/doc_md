---
文档编号: DES-API-INS-2026-001
版本: V4.1
编制人: 陈思远
编制日期: 2026-04-01
文档类型: 接口文档
业务域: 保险-承保
tags:
  - 接口文档
  - API
  - 承保
---

# 核心承保系统 API 接口文档

| 项目 | 内容 |
|------|------|
| 文档编号 | DES-API-INS-2026-001 |
| 版本 | V4.1 |
| 编制日期 | 2026-04-01 |
| 编制人 | 陈思远 |
| 基础路径 | `https://api.insurance.com/api/v1` |

---

## 1. 概述

本文档定义核心承保系统对外提供的 RESTful API 接口，涵盖产品查询、报价、投保、核保、出单全流程。

### 1.1 通用规范

| 规范项 | 要求 |
|--------|------|
| 协议 | HTTPS (TLS 1.2+) |
| 数据格式 | JSON |
| 字符编码 | UTF-8 |
| 日期格式 | ISO 8601 (yyyy-MM-dd'T'HH:mm:ssZ) |
| 货币精度 | 分（整数，如100.00元表示为10000） |

### 1.2 通用请求头

| Header | 必填 | 说明 |
|--------|------|------|
| Authorization | 是 | Bearer {access_token} |
| Content-Type | 是 | application/json |
| X-Request-Id | 是 | 请求唯一标识 (UUID) |
| X-Timestamp | 是 | 请求时间戳 (毫秒) |
| X-Sign | 是 | 请求签名 |
| X-Channel | 否 | 渠道编码 |

### 1.3 通用响应结构

```json
{
  "code": 200,
  "message": "success",
  "data": { ... },
  "requestId": "550e8400-e29b-41d4-a716-446655440000",
  "timestamp": 1714550400000
}
```

### 1.4 错误码

| 错误码 | 说明 |
|--------|------|
| 200 | 成功 |
| 400 | 参数错误 |
| 401 | 未授权 |
| 403 | 权限不足 |
| 404 | 资源不存在 |
| 429 | 请求过于频繁 |
| 500 | 服务器内部错误 |
| 10001 | 投保单不存在 |
| 10002 | 投保单状态不允许操作 |
| 10003 | 产品已下架 |
| 10004 | 费率计算失败 |
| 10005 | 核保拒绝 |
| 10006 | 支付失败 |
| 10007 | 保单生成失败 |
| 10008 | 重复投保 |
| 10009 | 投保人年龄不在承保范围 |
| 10010 | 车型库无匹配记录 |

---

## 2. 产品模块

### 2.1 查询产品列表

```
GET /products
```

**请求参数：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| category | string | 否 | 产品类别：CAR/HEALTH/LIFE/PROPERTY |
| status | string | 否 | 状态：ON_SALE/OFF_SALE |
| page | int | 否 | 页码，默认1 |
| pageSize | int | 否 | 每页条数，默认20，最大100 |

**响应示例：**

```json
{
  "code": 200,
  "data": {
    "total": 15,
    "list": [
      {
        "productCode": "CAR-COMP-2026",
        "productName": "机动车交通事故责任强制保险",
        "category": "CAR",
        "status": "ON_SALE",
        "description": "国家强制投保的车辆保险",
        "coverageList": [
          {
            "coverageCode": "DEATH",
            "coverageName": "死亡伤残赔偿限额",
            "maxAmount": 180000
          },
          {
            "coverageCode": "MEDICAL",
            "coverageName": "医疗费用赔偿限额",
            "maxAmount": 18000
          },
          {
            "coverageCode": "PROPERTY",
            "coverageName": "财产损失赔偿限额",
            "maxAmount": 2000
          }
        ],
        "effectiveFrom": "2026-01-01",
        "effectiveTo": "2026-12-31"
      }
    ]
  }
}
```

### 2.2 查询产品详情

```
GET /products/{productCode}
```

**响应参数：**

| 参数 | 类型 | 说明 |
|------|------|------|
| productCode | string | 产品编码 |
| productName | string | 产品名称 |
| category | string | 产品类别 |
| planList | array | 方案列表 |
| planList[].planCode | string | 方案编码 |
| planList[].planName | string | 方案名称 |
| planList[].premium | long | 方案保费(分) |
| questionList | array | 健康告知问题列表 |

---

## 3. 报价模块

### 3.1 车险报价

```
POST /quote/car
```

**请求参数：**

```json
{
  "vehicleInfo": {
    "licenseNo": "京A12345",
    "vin": "LSVCA2A48GN000001",
    "engineNo": "EA888001",
    "brandModelCode": "BORA-2024",
    "firstRegDate": "2024-01-15",
    "usageType": "PRIVATE",
    "seatCount": 5
  },
  "applicant": {
    "name": "张三",
    "idType": "ID_CARD",
    "idNo": "110101199001011234",
    "mobile": "13800138000"
  },
  "coverageList": [
    { "coverageCode": "COMP", "amount": 0 },
    { "coverageCode": "CAR_DAMAGE", "amount": 0 },
    { "coverageCode": "THIRD_PARTY", "amount": 100000000 },
    { "coverageCode": "DRIVER", "amount": 5000000 },
    { "coverageCode": "PASSENGER", "amount": 5000000 }
  ],
  "effectiveDate": "2026-05-01"
}
```

**响应示例：**

```json
{
  "code": 200,
  "data": {
    "quoteNo": "Q2026050100001",
    "validUntil": "2026-05-08T23:59:59+08:00",
    "premiumDetail": {
      "compulsoryPremium": 95000,
      "commercialPremium": 3567800,
      "totalPremium": 3662800,
      "breakdown": [
        { "coverageCode": "COMP", "premium": 95000, "rate": 0.095 },
        { "coverageCode": "CAR_DAMAGE", "premium": 1200000, "factor": 1.0 },
        { "coverageCode": "THIRD_PARTY", "premium": 1580000, "factor": 0.85 },
        { "coverageCode": "DRIVER", "premium": 395800, "factor": 0.95 },
        { "coverageCode": "PASSENGER", "premium": 392000, "factor": 0.95 }
      ]
    },
    "factorDetail": {
      "ncdFactor": 0.85,
      "violationFactor": 1.0,
      "pricingFactor": 0.95,
      "channelFactor": 1.0
    }
  }
}
```

### 3.2 健康险报价

```
POST /quote/health
```

**请求参数：**

```json
{
  "productCode": "HL-MED-MILLION",
  "insuredList": [
    {
      "name": "李四",
      "idType": "ID_CARD",
      "idNo": "110101199201011234",
      "birthday": "1992-01-01",
      "gender": "MALE",
      "occupation": "OFFICE_WORKER"
    }
  ],
  "planCode": "PLAN-A",
  "socialInsurance": true
}
```

---

## 4. 投保模块

### 4.1 创建投保单

```
POST /insurance/apply
```

**请求参数：**

```json
{
  "quoteNo": "Q2026050100001",
  "applicant": {
    "name": "张三",
    "idType": "ID_CARD",
    "idNo": "110101199001011234",
    "mobile": "13800138000",
    "email": "zhangsan@example.com",
    "address": {
      "province": "北京市",
      "city": "北京市",
      "district": "朝阳区",
      "detail": "建国路88号SOHO现代城A座"
    }
  },
  "insuredList": [
    {
      "name": "张三",
      "idType": "ID_CARD",
      "idNo": "110101199001011234",
      "relationToApplicant": "SELF"
    }
  ],
  "beneficiaryList": [
    {
      "name": "张小三",
      "idType": "ID_CARD",
      "idNo": "110101202001011234",
      "relationToInsured": "CHILD",
      "share": 100
    }
  ],
  "healthDisclosure": [
    { "questionId": "HQ001", "answer": false },
    { "questionId": "HQ002", "answer": true, "detail": "2025年体检发现轻度脂肪肝" }
  ],
  "agreementVersion": "V2026.04"
}
```

**响应示例：**

```json
{
  "code": 200,
  "data": {
    "applyNo": "APP2026050100001",
    "status": "PENDING_UNDERWRITE",
    "premium": 3662800,
    "createdAt": "2026-05-01T10:30:00+08:00"
  }
}
```

### 4.2 查询投保单状态

```
GET /insurance/apply/{applyNo}
```

**响应参数：**

| 参数 | 类型 | 说明 |
|------|------|------|
| applyNo | string | 投保单号 |
| status | string | 状态：PENDING/UNDERWRITING/APPROVED/REJECTED/PAID/EFFECTIVE |
| premium | long | 保费(分) |
| rejectReason | string | 拒保原因（状态为REJECTED时） |
| policyNo | string | 保单号（状态为EFFECTIVE时） |
| timeline | array | 状态变更时间线 |

### 4.3 投保单支付

```
POST /insurance/apply/{applyNo}/pay
```

**请求参数：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| paymentMethod | string | 是 | WECHAT/ALIPAY/BANK_CARD/CORPORATE |
| paymentAccount | string | 否 | 支付账户（银行卡号） |
| returnUrl | string | 否 | 支付完成回调URL |

---

## 5. 核保模块

### 5.1 查询核保结果

```
GET /underwrite/{applyNo}
```

**响应示例：**

```json
{
  "code": 200,
  "data": {
    "applyNo": "APP2026050100001",
    "result": "APPROVED",
    "type": "AUTO",
    "score": 25,
    "riskLevel": "LOW",
    "rules": [
      {
        "ruleId": "AU-001",
        "ruleName": "车辆信息校验",
        "result": "PASS",
        "detail": "车辆信息与车型库匹配"
      },
      {
        "ruleId": "AU-006",
        "ruleName": "历史出险校验",
        "result": "PASS",
        "detail": "近3年出险1次，风险可控"
      }
    ],
    "processedAt": "2026-05-01T10:30:05+08:00"
  }
}
```

### 5.2 人工核保-审核

```
POST /underwrite/{applyNo}/review
```

**请求参数：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| result | string | 是 | APPROVED/REJECTED/CONDITIONAL |
| comment | string | 否 | 审核意见 |
| conditions | array | 否 | 附加承保条件（CONDITIONAL时必填） |
| reviewerId | string | 是 | 审核员工号 |

---

## 6. 保单模块

### 6.1 查询保单详情

```
GET /policies/{policyNo}
```

**响应示例：**

```json
{
  "code": 200,
  "data": {
    "policyNo": "BJ-CAR-2026-0000000001",
    "productCode": "CAR-COMP-2026",
    "productName": "交强险+商业车险",
    "status": "EFFECTIVE",
    "effectiveDate": "2026-05-01",
    "expireDate": "2027-04-30",
    "premium": 3662800,
    "applicant": { "name": "张三", "mobile": "13800138000" },
    "insured": { "name": "张三" },
    "vehicle": {
      "licenseNo": "京A12345",
      "vin": "LSVCA2A48GN000001",
      "brandModel": "大众宝来2024款"
    },
    "coverageDetail": [
      { "coverageCode": "COMP", "coverageName": "交强险", "amount": 200000 },
      { "coverageCode": "CAR_DAMAGE", "coverageName": "车损险", "amount": 150000000 },
      { "coverageCode": "THIRD_PARTY", "coverageName": "第三者责任险", "amount": 100000000 }
    ],
    "pdfUrl": "https://oss.insurance.com/policies/BJ-CAR-2026-0000000001.pdf"
  }
}
```

### 6.2 保单验真

```
GET /policies/verify/{policyNo}
```

**响应参数：**

| 参数 | 类型 | 说明 |
|------|------|------|
| valid | boolean | 是否有效 |
| policyNo | string | 保单号 |
| productName | string | 产品名称 |
| status | string | 保单状态 |
| effectiveDate | string | 生效日期 |
| expireDate | string | 到期日期 |

---

## 7. 签名算法

### 7.1 签名生成规则

```python
# 1. 将请求参数按ASCII码排序，拼接成字符串
sorted_params = sorted(params.items())
sign_str = "&".join(f"{k}={v}" for k, v in sorted_params)

# 2. 拼接时间戳和随机串
sign_str = f"{timestamp}\n{nonce}\n{sign_str}"

# 3. 使用RSA私钥签名
signature = rsa_sign(sign_str, private_key, algorithm='SHA256WithRSA')

# 4. Base64编码
x_sign = base64_encode(signature)
```

### 7.2 签名验证

服务端使用渠道方公钥验证签名，时间戳偏差超过5分钟的请求拒绝。

---

> **变更记录**

| 版本 | 日期 | 变更内容 | 变更人 |
|------|------|----------|--------|
| V4.0 | 2026-02-01 | 全面重构接口规范 | 陈思远 |
| V4.1 | 2026-04-01 | 增加保单验真接口、完善错误码 | 陈思远 |

---

## 关联文档

- 需求规格：[[车险投保业务需求规格说明书_BRD]]、[[寿险保全业务需求规格说明书_BRD]]
- 架构设计：[[保险核心系统技术架构设计]]
- 数据模型：[[核心数据模型设计_ERD]]
- 数据字典：[[数据字典_核心业务字段说明]]
