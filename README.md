# Claude Usage Diagnostics

A small, vendor-neutral troubleshooting aid for separating usage limits, context limits, model settings, and authentication problems when working with Claude.

## Included

- `diagnostic-matrix.csv` — symptom-to-check matrix for a spreadsheet or support workflow.
- `diagnostic-schema.json` — field definitions and severity values.
- `diagnose.py` — an offline command-line questionnaire that prints the next checks.
- `diagnostic-flow.md` — the decision flow with links to official Anthropic documentation.

This project does not call Claude, inspect an account, or claim access to private usage data. It helps you collect the right facts before changing plans or credentials. The companion public guide is [Claude Usage Guide](https://claudeusageguide.com/).

## Quick start

    python diagnose.py

## Scope

Service behavior and plan limits can change. Verify current limits and account details in Claude and in Anthropic's official documentation before treating a diagnosis as confirmed.

## License

MIT

## Language

简体中文说明见 [README.zh-CN.md](README.zh-CN.md)。
