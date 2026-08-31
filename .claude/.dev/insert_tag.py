"""Insert a problem name into a tags.json5 block in alphabetical order.

Usage: uv run python .claude/.dev/insert_tag.py <tag_name> <problem_name>

Inserts by line index with an alphabetical scan (quoted-string entries only,
so leading metadata objects are skipped), then verifies nothing shifted out of
order. Re-run `bake lint` afterwards: scripts/sort_tags.py is the real gate.
"""

import re
import sys

TAGS_PATH = "src/leetcode_py/cli/resources/leetcode/json/tags.json5"


def insert_tag(tag: str, name: str) -> None:
    with open(TAGS_PATH) as f:
        lines = f.read().splitlines()
    start = next(
        (i for i, line in enumerate(lines) if line.strip() == f"{tag}: ["),
        None,
    )
    if start is None:
        sys.exit(f"tag block not found: {tag}: [")
    end = next(i for i in range(start, len(lines)) if lines[i].strip() == "],")

    entries = [i for i in range(start + 1, end) if re.match(r'^"[a-z0-9_]+",?$', lines[i].strip())]
    after = [i for i in entries if lines[i].strip().strip('"').rstrip(",") > name]
    if not after:
        sys.exit(f"{name} sorts after every entry in {tag}; append manually")
    target = after[0]

    lines.insert(target, f'        "{name}",')
    with open(TAGS_PATH, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"inserted {name} into {tag} at line {target + 1}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    insert_tag(sys.argv[1], sys.argv[2])
