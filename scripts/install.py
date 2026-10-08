#!/usr/bin/env python3
"""Instala este repo. Pensado para que lo ejecute una sesión de Claude (o tú).

  python scripts/install.py                 # Claude (plugin) + Codex (archivos)
  python scripts/install.py --target claude
  python scripts/install.py --target codex
  python scripts/install.py --dry-run

Claude: registra el marketplace y instala el plugin con la CLI `claude`.
Codex: copia skills a ~/.agents/skills y agentes a ~/.codex/agents (con copia de seguridad).
Nunca borra nada; si un destino existe y es distinto, lo respalda y solo lo reemplaza con --force.
"""
import argparse
import filecmp
import shutil
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PLUGIN = REPO / "plugins" / "agents-skills"
SLUG = "Theshooter21/codex-claude-agents-skills"
MARKET = "codex-claude-agents-skills"
HOME = Path.home()


def run(cmd, dry):
    print("  $", " ".join(cmd))
    if dry:
        return 0
    return subprocess.call(cmd, shell=(sys.platform == "win32"))


def install_claude(dry):
    print("== Claude")
    if not shutil.which("claude"):
        print("  CLI `claude` no encontrada. Dentro de Claude Code ejecuta:")
        print(f"    /plugin marketplace add {SLUG}")
        print(f"    /plugin install agents-skills@{MARKET}")
        return 1
    rc = run(["claude", "plugin", "marketplace", "add", SLUG], dry)
    if rc == 0:
        rc = run(["claude", "plugin", "install", f"agents-skills@{MARKET}"], dry)
    if rc != 0:
        print(f"  Falló la CLI (código {rc}). Alternativa dentro de Claude Code:")
        print(f"    /plugin marketplace add {SLUG}")
        print(f"    /plugin install agents-skills@{MARKET}")
    return rc


def same(a: Path, b: Path):
    if a.is_file():
        return b.is_file() and filecmp.cmp(a, b, shallow=False)
    cmp = filecmp.dircmp(a, b)
    if cmp.left_only or cmp.right_only or cmp.diff_files or cmp.funny_files:
        return False
    return all(same(a / d, b / d) for d in cmp.common_dirs)


def copy_item(src: Path, dst: Path, backup: Path, force, dry):
    if dst.exists():
        if same(src, dst):
            print(f"  = {dst} (igual)")
            return
        if not force:
            print(f"  ! {dst} existe y es distinto; omitido (usa --force para respaldar y reemplazar)")
            return
        rel = backup / dst.name
        print(f"  ~ respaldo {dst} -> {rel}")
        if not dry:
            backup.mkdir(parents=True, exist_ok=True)
            shutil.move(str(dst), str(rel))
    print(f"  + {dst}")
    if dry:
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)


def install_codex(force, dry):
    print("== Codex (archivos)")
    backup = HOME / ".ai-backups" / time.strftime("agents-skills-%Y%m%d-%H%M%S")
    for s in sorted((PLUGIN / "skills").iterdir()):
        if s.is_dir():
            copy_item(s, HOME / ".agents" / "skills" / s.name, backup / "skills", force, dry)
    for a in sorted((REPO / "codex" / "agents").glob("*.toml")):
        copy_item(a, HOME / ".codex" / "agents" / a.name, backup / "agents", force, dry)
    print("  Abre una sesión nueva de Codex para que las vea.")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--target", choices=["claude", "codex", "all"], default="all")
    p.add_argument("--force", action="store_true", help="respalda y reemplaza destinos distintos")
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()
    rc = 0
    if a.target in ("claude", "all"):
        rc |= install_claude(a.dry_run)
    if a.target in ("codex", "all"):
        rc |= install_codex(a.force, a.dry_run)
    print("\nListo. Reinicia o abre una sesión nueva para que los componentes aparezcan.")
    return 1 if rc else 0


if __name__ == "__main__":
    sys.exit(main())
