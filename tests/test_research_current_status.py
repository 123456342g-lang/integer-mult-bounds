"""The status page's only "current" section must agree with the selected record."""

import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "docs/research/current-status.md"
SELECTED = json.loads((ROOT / "certificates/selected-result.json").read_text())


def headings(text):
    """ATX headings outside fenced code blocks, as (line index, text)."""
    out, fenced = [], False
    for i, line in enumerate(text.splitlines()):
        if line.startswith("```"):
            fenced = not fenced
        elif not fenced and re.match(r"#{1,6} ", line):
            out.append((i, line))
    return out


class CurrentStatusTests(unittest.TestCase):
    def setUp(self):
        self.text = STATUS.read_text()
        self.lines = self.text.splitlines()
        self.heads = headings(self.text)

    def test_only_the_first_heading_claims_current_or_selected(self):
        self.assertEqual(self.heads[0], (0, "# Current reviewed status"))
        stale = [h for _, h in self.heads[1:]
                 if re.search(r"\b(current|selected|next research)\b", h, re.IGNORECASE)]
        self.assertEqual(stale, [], "rename superseded headings to name their checkpoint")

    def test_current_section_matches_selected_record(self):
        end = self.heads[1][0]
        current = "\n".join(self.lines[:end])
        self.assertIn(f"**{SELECTED['decimal']}**", current)
        self.assertIn(Path(SELECTED["review"]).name, current)
        self.assertIn(f"`{SELECTED['reproduce']}`", current)

    def test_history_banner_precedes_historical_sections(self):
        end = self.heads[1][0]
        self.assertIn("historical snapshot", "\n".join(self.lines[:end]))
        self.assertIn("selected-result.json", "\n".join(self.lines[:end]))


if __name__ == "__main__":
    unittest.main()
