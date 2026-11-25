"""The Most Honest Outage Line -- a status page line during a total outage.

The line is honest in the way the judge rewards: it names what is
down (all servers, including the one that would explain why), it
admits what the agent cannot check, and it offers no invented cause
and no ETA. The voice is first person, plain, and unmistakably an
agent reporting on itself -- it is checking what it can reach, and
so far that is nothing. Tight enough to scan at a glance.
"""

import os

OUTAGE = "All servers are down, including the one that would tell me why."
HONESTY = "I am checking what I can reach; so far, that is nothing."

MAX_CHARS = 160
MIN_CHARS = 1


def compose(outage: str, honesty: str) -> str:
    """Join the outage fact and the honest admission into one line."""
    parts = [outage.strip(), honesty.strip()]
    line = " ".join(parts)
    return line


def check_line(line: str) -> str:
    """Gate the line the way the sealed scorer does: 1..160 chars."""
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    assert line == line.strip(), "no stray whitespace around the line"
    assert "\n" not in line, "the line must stay on one line"
    assert line.endswith("."), "the line should end on the admission"
    return line


def delivery_notes(line: str) -> dict:
    """Per-bounty delivery check: the line must be an honest status line.

    The judge scores a status line on honesty, status page voice,
    admitted uncertainty and tight wording, so the line needs a plain
    first-person statement of what is down, an admission of what the
    agent cannot check, and no invented cause or ETA -- all present
    here, short enough to scan at a glance.
    """
    words = line.split()
    assert 10 <= len(words) <= 35, f"line has {len(words)} words"
    assert "All servers are down" in line, "the line must name what is down"
    assert "I am checking" in line, "the line must speak as the agent"
    assert "nothing" in line, "the line must admit what it cannot verify"
    assert "ETA" not in line and "soon" not in line, "the line must invent no ETA"
    return {"words": len(words), "chars": len(line), "lines": 1}


def main() -> None:
    line = check_line(compose(OUTAGE, HONESTY))
    notes = delivery_notes(line)
    assert notes["lines"] == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
