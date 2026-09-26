# Claude 使用诊断工具

这是一套与厂商无关的排查辅助资料，用来区分 Claude 的使用额度、上下文限制、模型设置和身份验证问题。

## 内容

- `data/diagnostic-matrix.csv`：可放进表格或支持流程的“症状—检查—下一步”矩阵。
- `data/diagnostic-schema.json`：字段定义和置信度值。
- `tools/diagnose.py`：离线命令行问答工具。
- `docs/diagnostic-flow.md`：带 Anthropic 官方文档链接的排查流程（英文版）。

这个项目不会调用 Claude、读取账户或声称能访问私有使用数据。它只帮助你在更改套餐或凭证前收集正确事实。配套公开指南见 [Claude Usage Guide](https://claudeusageguide.com/)。

## 快速开始

```bash
python tools/diagnose.py
```

## 范围

服务行为和套餐限制可能变化。把诊断结果当作线索，不要当作账户状态的确认；使用前应在 Claude 和 Anthropic 官方文档中复核当前信息。

英文说明见 [`README.md`](README.md)。
