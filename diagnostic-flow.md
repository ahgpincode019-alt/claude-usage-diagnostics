# Diagnostic flow

## 1. Identify the kind of limit

Start with the exact error and the current `/usage` view. A usage window is not the same as a conversation context limit. Record the session window and weekly figure separately.

## 2. Check the selected path

If the web interface works but a CLI request fails, record the model name, long-context setting, effort setting, and whether tools or retries are involved. Change one variable at a time so the result remains interpretable.

## 3. Check authentication

For Claude Code, use the documented status command and follow the official authentication flow. Never put an access token or account cookie in this repository or in a diagnostic report.

## 4. Verify before concluding

The matrix labels likely causes, not guaranteed causes. Re-check the current official help pages because plans, model names, and error messages can change.

Official starting points:

- [Troubleshoot Claude error messages](https://support.claude.com/en/articles/12466728-troubleshoot-claude-error-messages)
- [Get started with Claude](https://support.claude.com/en/articles/8114491-get-started-with-claude)
- [Claude Code authentication](https://code.claude.com/docs/en/authentication)
