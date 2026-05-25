# Compliance Check Prompt

请审查以下法律内容是否存在风险：

1. 是否存在绝对化法律结论；
2. 是否承诺胜诉、赔偿金额或处理结果；
3. 是否可能误导普通用户；
4. 是否泄露当事人隐私；
5. 是否存在诽谤或名誉侵权风险；
6. 是否有煽动性或攻击性表达；
7. 是否可能违反平台内容规则；
8. 是否缺少必要风险提示。

请输出：

```json
{
  "risk_score": 0,
  "risk_level": "low / medium / high",
  "risk_items": [],
  "revision_suggestions": [],
  "safe_version": ""
}
```
