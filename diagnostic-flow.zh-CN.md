# 诊断流程

## 1. 先判断是哪类限制

从完整错误文本和当前 `/usage` 页面开始。使用窗口限制与单个对话的上下文限制不是一回事。分别记录短期窗口和周额度数字。

## 2. 检查实际使用路径

如果网页界面能用但 CLI 请求失败，记录模型名称、长上下文选项、effort 设置，以及是否涉及工具调用或自动重试。一次只改变一个变量，结果才容易解释。

## 3. 检查身份验证

使用 Claude Code 官方文档中的状态命令和登录流程。不要把访问令牌或账户 Cookie 放入此仓库或诊断报告。

## 4. 得出结论前复核

矩阵中的“可能原因”不是保证原因。套餐、模型名称和错误信息可能变化，应重新查看当前官方帮助页面。

官方入口：

- [排查 Claude 错误信息](https://support.claude.com/en/articles/12466728-troubleshoot-claude-error-messages)
- [开始使用 Claude](https://support.claude.com/en/articles/8114491-get-started-with-claude)
- [Claude Code 身份验证](https://code.claude.com/docs/en/authentication)
