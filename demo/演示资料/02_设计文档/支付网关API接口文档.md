---
文档编号: API-PAY-2026-003
版本: V2.0
编制人: 李建国
编制日期: 2026-03-20
文档类型: 接口文档
业务域: 保险-支付
tags:
  - 接口文档
  - API
  - 支付网关
---

# 支付网关 API 接口文档

| 项目 | 内容 |
|------|------|
| 文档编号 | API-PAY-2026-003 |
| 版本 | V2.0 |
| 编制日期 | 2026-03-20 |
| 编制人 | 李建国 |
| Base URL | https://api.insurance.com/payment/v1 |

---

## 1. 支付渠道

| 渠道编码 | 渠道名称 | 支持场景 | 手续费 |
|----------|----------|----------|--------|
| WECHAT | 微信支付 | APP/H5/小程序 | 0.6% |
| ALIPAY | 支付宝 | APP/H5/小程序 | 0.55% |
| UNIONPAY | 银联快捷支付 | APP/H5 | 0.45% |
| BANK_TRANSFER | 对公转账 | 后台 | 0 |
| AUTO_DEBIT | 银行代扣 | 自动续费 | 0.3% |

## 2. 统一支付接口

### 2.1 创建支付单

```
POST /create
```

**请求参数：**

```json
{
  "orderNo": "P20260501000001",
  "orderType": "PREMIUM",
  "amount": 4520.30,
  "currency": "CNY",
  "paymentMethod": "WECHAT",
  "payerName": "张三",
  "payerMobile": "13800138000",
  "description": "商业车险保费",
  "expireTime": "2026-05-01T12:00:00",
  "notifyUrl": "https://core.insurance.com/payment/callback",
  "returnUrl": "https://app.insurance.com/pay/result"
}
```

**响应参数：**

```json
{
  "code": 200,
  "data": {
    "paymentNo": "PAY20260501000001",
    "paymentUrl": "weixin://wxpay/bizpayurl?...",
    "prepayId": "wx20260501103000abcdef",
    "expireTime": "2026-05-01T12:00:00"
  }
}
```

### 2.2 支付状态查询

```
GET /status/{paymentNo}
```

**响应参数：**

```json
{
  "code": 200,
  "data": {
    "paymentNo": "PAY20260501000001",
    "orderNo": "P20260501000001",
    "status": "SUCCESS",
    "amount": 4520.30,
    "paymentMethod": "WECHAT",
    "channelTransactionId": "4200001234202605010000000001",
    "paidTime": "2026-05-01T10:32:00",
    "notifyStatus": "NOTIFIED"
  }
}
```

### 2.3 支付结果通知（回调）

```
POST {notifyUrl} (支付网关调用业务系统)
```

**通知参数：**

```json
{
  "paymentNo": "PAY20260501000001",
  "orderNo": "P20260501000001",
  "status": "SUCCESS",
  "amount": 4520.30,
  "paidTime": "2026-05-01T10:32:00",
  "sign": "RSA2_SIGNATURE"
}
```

## 3. 退款接口

### 3.1 发起退款

```
POST /refund
```

**请求参数：**

```json
{
  "originalPaymentNo": "PAY20260501000001",
  "refundAmount": 4520.30,
  "refundReason": "犹豫期退保",
  "refundType": "FULL",
  "notifyUrl": "https://core.insurance.com/refund/callback"
}
```

**响应参数：**

```json
{
  "code": 200,
  "data": {
    "refundNo": "REF20260515000001",
    "status": "PROCESSING",
    "estimatedTime": "2026-05-20T23:59:59"
  }
}
```

### 3.2 退款状态查询

```
GET /refund/{refundNo}
```

## 4. 赔款支付接口

### 4.1 赔款发放

```
POST /claim-payment
```

**请求参数：**

```json
{
  "claimNo": "CLM20260510000001",
  "payeeName": "张三",
  "payeeIdNumber": "110101199001011234",
  "payeeBankCode": "ICBC",
  "payeeAccount": "6222021234567890123",
  "amount": 2718.00,
  "purpose": "医疗理赔款"
}
```

## 5. 对账接口

### 5.1 下载对账文件

```
GET /reconciliation?date=2026-05-01&channel=WECHAT
```

### 5.2 差异处理

```
POST /reconciliation/dispute
```

## 6. 安全规范

| 安全项 | 要求 |
|--------|------|
| 通信加密 | TLS 1.2+ |
| 数据签名 | RSA2（SHA256WithRSA） |
| 敏感信息 | 银行卡号AES加密传输 |
| 证书管理 | 商户证书+平台证书双证书体系 |
| IP白名单 | 支付回调IP需白名单配置 |

---

> **变更记录**

| 版本 | 日期 | 变更内容 | 变更人 |
|------|------|----------|--------|
| V1.0 | 2026-01-20 | 初始版本 | 李建国 |
| V2.0 | 2026-03-20 | 增加赔款支付和对账接口 | 李建国 |

---

## 关联文档

- 需求规格：[[互联网保险渠道对接需求规格说明书_SRS]]
- 架构设计：[[保险核心系统技术架构设计]]
- 数据字典：[[数据字典_核心业务字段说明]]
