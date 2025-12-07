#!/usr/bin/env python3
"""
测试Codex提示词生成技能
"""

import json
import subprocess
import sys


def test_skill():
    """测试技能功能"""
    # 准备测试数据
    test_input = {
        "requirement_doc": """
        开发一个用户管理系统，需要包含以下功能：
        - 用户注册功能，需要验证邮箱格式
        - 用户登录功能，支持邮箱和密码登录
        - 用户信息修改功能
        - 密码重置功能

        非功能性需求：
        - 性能：系统应能支持1000并发用户
        - 安全：用户密码需加密存储
        - 可用性：系统正常运行时间应达到99.9%
        """
    }

    # 将测试数据转换为JSON字符串
    input_json = json.dumps(test_input, ensure_ascii=False, indent=2)

    print("测试输入:")
    print(input_json)
    print("\n" + "="*50 + "\n")

    # 调用技能脚本
    try:
        result = subprocess.run(
            ['python3', 'codex_prompt_generator.py'],
            input=input_json,
            capture_output=True,
            text=True,
            cwd='/Users/jason/Documents/Code/PythonProjects/ClaudeSkills/skills/codex-prompt-generator'
        )

        if result.returncode == 0:
            print("技能执行成功!")
            print("输出结果:")
            print(result.stdout)
        else:
            print("技能执行失败!")
            print("错误信息:")
            print(result.stderr)

    except FileNotFoundError:
        print("错误: 找不到技能脚本文件")
    except Exception as e:
        print(f"测试过程中发生错误: {e}")


if __name__ == "__main__":
    test_skill()