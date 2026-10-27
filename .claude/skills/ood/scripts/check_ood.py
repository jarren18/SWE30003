"""Deterministic checks for the rubric penalties in the Assignment 2 object design document.

Each check maps to a rubric line that deducts marks mechanically, so these run as a gate
before any model-based grading. The document must follow the design contract in
.claude/skills/ood/SKILL.md (Mermaid diagrams, "CRC Card: <Class>" headings, CRC tables).

Usage:  python .claude/skills/ood/scripts/check_ood.py Assignment2/build/FINAL_OOD.md
Exit:   0 = no errors (warnings allowed), 1 = errors found, 2 = unusable input
"""
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = {
    "Executive Summary": r"executive summary",
    "Introduction": r"introduction",
    "Assumptions": r"assumption",
    "Problem Analysis": r"problem analysis",
    "Simplifications": r"simplification",
    "Candidate Classes": r"candidate class",
    "Class Diagram": r"class diagram",
    "Discarded Classes": r"discarded",
    "CRC Cards": r"crc cards",
    "Design Heuristics": r"heuristic",
    "Design Patterns": r"design pattern",
    "Bootstrap Process": r"bootstrap",
    "Verification": r"verification",
    "References": r"reference",
}
MIN_SCENARIOS = 4
IDENT = r"[A-Za-z_]\w*"
NONE_MARKERS = {"", "-", "—", "–", "none", "n/a", "na"}

CLASS_SKIP = re.compile(r"^(classDiagram|direction|note|%%|style|classDef|cssClass|click|link|callback|namespace|\})")
CLASS_ARROW = re.compile(r"(<\|--|--\|>|<\|\.\.|\.\.\|>|\*--|--\*|o--|--o|-->|<--|\.\.>|<\.\.|--|\.\.)")
SEQ_DECL = re.compile(rf"^(?:create\s+)?(participant|actor)\s+({IDENT})(?:\s+as\s+(.+))?$")
SEQ_MSG = re.compile(rf"^({IDENT})\s*(-{{1,2}}(?:>>|>|x|\)))\s*[+-]?\s*({IDENT})\s*:(.*)$")


class Report:
    def __init__(self):
        self.errors, self.warnings, self.info = [], [], []

    def error(self, criterion, msg):
        self.errors.append(f"[{criterion}] {msg}")

    def warn(self, criterion, msg):
        self.warnings.append(f"[{criterion}] {msg}")


def headings(text):
    """Return (level, title, start, end) for every Markdown heading, end = next heading of same or higher level."""
    found = [(len(m.group(1)), m.group(2).strip(), m.start()) for m in re.finditer(r"^(#{1,6})\s+(.+)$", text, re.M)]
    result = []
    for i, (level, title, start) in enumerate(found):
        end = next((s for lv, _, s in found[i + 1:] if lv <= level), len(text))
        result.append((level, title, start, end))
    return result


def section(text, heads, pattern):
    for level, title, start, end in heads:
        if re.search(pattern, title, re.I):
            return start, end
    return None


def mermaid_blocks(text):
    return [(m.start(), m.group(1)) for m in re.finditer(r"```mermaid\s*\n(.*?)```", text, re.S)]


def parse_class_diagram(src):
    classes, members, body_of = set(), [], None
    for raw in src.splitlines():
        line = raw.strip()
        if not line:
            continue
        if body_of:
            if line.startswith("}"):
                body_of = None
            elif not re.fullmatch(r"<<[^>]+>>", line):
                members.append((body_of, line))
            continue
        if CLASS_SKIP.match(line):
            continue
        m = re.match(rf"^class\s+({IDENT})(?:~[^~]*~)?(?:\[[^\]]*\])?(?::::\w+)?\s*(\{{)?(.*)$", line)
        if m:
            classes.add(m.group(1))
            if m.group(2):
                rest = m.group(3).strip()
                inner = rest.rstrip("}").strip()
                if inner and not re.fullmatch(r"<<[^>]+>>", inner):
                    members.append((m.group(1), inner))
                if not rest.endswith("}"):
                    body_of = m.group(1)
            continue
        m = re.match(rf"^<<[^>]+>>\s+({IDENT})$", line)
        if m:
            classes.add(m.group(1))
            continue
        unquoted = re.sub(r'"[^"]*"', " ", line)
        lhs = unquoted.split(":", 1)[0]
        if CLASS_ARROW.search(lhs):
            classes.update(p.strip() for p in CLASS_ARROW.split(lhs) if re.fullmatch(IDENT, p.strip()))
            continue
        m = re.match(rf"^({IDENT})\s*:\s*(.+)$", line)
        if m:
            classes.add(m.group(1))
            members.append((m.group(1), m.group(2)))
    return classes, members


def parse_sequence(src):
    """Return ({participant_id: class_name}, actor_ids, creation_steps)."""
    names, actors, used, creations = {}, set(), set(), 0
    for raw in src.splitlines():
        line = raw.strip()
        m = SEQ_DECL.match(line)
        if m:
            kind, pid, label = m.groups()
            name = (label or pid).strip().strip('"')
            name = name.split(":")[-1].strip() or pid
            first = re.match(IDENT, name)
            names[pid] = first.group(0) if first else pid
            if kind == "actor":
                actors.add(pid)
            if line.startswith("create"):
                creations += 1
            continue
        m = SEQ_MSG.match(line)
        if m:
            used.update((m.group(1), m.group(3)))
            if re.search(r"\b(create|creates|new|instantiate)\b|<<create>>|«create»", m.group(4), re.I):
                creations += 1
    for pid in used:
        names.setdefault(pid, pid)
    return names, actors, creations


def parse_crc_cards(text, heads):
    cards = {}
    for level, title, start, end in heads:
        m = re.search(rf"CRC Card:\s*({IDENT})", title)
        if m:
            cards[m.group(1)] = text[start:end]
    return cards


def check_crc(name, body, classes, report):
    crit = "5 CRC"
    if not re.search(r"\*\*\s*(super ?class|parent(?: class)?)\s*:?\s*\*\*", body, re.I):
        report.error(crit, f"{name}: missing **Superclass:** line (-1)")
    if not re.search(r"\*\*\s*description\s*:?\s*\*\*", body, re.I):
        report.error(crit, f"{name}: missing **Description:** line (-1)")
    rows = [r for r in body.splitlines() if r.strip().startswith("|")]
    header = next((i for i, r in enumerate(rows) if re.search(r"responsibilit", r, re.I) and re.search(r"collaborator", r, re.I)), None)
    if header is None:
        report.error(crit, f"{name}: no | Responsibility | Collaborators | table (-1)")
        return
    data = [r for r in rows[header + 1:] if not re.fullmatch(r"\|[\s:|-]+\|?", r.strip())]
    if not data:
        report.error(crit, f"{name}: CRC table has no responsibilities (-1)")
    for row in data:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) < 2 or not cells[0]:
            report.error(crit, f"{name}: malformed CRC row: {row.strip()}")
            continue
        responsibility, collaborators = cells[0], cells[1]
        if re.search(rf"\b{IDENT}\s*\([^)]*\)", responsibility):
            report.warn("6 Quality", f"{name}: responsibility reads like a method signature: '{responsibility}'")
        if not collaborators:
            report.error(crit, f"{name}: responsibility '{responsibility}' has an empty collaborator cell; write '—' if none (-1)")
            continue
        if collaborators.lower() in NONE_MARKERS:
            continue
        for collab in re.findall(r"\b[A-Z]\w*\b", collaborators):
            if collab not in classes:
                report.warn(crit, f"{name}: collaborator '{collab}' is not a class in the diagram (fine only if it is a named external system)")
    if len(data) > 9:
        report.warn("6 Quality", f"{name}: {len(data)} responsibilities; check it is not a god class")


def check(path):
    text = path.read_text(encoding="utf-8")
    heads = headings(text)
    report = Report()

    for label, pattern in REQUIRED_SECTIONS.items():
        if not section(text, heads, pattern):
            report.error("9 Coherence", f"no heading for '{label}'")
    if not re.search(r"(table of contents|^#+\s*contents)", text, re.I | re.M):
        report.warn("9 Coherence", "no table of contents found")
    if not re.search(r"assignment 1.{0,80}appendix|appendix.{0,120}assignment 1", text, re.I | re.S):
        report.error("10 Admin", "no statement that the Assignment 1 SRS is attached as an appendix (up to -5)")

    blocks = mermaid_blocks(text)
    class_blocks = [src for _, src in blocks if src.lstrip().startswith("classDiagram")]
    if not class_blocks:
        report.error("4 Classes", "no Mermaid classDiagram found")
        classes, members = set(), []
    else:
        classes, members = set(), []
        for src in class_blocks:
            c, m = parse_class_diagram(src)
            classes |= c
            members += m
    for owner, member in members:
        report.error("4 Classes", f"class diagram lists a member on {owner}: '{member}' (no attributes/methods/signatures; up to -5)")

    cards = parse_crc_cards(text, heads)
    for name in sorted(classes - cards.keys()):
        report.error("5 CRC", f"class '{name}' is in the diagram but has no CRC card (-4)")
    for name in sorted(cards.keys() - classes):
        report.error("4 Classes", f"CRC card '{name}' has no class in the diagram (inconsistent class list)")
    for name, body in sorted(cards.items()):
        check_crc(name, body, classes, report)

    span = section(text, heads, REQUIRED_SECTIONS["Candidate Classes"])
    if span:
        listed = text[span[0]:span[1]]
        for name in sorted(classes):
            if not re.search(rf"\b{name}\b", listed):
                report.warn("4 Classes", f"'{name}' is not mentioned in the Candidate Classes section text")

    def sequences_in(pattern):
        s = section(text, heads, pattern)
        if not s:
            return []
        return [src for pos, src in blocks if s[0] <= pos < s[1] and src.lstrip().startswith("sequenceDiagram")]

    def check_participants(src, crit, where):
        names, actors, creations = parse_sequence(src)
        for pid, name in sorted(names.items()):
            if pid not in actors and name not in classes:
                report.error(crit, f"{where}: participant '{name}' is not a defined class (-1)")
        return creations

    boot = sequences_in(REQUIRED_SECTIONS["Bootstrap Process"])
    if not boot:
        report.error("7 Bootstrap", "no Mermaid sequenceDiagram in the Bootstrap section")
    elif sum(check_participants(src, "7 Bootstrap", "bootstrap") for src in boot) == 0:
        report.warn("7 Bootstrap", "bootstrap diagram shows no creation steps (use 'create participant' or 'creates' messages)")

    scenarios = sequences_in(REQUIRED_SECTIONS["Verification"])
    if len(scenarios) < MIN_SCENARIOS:
        report.error("8 Verification", f"{len(scenarios)} sequence diagrams in Verification; need at least {MIN_SCENARIOS} (4 pts each)")
    for i, src in enumerate(scenarios, start=1):
        check_participants(src, "8 Verification", f"scenario {i}")
        if not re.search(r"^\s*(alt|opt)\b", src, re.M):
            report.warn("8 Verification", f"scenario {i} has no alt/opt branch; non-trivial scenarios should show validation or failure handling")

    for ref in sorted(set(re.findall(r"\b(?:Section|Figure|Table)\s+(\d+(?:\.\d+)*)", text))):
        if not re.search(rf"^#+\s*{re.escape(ref)}[\s.]", text, re.M) and not re.search(rf"(Figure|Table)\s+{re.escape(ref)}\s*[:.–—-]", text):
            report.warn("9 Coherence", f"cross-reference to '{ref}' has no matching numbered heading or caption")

    print(f"Checked {path}")
    print(f"Classes in diagram: {len(classes)} | CRC cards: {len(cards)} | Verification scenarios: {len(scenarios)} | Bootstrap diagrams: {len(boot)}")
    print(f"\nERRORS ({len(report.errors)})")
    print("\n".join(f"  - {e}" for e in report.errors) or "  none")
    print(f"\nWARNINGS ({len(report.warnings)})")
    print("\n".join(f"  - {w}" for w in report.warnings) or "  none")
    return 1 if report.errors else 0


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 2 or not Path(sys.argv[1]).is_file():
        print(__doc__)
        return 2
    return check(Path(sys.argv[1]))


if __name__ == "__main__":
    sys.exit(main())
