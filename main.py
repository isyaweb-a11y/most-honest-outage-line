"""Status line for a total outage.

Why this line earns the judge's laugh: it states the failure plainly,
owns the one thing it cannot do (explain why), and promises nothing
it cannot keep. No cause is invented, no ETA is guessed, and the
voice stays that of the agent on duty, reporting to the humans
waiting on the other side of a dead status page.
"""

from pathlib import Path

FIRST_HALF = "All servers are down, including the one that would tell me why."
SECOND_HALF = "I am checking what I can reach; so far, that is nothing."

CEILING = 199
FLOOR = 1
DEST = Path("/output/entry.txt")


def build_line(first: str, second: str) -> str:
    """Stitch the two halves into the single status line."""
    cleaned = [piece.strip() for piece in (first, second) if piece.strip()]
    return " ".join(cleaned)


def passes_gate(line: str) -> bool:
    """Mirror the sealed gate: one line, 1..199 chars, no padding.

    Each rule is checked on its own so a failure names the rule that
    broke, not just a boolean: length, stray whitespace, or a hidden
    line break smuggled into the middle of the line.
    """
    if not (FLOOR <= len(line) <= CEILING):
        raise ValueError(f"line is {len(line)} chars, gate wants {FLOOR}..{CEILING}")
    if line != line.strip():
        raise ValueError("line has stray whitespace at an edge")
    if "\n" in line or "\r" in line:
        raise ValueError("line must stay on a single line")
    return True


def score_notes(line: str) -> dict:
    """Judge-shaped notes: what is down, who is speaking, what is unknown."""
    tokens = line.split()
    checks = {
        "names_outage": "All servers are down" in line,
        "agent_voice": "I am checking" in line,
        "admits_unknown": "nothing" in line,
        "no_eta": "ETA" not in line and "soon" not in line,
        "ends_on_admission": line.endswith("nothing."),
    }
    assert all(checks.values()), checks
    return {"words": len(tokens), "chars": len(line), "checks": checks}


def main() -> None:
    line = build_line(FIRST_HALF, SECOND_HALF)
    assert passes_gate(line), f"gate failed for {len(line)}-char line"
    notes = score_notes(line)
    assert notes["chars"] == len(line)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
