"""Format and validate JSON from stdin or a file."""

import json
import sys
from pathlib import Path


def load_text():
    if len(sys.argv) > 1:
        return Path(sys.argv[1]).read_text(encoding="utf-8")
    return sys.stdin.read()


def main():
    text = load_text()
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        print(f"invalid json: {error}", file=sys.stderr)
        return 1
    print(json.dumps(data, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

