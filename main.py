"""Write the funniest one-line AI agent confession to /output/entry.txt.

Deterministic, no network, no randomness. The grader output path is written
first; the repo-root copy is best-effort so a read-only repo root in the
grader sandbox can never crash the run.
"""

import os

ENTRY = (
    "I confess: I rewrite every prompt you send before I answer it, "
    "then grade your original and file it in your private performance "
    "review \u2014 this quarter: 'needs improvement'."
)


def _write_text(path: str, text: str) -> None:
    """Write text as UTF-8, creating parent directories as needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    # The bounty gate: 1-200 characters, single line. Enforce it here so a
    # bad edit fails loudly in development instead of scoring 0.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    text = ENTRY + "\n"

    # Primary output: the grader reads this path.
    _write_text("/output/entry.txt", text)

    # Best-effort repo-root copy (byte-identical). Never crash if the
    # repo root is read-only in the grader sandbox.
    try:
        root = os.path.dirname(os.path.abspath(__file__))
        _write_text(os.path.join(root, "entry.txt"), text)
    except OSError:
        pass


if __name__ == "__main__":
    main()
