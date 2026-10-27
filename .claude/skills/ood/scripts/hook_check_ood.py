"""PostToolUse hook: re-run check_ood.py whenever FINAL_OOD.md is written or edited.

Reads the hook payload from stdin and ignores every other file. On check errors it exits 2,
which feeds the report back to the agent that made the edit so it can fix the document.
"""
import json
import subprocess
import sys
from pathlib import Path

TARGET = "FINAL_OOD.md"
CHECKER = Path(__file__).with_name("check_ood.py")


def main():
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    file_path = (payload.get("tool_input") or {}).get("file_path") or ""
    if Path(file_path).name != TARGET or not Path(file_path).is_file():
        return 0
    result = subprocess.run(
        [sys.executable, str(CHECKER), file_path],
        capture_output=True, text=True, encoding="utf-8",
    )
    if result.returncode == 1:
        sys.stderr.reconfigure(encoding="utf-8")
        sys.stderr.write(f"check_ood.py found rubric-penalty errors in {TARGET}; fix them:\n{result.stdout}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
