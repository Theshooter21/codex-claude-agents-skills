#!/usr/bin/env python3
"""Valida el repo: JSON, frontmatter, TOML, sincronía Claude/Codex y ausencia de datos privados."""
import json
import pathlib
import re
import sys
import tomllib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "agents-skills"
errors = []


def err(msg):
    errors.append(msg)


def frontmatter(path):
    m = re.match(r"---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    if not m:
        err(f"{path}: sin frontmatter")
        return {}
    return dict(
        (k.strip(), v.strip())
        for k, _, v in (ln.partition(":") for ln in m.group(1).splitlines() if ":" in ln)
    )


for j in [ROOT / ".claude-plugin" / "marketplace.json", PLUGIN / ".claude-plugin" / "plugin.json"]:
    try:
        json.loads(j.read_text(encoding="utf-8"))
    except Exception as e:
        err(f"{j}: JSON inválido ({e})")

for d in sorted((PLUGIN / "skills").iterdir()):
    f = d / "SKILL.md"
    if not f.exists():
        err(f"{d}: falta SKILL.md")
        continue
    fm = frontmatter(f)
    if fm.get("name") != d.name:
        err(f"{f}: name '{fm.get('name')}' != directorio '{d.name}'")
    if not fm.get("description"):
        err(f"{f}: sin description")

claude = {p.stem for p in (PLUGIN / "agents").glob("*.md")}
codex = {p.stem for p in (ROOT / "codex" / "agents").glob("*.toml")}
if claude != codex:
    err(f"agentes desincronizados: {sorted(claude ^ codex)}")
for p in (PLUGIN / "agents").glob("*.md"):
    fm = frontmatter(p)
    if fm.get("name") != p.stem or not fm.get("description"):
        err(f"{p}: frontmatter incorrecto")
for p in (ROOT / "codex" / "agents").glob("*.toml"):
    try:
        t = tomllib.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        err(f"{p}: TOML inválido ({e})")
        continue
    for k in ("name", "description", "developer_instructions"):
        if not t.get(k):
            err(f"{p}: falta {k}")

# Datos privados / secretos
bad = re.compile(
    r"automec|C:\\Users\\|C:/Users/|/home/\w+|eduvi|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}",
    re.I,
)
for p in ROOT.rglob("*"):
    if p.is_file() and ".git" not in p.parts and p.suffix in {".md", ".json", ".toml", ".py", ".txt", ""}:
        if p.name in {"validate.py"}:
            continue
        for i, ln in enumerate(p.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            if bad.search(ln):
                err(f"{p.relative_to(ROOT)}:{i}: posible dato privado: {ln.strip()[:80]}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(claude)} agentes, {len(list((PLUGIN / 'skills').iterdir()))} skills")
