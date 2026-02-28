---
name: fee-income-forecast
description: "Generate quarterly intermediate business income forecast notification emails (.eml) for provincial branch departments and city branch finance departments. Use when: (1) user receives head office forecast notice and needs to draft downstream notifications, (2) user says 中收预测通知, 生成中收邮件, 中间业务预测, or similar, (3) quarterly forecast season (typically the month before quarter-end)."
---

# 中收预测通知

Generate two notification emails per quarter for intermediate business income forecasting:
1. **City branch notice** (给市分行) — detailed forecast with calendar table
2. **Department notice** (给专业部门) — department-level forecast with simpler format

## Workflow

```
1. Collect inputs (head office notice + provincial finance notice)
2. Determine reporting dates and rules
3. Generate city branch notice (.eml)
4. Generate department notice (.eml)
5. User review and send
```

## Step 1: Collect Inputs

Ask user for:
- Head office notice content (总行通知)
- Provincial finance forecast notice (省行财务预测通知) — for date alignment
- Any additional reporting dates or special requirements

## Step 2: Determine Reporting Dates

1. Base dates = provincial finance forecast dates
2. Add any extra dates required by head office (e.g., early first submission)
3. Last day of quarter: always add 18:00 supplementary report
4. C-column rules: see `references/填报规则.md`

## Step 3: Generate City Branch Notice

**Target**: city branch finance departments + provincial branch professional departments

**Email structure**:
- Title: 关于{year}年{quarter}中间业务收入预测安排的通知
- Addressee: 各市分行
- Body sections: 预测内容 → 报送方式 → 报送时间(with calendar) → 注意事项
- Sign-off: 省分行财务会计部 + date

**Formatting**: see `references/邮件格式规范.md`

**Calendar table**: generate March calendar with ✅ on reporting dates. Last day gets special red highlight with "18时加报" note.

**Recipients**: load from `03 Projects/中收预测/收件人通讯录.md`
- To: city branch contacts only (市分行联系人, no provincial department staff)
- Cc: 陈良元, 徐捷 (省分行财务会计部)

**Output**: `00 Focus Zone/中间业务收入预测通知.eml`

## Step 4: Generate Department Notice

**Target**: provincial branch professional departments only

**Email structure**:
- Title: 关于{year}年{quarter}中间业务收入预测安排的通知
- Addressee: 各专业部门
- Body sections: 报送内容 → 报送时间 → 填报提示 → 预测表样
- Sign-off: 财务会计部 + date

Key content points:
- 报送内容: 分科目收入/支出预测 + 季末下划收入预测, 共两张表
- 填报提示: 含总行下划/分润、省行划转、工银理财模拟考核; 支出科目涉及银行卡/个金/结现等; 科目分工按上年分润规则; 同比下降科目备注说明
- 预测表样: 附同期、上月科目收入及预测累计数
- Attachment placeholder: 省分行专业部门科目预测模板-{year}年{quarter}.xlsx

**Recipients**: load from `03 Projects/中收预测/收件人通讯录.md`
- To: professional departments only (省分行专业部门, excluding 财务会计部 itself)
- Cc: 陈良元, 徐捷

**Output**: `00 Focus Zone/中间业务收入预测通知（专业部门）.eml`

## Step 5: User Review

Remind user to:
1. Open .eml files in email client to preview
2. Verify dates, content, recipients
3. Attach actual Excel templates before sending
4. Replace placeholder sender address with real address

## EML Generation

Use Python `email.mime.text.MIMEText` with HTML body, charset UTF-8. See `references/邮件格式规范.md` for font and styling specs. See `scripts/generate_eml.py` for the generation script.

## Resources

- `references/邮件格式规范.md` — font specs, calendar table styling, color codes
- `references/填报规则.md` — C-column fill rules, forecast content specs
- `scripts/generate_eml.py` — Python script to generate .eml files
- Contacts: `03 Projects/中收预测/收件人通讯录.md`
- Project overview: `03 Projects/中收预测/README.md`
