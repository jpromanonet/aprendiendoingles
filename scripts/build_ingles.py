"""Arma data/lexicon.json y data/a1.json ... c2.json para el curso de inglés británico (England)."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from course_upper import A1_SPECS, bind  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def main():
    from course_bind import extra_lessons, extra_words

    lexicon, a1_lessons = bind(A1_SPECS, 1)
    for level, rows in extra_words().items():
        lexicon += rows

    seen = set()
    for item in lexicon:
        if item["hanzi"] in seen:
            raise SystemExit("repetida: " + item["hanzi"])
        seen.add(item["hanzi"])

    courses = {1: a1_lessons, **extra_lessons()}

    missing = []
    for classes in courses.values():
        for item in classes:
            for pin in item["pins"]:
                if pin not in seen:
                    missing.append(pin)
    if missing:
        raise SystemExit("pins fuera del léxico: " + ", ".join(missing))

    by_level = {}
    for item in lexicon:
        by_level.setdefault(item["level"], set()).add(item["hanzi"])
    names = {1: "a1", 2: "a2", 3: "b1", 4: "b2", 5: "c1", 6: "c2"}
    for level, classes in courses.items():
        if len(classes) != 12:
            raise SystemExit(f"{names[level]} tiene {len(classes)} clases")
        pinned = [pin for item in classes for pin in item["pins"]]
        unknown = sorted({pin for pin in pinned if pin not in by_level[level]})
        if unknown:
            raise SystemExit(f"{names[level]} pins ajenos: " + ", ".join(unknown))
        uncovered = sorted(by_level[level] - set(pinned))
        if uncovered:
            raise SystemExit(f"{names[level]} sin clase: " + ", ".join(uncovered))

    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data" / "lexicon.json").write_text(
        json.dumps(lexicon, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    counts = []
    for level, classes in courses.items():
        path = ROOT / "data" / f"{names[level]}.json"
        path.write_text(json.dumps(classes, ensure_ascii=False, indent=2), encoding="utf-8")
        counts.append(f"{names[level].upper()} {len(classes)}")
    per_level = " ".join(f"{names[level].upper()}={len(words)}" for level, words in sorted(by_level.items()))
    print(f"lexico {len(lexicon)} ({per_level}) " + " ".join(counts))


if __name__ == "__main__":
    main()
