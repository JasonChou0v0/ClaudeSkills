# ClaudeSkills

Public repository for Claude Skills

## 目录结构

```
.
├── README.md
├── .claude-plugin/
│   └── marketplace.json      # 技能市场配置文件
└── skills/
    └── codex-prompt-generator/    # Codex提示词生成技能
        ├── codex_prompt_generator.py    # 技能主程序
        ├── codex_prompt_generator.yaml  # 技能配置文件
        └── test_codex_prompt_generator.py  # 技能测试文件
```

## 技能说明

### Codex提示词生成技能 (codex-prompt-generator)

根据需求文档生成Codex编码提示词的技能。该技能能够分析用户提供的需求文档，并自动生成结构化、优化的Codex编码提示词，帮助开发者更高效地使用Codex模型生成代码。

#### 功能特点

- 分析需求文档中的编程语言信息
- 提取功能需求和非功能性需求
- 自动生成结构化的Codex编码提示词
- 支持多种编程语言的代码生成提示

#### 输入参数

- `requirement_doc` (string, 必需): 需求文档内容

#### 输出结果

- `codex_prompt` (string): 为Codex模型优化的编码提示词