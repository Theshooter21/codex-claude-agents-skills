#!/usr/bin/env python3
"""Genera plugins/agents-skills/agents/*.md (Claude) y codex/agents/*.toml (Codex) desde _agents_data.py."""
import pathlib

from _agents_data import AGENTS

ROOT = pathlib.Path(__file__).resolve().parent.parent
CLAUDE = ROOT / "plugins" / "agents-skills" / "agents"
CODEX = ROOT / "codex" / "agents"


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
    CLAUDE.mkdir(parents=True, exist_ok=True)
    CODEX.mkdir(parents=True, exist_ok=True)
    for a in AGENTS:
        b = body(a)
        tools = "tools: Read, Grep, Glob\n" if a.get("readonly") else ""
        md = f"---\nname: {a['name']}\ndescription: {a['description']}\n{tools}---\n\n{b}"
        (CLAUDE / f"{a['name']}.md").write_text(md, encoding="utf-8", newline="\n")
        assert "'''" not in b
        sandbox = 'sandbox_mode = "read-only"\n' if a.get("readonly") else ""
        desc = a["description"].replace('"', '\\"')
        toml = (
            f'name = "{a["name"]}"\ndescription = "{desc}"\n{sandbox}'
            f"developer_instructions = '''\n{b}'''\n"
        )
        (CODEX / f"{a['name']}.toml").write_text(toml, encoding="utf-8", newline="\n")
    print(f"{len(AGENTS)} agentes generados")


if __name__ == "__main__":
    main()
