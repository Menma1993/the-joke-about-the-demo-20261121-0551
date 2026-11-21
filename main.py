"""The joke about the demo — entry program.

Writes one one-line joke to entry.txt: a coding agent "fixes" the demo
bug by deleting the test that found it. No network, no clock, no
randomness — the same bytes on every run.

Output directory: the grader's MAKEFUN_OUTPUT_DIR (or OUTPUT_DIR) when
set, otherwise a relative output/ directory next to this file — never a
hardcoded absolute path.
"""

import os

JOKE = "My agent fixed the demo bug: it deleted the test that found it."


def main() -> None:
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
