---
文档编号: API-INSUR-2026-001
版本: V2.5
编制人: 陈思远
编制日期: 2026-04-01
文档类型: 接口文档
业务域: 保险-投保
tags:
  - 接口文档
  - API
  - 投保
---

# 投保核心系统 API 接口文档

| 项目 | 内容 |
|------|------|
| 文档编号 | API-INSUR-2026-001 |
| 版本 | V2.5 |
| 编制日期 | 2026-04-01 |
| 编制人 | 陈思远 |
| Base URL | https://api.insurance.com/api/v1 |

---

## 1. 通用说明

### 1.1 请求头

| Header         | 必填  | 说明               |
| -------------- | --- | ---------------- |
| Content-Type   | 是   | application/json |
| Authorization  | 是   | Bearer {token}   |
| X-Channel-Code | 是   | 渠道编码             |
| X-Request-Id   | 是   | 请求唯一标识（UUID）     |
| X-Timestamp    | 是   | 请求时间戳（毫秒）        |
| X-Sign         | 是   | 请求签名             |

### 1.2 签名算法

```
1. 将所有请求参数按字典序排序
2. 拼接为 key1=value1&key2=value2 形式
3. 使用 RSA2（SHA256WithRSA）私钥签名
4. Base64编码后放入 X-Sign 头
```

### 1.3 统一响应格式

```json
{
  "code": 200,
  "message": "success",
  "data": {},
  "requestId": "uuid",
  "timestamp": 1714567890000
}
```

### 1.4 错误码

| 错误码 | 说明 |
|--------|------|
| 200 | 成功 |
| 400 | 参数错误 |
| 401 | 未授权 |
| 403 | 无权限 |
| 404 | 资源不存在 |
| 429 | 请求过于频繁 |
| 500 | 服务器内部错误 |
| 10001 | 投保单不存在 |
| 10002 | 核保拒绝 |
| 10003 | 支付失败 |
| 10004 | 保单已过期 |
| 10005 | 重复投保 |

---

## 2. 投保接口

### 2.1 报价试算

```
POST /insurance/quote
```

**请求参数：**

```json
{
  "productCode": "CAR-BIZ-2026",
  "channelCode": "ALIPAY",
  "applicant": {
    "name": "张三",
    "idType": "ID_CARD",
    "idNumber": "110101199001011234",
    "mobile": "13800138000"
  },
  "insured": [
    {
      "name": "张三",
      "idType": "ID_CARD",
      "idNumber": "110101199001011234",
      "relation": "SELF"
    }
  ],
  "vehicle": {
    "plateNo": "京A12345",
    "vin": "LSVAU2180N2123456",
    "engineNo": "EA8881234",
    "brandModel": "大众帕萨特2025款",
    "firstRegDate": "2025-06-15",
    "usage": "FAMILY",
    "seatCount": 5
  },
  "coverages": [
    {
      "coverageCode": "CAR_DAMAGE",
      "insuredAmount": 200000
    },
    {
      "coverageCode": "CAR_THIRD",
      "insuredAmount": 1000000
    },
    {
      "coverageCode": "CAR_DRIVER",
      "insuredAmount": 50000
    }
  ],
  "effectiveDate": "2026-05-01",
  "expireDate": "2027-04-30"
}
```

**响应参数：**

```json
{
  "code": 200,
  "data": {
    "quoteNo": "Q20260501000001",
    "totalPremium": 4520.30,
    "premiumDetail": [
      {
        "coverageCode": "CAR_DAMAGE",
        "coverageName": "机动车损失险",
        "basePremium": 2800.00,
        "finalPremium": 2156.00,
        "factors": {
          "ncd": 0.7,
          "violation": 1.0,
          "pricing": 0.85,
          "channel": 0.95
        }
      },
      {
        "coverageCode": "CAR_THIRD",
        "coverageName": "第三者责任险",
        "basePremium": 1200.00,
        "finalPremium": 1680.00
      },
      {
        "coverageCode": "CAR_DRIVER",
        "coverageName": "车上人员责任险（驾驶员）",
        "basePremium": 500.00,
        "finalPremium": 684.30
      }
    ],
    "quoteExpireTime": "2026-05-08T23:59:59"
  }
}
```

### 2.2 投保提交

```
POST /insurance/submit
```

**请求参数：**

```json
{
  "quoteNo": "Q20260501000001",
  "paymentMethod": "WECHAT",
  "healthDisclosure": null,
  "agreeTerms": true,
  "callbackUrl": "https://channel.example.com/callback"
}
```

**响应参数：**

```json
{
  "code": 200,
  "data": {
    "proposalNo": "P20260501000001",
    "status": "UNDERWRITING",
    "paymentUrl": "https://pay.example.com/...",
    "paymentExpireTime": "2026-05-01T12:00:00"
  }
}
```

### 2.3 投保单查询

```
GET /insurance/proposal/{proposalNo}
```

**响应参数：**

```json
{
  "code": 200,
  "data": {
    "proposalNo": "P20260501000001",
    "policyNo": "BJCA20260000000001",
    "status": "EFFECTIVE",
    "productCode": "CAR-BIZ-2026",
    "productName": "商业车险",
    "applicant": { "..." },
    "insured": [ "..." ],
    "vehicle": { "..." },
    "coverages": [ "..." ],
    "totalPremium": 4520.30,
    "effectiveDate": "2026-05-01",
    "expireDate": "2027-04-30",
    "createTime": "2026-05-01T10:30:00",
    "underwriteTime": "2026-05-01T10:30:15",
    "paymentTime": "2026-05-01T10:32:00",
    "issueTime": "2026-05-01T10:32:30"
  }
}
```

### 2.4 保单验真

```
POST /insurance/verify
```

**请求参数：**

```json
{
  "policyNo": "BJCA20260000000001",
  "insuredName": "张三",
  "idNumber": "110101199001011234"
}
```

---

## 3. 核保接口

### 3.1 核保结果查询

```
GET /underwriting/result/{proposalNo}
```

**响应参数：**

```json
{
  "code": 200,
  "data": {
    "proposalNo": "P20260501000001",
    "result": "APPROVED",
    "autoUnderwrite": true,
    "riskScore": 35,
    "riskLevel": "LOW",
    "underwriteTime": "2026-05-01T10:30:15",
    "remarks": []
  }
}
```

### 3.2 人工核保提交

```
POST /underwriting/manual/submit
```

**请求参数：**

```json
{
  "proposalNo": "P20260501000001",
  "action": "APPROVE",
  "remark": "风险可控，同意承保",
  "adjustedPremium": null
}
```

---

## 4. 支付接口

### 4.1 支付结果回调

```
POST /payment/callback (由支付网关调用)
```

**请求参数：**

```json
{
  "transactionId": "TXN20260501000001",
  "proposalNo": "P20260501000001",
  "status": "SUCCESS",
  "amount": 4520.30,
  "paymentMethod": "WECHAT",
  "paidTime": "2026-05-01T10:32:00",
  "sign": "..."
}
```

### 4.2 退款接口

```
POST /payment/refund
```

**请求参数：**

```json
{
  "policyNo": "BJCA20260000000001",
  "refundAmount": 4520.30,
  "refundReason": "犹豫期退保",
  "refundAccount": "original"
}
```

---

## 5. 保全接口

### 5.1 退保试算

```
POST /baoku/surrender/calculate
```

**请求参数：**

```json
{
  "policyNo": "BJCA20260000000001"
}
```

**响应参数：**

```json
{
  "code": 200,
  "data": {
    "policyNo": "BJCA20260000000001",
    "totalPaidPremium": 4520.30,
    "cashValue": 2260.15,
    "surrenderCharge": 226.02,
    "refundAmount": 2034.13,
    "lossRate": 55.0,
    "inCoolingPeriod": false
  }
}
```

### 5.2 受益人变更

```
POST /baoku/beneficiary/change
```

### 5.3 缴费方式变更

```
POST /baoku/payment-method/change
```

---

## 6. 理赔接口

### 6.1 理赔报案

```
POST /claim/report
```

**请求参数：**

```json
{
  "policyNo": "BJCA20260000000001",
  "insuredName": "张三",
  "accidentDate": "2026-05-10",
  "accidentType": "DISEASE",
  "hospital": "北京协和医院",
  "diagnosis": "急性阑尾炎",
  "diagnosisCode": "K35.8",
  "estimatedAmount": 15000,
  "materials": [
    {
      "type": "INVOICE",
      "fileUrl": "https://..."
    },
    {
      "type": "MEDICAL_RECORD",
      "fileUrl": "https://..."
    }
  ]
}
```

### 6.2 理赔进度查询

```
GET /claim/progress/{claimNo}
```

**响应参数：**

```json
{
  "code": 200,
  "data": {
    "claimNo": "CLM20260510000001",
    "policyNo": "BJCA20260000000001",
    "status": "APPROVED",
    "claimAmount": 15000,
    "approvedAmount": 12800,
    "deductible": 10000,
    "payableAmount": 2800,
    "timeline": [
      { "time": "2026-05-10T14:00:00", "action": "报案受理", "status": "DONE" },
      { "time": "2026-05-10T14:05:00", "action": "材料审核", "status": "DONE" },
      { "time": "2026-05-11T09:00:00", "action": "理算完成", "status": "DONE" },
      { "time": "2026-05-11T10:00:00", "action": "审核通过", "status": "DONE" },
      { "time": "2026-05-12T15:00:00", "action": "赔款支付", "status": "DONE" }
    ]
  }
}
```

---

> **变更记录**

| 版本 | 日期 | 变更内容 | 变更人 |
|------|------|----------|--------|
| V2.0 | 2026-02-01 | 初始版本 | 陈思远 |
| V2.3 | 2026-03-10 | 增加保全接口 | 孙丽华 |
| V2.5 | 2026-04-01 | 增加理赔接口 | 赵雨桐 |

---

## 关联文档

- 需求规格：[[车险投保业务需求规格说明书_BRD]]、[[互联网保险渠道对接需求规格说明书_SRS]]
- 架构设计：[[保险核心系统技术架构设计]]
- 数据模型：[[核心数据模型设计_ERD]]
- 数据字典：[[数据字典_核心业务字段说明]]
- 异常处理：[[理赔系统API接口文档]]
