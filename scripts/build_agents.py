#!/usr/bin/env python3
"""Genera plugins/agents-skills/agents/*.md desde _agents_data.py."""
import json
import pathlib

from _agents_data import AGENTS

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "plugins" / "agents-skills" / "agents"


def bullets(items):
    return "\n".join(f"- {i}" for i in items)


def body(a):
    return (
        f"# {a['title']}\n\n## Rol\n\n{a['role']}\n\n"
        f"## Responsabilidades\n\n{bullets(a['resp'])}\n\n"
        f"## Límites\n\n{bullets(a['limits'])}\n\n"
        f"## Formato de salida\n\n{bullets(a['output'])}\n\n"
        f"## Checklist\n\n{bullets(a['checks'])}\n"
    )


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for a in AGENTS:
        tools = "tools: Read, Grep, Glob\n" if a.get("readonly") else ""
        desc = json.dumps(a["description"], ensure_ascii=False)
        md = f"---\nname: {a['name']}\ndescription: {desc}\n{tools}---\n\n{body(a)}"
        (OUT / f"{a['name']}.md").write_text(md, encoding="utf-8", newline="\n")
    print(f"{len(AGENTS)} agentes generados")


if __name__ == "__main__":
    main()
