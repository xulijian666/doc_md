---
文档编号: API-CLM-2026-002
版本: V1.8
编制人: 赵雨桐
编制日期: 2026-04-15
文档类型: 接口文档
业务域: 保险-理赔
tags:
  - 接口文档
  - API
  - 理赔
---

# 理赔系统 API 接口文档

| 项目 | 内容 |
|------|------|
| 文档编号 | API-CLM-2026-002 |
| 版本 | V1.8 |
| 编制日期 | 2026-04-15 |
| 编制人 | 赵雨桐 |
| Base URL | https://api.insurance.com/claim/v1 |

---

## 1. 理赔报案接口

### 1.1 创建报案

```
POST /report
```

**请求参数：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| policyNo | string | 是 | 保单号 |
| insuredId | string | 是 | 出险人ID |
| accidentDate | string | 是 | 出险日期 |
| accidentType | enum | 是 | DISEASE/ACCIDENT/OTHER |
| hospitalCode | string | 是 | 就诊医院编码 |
| diagnosis | string | 是 | 诊断描述 |
| diagnosisCode | string | 是 | ICD-10编码 |
| estimatedAmount | number | 否 | 预估金额 |
| description | string | 否 | 出险描述 |
| reporterMobile | string | 是 | 报案人手机号 |

**响应参数：**

```json
{
  "code": 200,
  "data": {
    "claimNo": "CLM20260510000001",
    "reportTime": "2026-05-10T14:00:00",
    "status": "REPORTED",
    "requiredMaterials": [
      { "type": "ID_CARD", "name": "身份证", "status": "PENDING" },
      { "type": "BANK_CARD", "name": "银行卡", "status": "PENDING" },
      { "type": "INVOICE", "name": "医疗发票", "status": "PENDING" },
      { "type": "MEDICAL_RECORD", "name": "病历", "status": "PENDING" },
      { "type": "FEE_DETAIL", "name": "费用明细", "status": "PENDING" }
    ]
  }
}
```

### 1.2 材料上传

```
POST /report/{claimNo}/materials
```

**请求参数（multipart/form-data）：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| materialType | string | 是 | 材料类型 |
| file | file | 是 | 文件内容 |
| ocrConfirm | boolean | 否 | 是否确认OCR结果 |

### 1.3 OCR识别结果

```
GET /report/{claimNo}/materials/{materialId}/ocr
```

**响应参数：**

```json
{
  "code": 200,
  "data": {
    "materialType": "INVOICE",
    "ocrResult": {
      "invoiceNo": "12345678",
      "invoiceDate": "2026-05-10",
      "totalAmount": 15230.50,
      "hospitalName": "北京协和医院",
      "patientName": "张三",
      "items": [
        { "name": "手术费", "amount": 8000.00 },
        { "name": "药品费", "amount": 4500.50 },
        { "name": "检查费", "amount": 2730.00 }
      ]
    },
    "confidence": 0.97,
    "needConfirm": true
  }
}
```

## 2. 理赔审核接口

### 2.1 自动审核

```
POST /review/auto
```

**请求参数：**

```json
{
  "claimNo": "CLM20260510000001"
}
```

**响应参数：**

```json
{
  "code": 200,
  "data": {
    "claimNo": "CLM20260510000001",
    "autoReviewResult": "PASS",
    "riskScore": 25,
    "checks": [
      { "rule": "保单有效性", "result": "PASS" },
      { "rule": "等待期校验", "result": "PASS" },
      { "rule": "免责条款", "result": "PASS" },
      { "rule": "材料完整性", "result": "PASS" },
      { "rule": "重复报案", "result": "PASS" },
      { "rule": "医院白名单", "result": "PASS" },
      { "rule": "金额阈值", "result": "PASS" }
    ],
    "claimCalculation": {
      "totalExpense": 15230.50,
      "socialInsurancePaid": 8500.00,
      "deductible": 10000.00,
      "eligibleAmount": 5230.50,
      "reimbursementRate": 0.60,
      "payableAmount": 3138.30
    }
  }
}
```

### 2.2 人工审核

```
POST /review/manual
```

**请求参数：**

```json
{
  "claimNo": "CLM20260510000001",
  "action": "APPROVE",
  "approvedAmount": 3138.30,
  "remark": "材料齐全，诊断明确，同意理赔",
  "rejectReasonCode": null
}
```

### 2.3 拒赔

```
POST /review/manual
```

**请求参数：**

```json
{
  "claimNo": "CLM20260510000001",
  "action": "REJECT",
  "rejectReasonCode": "EXCLUSION_003",
  "remark": "属于免责条款第3条：既往症不在保障范围内"
}
```

## 3. 理算接口

### 3.1 理算计算

```
POST /calculate
```

**请求参数：**

```json
{
  "claimNo": "CLM20260510000001",
  "calculationModel": "STANDARD"
}
```

**响应参数：**

```json
{
  "code": 200,
  "data": {
    "claimNo": "CLM20260510000001",
    "calculation": {
      "items": [
        {
          "category": "手术费",
          "totalAmount": 8000.00,
          "eligibleAmount": 8000.00,
          "remark": "全额纳入"
        },
        {
          "category": "药品费",
          "totalAmount": 4500.50,
          "eligibleAmount": 3800.00,
          "remark": "部分药品不在目录内"
        },
        {
          "category": "检查费",
          "totalAmount": 2730.00,
          "eligibleAmount": 2730.00,
          "remark": "全额纳入"
        }
      ],
      "totalExpense": 15230.50,
      "totalEligible": 14530.00,
      "socialInsurancePaid": 8500.00,
      "deductible": 10000.00,
      "afterDeductible": 4530.00,
      "reimbursementRate": 0.60,
      "otherCompensation": 0,
      "payableAmount": 2718.00
    }
  }
}
```

## 4. 支付接口

### 4.1 赔款支付

```
POST /payment
```

**请求参数：**

```json
{
  "claimNo": "CLM20260510000001",
  "payeeName": "张三",
  "payeeBank": "工商银行",
  "payeeAccount": "6222021234567890123",
  "payAmount": 2718.00
}
```

### 4.2 支付状态查询

```
GET /payment/{claimNo}/status
```

**响应参数：**

```json
{
  "code": 200,
  "data": {
    "claimNo": "CLM20260510000001",
    "paymentStatus": "SUCCESS",
    "transactionId": "PAY20260512000001",
    "payAmount": 2718.00,
    "payTime": "2026-05-12T15:00:00",
    "bankSerialNo": "ICBC202605120001"
  }
}
```

## 5. 申诉接口

### 5.1 提交申诉

```
POST /appeal
```

**请求参数：**

```json
{
  "claimNo": "CLM20260510000001",
  "appealReason": "对拒赔结论有异议",
  "appealDescription": "该疾病非既往症，有体检报告证明",
  "supplementaryMaterials": [
    { "type": "HEALTH_CHECK", "fileUrl": "https://..." }
  ]
}
```

## 6. 查询接口

### 6.1 理赔案件列表

```
GET /cases?page=1&size=20&status=APPROVED&startDate=2026-05-01&endDate=2026-05-31
```

### 6.2 理赔案件详情

```
GET /cases/{claimNo}
```

### 6.3 理赔统计

```
GET /statistics?period=monthly&year=2026&month=5
```

---

> **变更记录**

| 版本 | 日期 | 变更内容 | 变更人 |
|------|------|----------|--------|
| V1.0 | 2026-02-15 | 初始版本 | 赵雨桐 |
| V1.5 | 2026-03-20 | 增加OCR接口 | 陈思远 |
| V1.8 | 2026-04-15 | 增加申诉接口 | 刘建国 |

---

## 关联文档

- 需求规格：[[健康险理赔流程需求规格说明书_SRS]]、[[团险投保与理赔需求规格说明书_BRD]]
- 架构设计：[[保险核心系统技术架构设计]]
- 数据模型：[[核心数据模型设计_ERD]]
- 数据字典：[[数据字典_核心业务字段说明]]
