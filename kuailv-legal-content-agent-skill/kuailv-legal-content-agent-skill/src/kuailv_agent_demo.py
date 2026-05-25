#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KuaiLv Legal Content Agent Demo

This is a lightweight rule-based demo that simulates the multi-agent workflow.
In production, each function can be replaced with an LLM call and RAG retrieval.
"""

import argparse
from pathlib import Path


def parser_agent(text: str) -> dict:
    return {
        "parties": ["员工", "公司"] if "员工" in text and "公司" in text else [],
        "key_facts": [
            "长期未签订书面劳动合同",
            "按月转账发放工资",
            "通过微信安排工作",
            "口头通知不用上班",
            "未支付经济补偿",
        ],
        "disputed_issues": [
            "是否存在劳动关系",
            "未签书面劳动合同是否产生责任",
            "口头解除是否违法",
            "员工可主张哪些权利",
            "证据是否充分",
        ],
    }


def rag_research_agent(parsed: dict) -> dict:
    return {
        "legal_basis_summary": [
            "劳动关系认定通常需要结合用工管理、劳动报酬、工作内容等因素判断。",
            "未签书面劳动合同可能产生相应法律责任，但需结合时效和证据。",
            "解除劳动合同是否需要支付经济补偿或赔偿，应结合解除原因和程序判断。",
        ],
        "uncertainty": [
            "具体结论取决于入职时间、工资标准、证据完整度和当地仲裁口径。"
        ],
    }


def legal_reasoning_agent(parsed: dict, research: dict) -> str:
    return (
        "若员工能够证明其接受公司管理、按月领取劳动报酬、从事公司安排的工作，"
        "则即使未签书面合同，也可能被认定存在劳动关系。公司仅以口头方式通知员工离职，"
        "且未支付补偿，可能存在合规风险。具体能否获得支持，需要结合证据和仲裁时效判断。"
    )


def creator_agent(analysis: str) -> dict:
    return {
        "hook": "公司没签劳动合同，就能随便让你走人吗？",
        "script_60s": (
            "公司没签劳动合同，就能随便让你走人吗？不一定。"
            "如果你虽然没签合同，但每天按公司安排上班，工资也是公司按月转给你，"
            "工作群、考勤、客户沟通记录都能证明你在为公司工作，那么双方仍然可能被认定为劳动关系。"
            "这时候，公司一句经营困难让你明天不用来了，不等于合法解除。"
            "你要重点整理工资流水、工作安排、考勤记录和聊天记录。"
            "具体能主张什么，要看证据和时间，建议先保存证据，再考虑劳动仲裁。"
        ),
        "titles": [
            "没签劳动合同，公司就能随便辞退你？",
            "老板口头让你走人，真的合法吗？",
            "没合同也可能有劳动关系，关键看这些证据",
        ],
    }


def compliance_agent(content: dict) -> dict:
    return {
        "risk_level": "low",
        "risk_items": [
            "避免使用一定赔偿、必胜等绝对化表达",
            "补充具体案件需结合证据判断的提示",
        ],
        "safe_note": "本内容为普通普法，不构成针对具体案件的正式法律意见。",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input markdown file")
    args = parser.parse_args()

    text = Path(args.input).read_text(encoding="utf-8")
    parsed = parser_agent(text)
    research = rag_research_agent(parsed)
    analysis = legal_reasoning_agent(parsed, research)
    content = creator_agent(analysis)
    compliance = compliance_agent(content)

    print("# 快律 Demo 输出")
    print("\n## 解析结果")
    print(parsed)
    print("\n## 法律研究摘要")
    print(research)
    print("\n## 法律分析")
    print(analysis)
    print("\n## 60秒口播稿")
    print(content["script_60s"])
    print("\n## 标题候选")
    for title in content["titles"]:
        print(f"- {title}")
    print("\n## 合规提示")
    print(compliance)


if __name__ == "__main__":
    main()
