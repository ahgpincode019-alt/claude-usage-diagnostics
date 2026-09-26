#!/usr/bin/env python3
"""Offline questionnaire for separating common Claude troubleshooting paths."""

def ask(label: str) -> str:
    return input(f"{label} ").strip().lower()


def main() -> None:
    print("Claude usage diagnostic (offline; no account data is collected)\n")
    error = ask("What best describes the symptom? [usage/context/api/auth/other]")
    if error == "usage":
        print("Next: open /usage and record the session window and weekly figure separately.")
        print("Do not infer that a weekly limit is exhausted from a short-window message alone.")
    elif error == "context":
        print("Next: record conversation size, attached files, and the exact context-related message.")
        print("Try a compact continuation containing only the facts the task still needs.")
    elif error == "api":
        print("Next: record the selected model, long-context option, effort level, tools, and retries.")
        print("Compare one minimal request on the ordinary model path, changing one variable at a time.")
    elif error == "auth":
        print("Next: run the official Claude Code auth status command and use the documented login flow if needed.")
        print("Never paste tokens, cookies, or private account output into a public issue or repository.")
    else:
        print("Next: preserve the exact error text, timestamp, client, model, and whether the web UI works.")
    print("\nThis is a triage aid, not a confirmation of account state. Verify against current official documentation.")


if __name__ == "__main__":
    main()
