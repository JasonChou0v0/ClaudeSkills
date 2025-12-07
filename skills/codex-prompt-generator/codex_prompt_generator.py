#!/usr/bin/env python3
"""
Codex Prompt Generator Skill
根据需求文档生成Codex编码提示词的技能
"""

import json
import sys
from typing import Dict, Any


def analyze_requirement_doc(requirement_doc: str) -> Dict[str, Any]:
    """
    分析需求文档，提取关键信息

    Args:
        requirement_doc (str): 需求文档内容

    Returns:
        Dict[str, Any]: 包含分析结果的字典
    """
    # 简单的关键词提取（实际应用中可以使用NLP技术）
    lines = requirement_doc.split('\n')

    # 提取可能的编程语言
    languages = []
    if 'python' in requirement_doc.lower():
        languages.append('Python')
    if 'javascript' in requirement_doc.lower() or 'js' in requirement_doc.lower():
        languages.append('JavaScript')
    if 'java' in requirement_doc.lower():
        languages.append('Java')
    if 'c++' in requirement_doc.lower() or 'cpp' in requirement_doc.lower():
        languages.append('C++')
    if 'go' in requirement_doc.lower() or 'golang' in requirement_doc.lower():
        languages.append('Go')

    # 提取功能需求
    functionalities = []
    for line in lines:
        if line.strip().startswith(('-', '*', '•')):
            functionalities.append(line.strip()[1:].strip())

    # 提取非功能性需求
    non_functional = []
    nfr_keywords = ['性能', '安全', '可用性', '可扩展性', '兼容性', '维护性']
    for keyword in nfr_keywords:
        if keyword in requirement_doc:
            non_functional.append(keyword)

    return {
        'languages': languages,
        'functionalities': functionalities,
        'non_functional_requirements': non_functional,
        'doc_length': len(requirement_doc)
    }


def generate_codex_prompt(analysis_result: Dict[str, Any], requirement_doc: str) -> str:
    """
    根据分析结果生成Codex编码提示词

    Args:
        analysis_result (Dict[str, Any]): 需求文档分析结果
        requirement_doc (str): 原始需求文档

    Returns:
        str: Codex编码提示词
    """
    prompt_parts = []

    # 添加开头说明
    prompt_parts.append("# Codex编码助手")
    prompt_parts.append("请根据以下需求文档生成相应的代码：\n")

    # 添加编程语言信息
    if analysis_result['languages']:
        prompt_parts.append(f"编程语言: {', '.join(analysis_result['languages'])}\n")

    # 添加功能需求
    if analysis_result['functionalities']:
        prompt_parts.append("功能需求:")
        for i, func in enumerate(analysis_result['functionalities'], 1):
            prompt_parts.append(f"{i}. {func}")
        prompt_parts.append("")

    # 添加非功能性需求
    if analysis_result['non_functional_requirements']:
        prompt_parts.append("非功能性需求:")
        for req in analysis_result['non_functional_requirements']:
            prompt_parts.append(f"- {req}")
        prompt_parts.append("")

    # 添加原始需求文档
    prompt_parts.append("详细需求文档:")
    prompt_parts.append("```")
    prompt_parts.append(requirement_doc)
    prompt_parts.append("```")

    # 添加Codex指令
    prompt_parts.append("\n请根据以上需求生成完整的代码实现，包括:")
    prompt_parts.append("- 必要的导入语句")
    prompt_parts.append("- 完整的函数/类定义")
    prompt_parts.append("- 适当的注释说明")
    prompt_parts.append("- 示例用法")

    return "\n".join(prompt_parts)


def main():
    """主函数"""
    try:
        # 从stdin读取输入
        input_data = json.load(sys.stdin)
        requirement_doc = input_data.get('requirement_doc', '')

        if not requirement_doc:
            print(json.dumps({
                "error": "缺少需求文档输入"
            }), file=sys.stderr)
            sys.exit(1)

        # 分析需求文档
        analysis_result = analyze_requirement_doc(requirement_doc)

        # 生成Codex提示词
        codex_prompt = generate_codex_prompt(analysis_result, requirement_doc)

        # 输出结果
        result = {
            "codex_prompt": codex_prompt
        }

        print(json.dumps(result, ensure_ascii=False, indent=2))

    except Exception as e:
        print(json.dumps({
            "error": f"处理过程中发生错误: {str(e)}"
        }), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()