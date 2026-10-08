#!/usr/bin/env python3
"""Instala el plugin en Claude Code (registra el marketplace e instala agents-skills).

  python scripts/install.py            # instala desde GitHub
  python scripts/install.py --local    # instala desde este clon (para pruebas)
  python scripts/install.py --dry-run
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SLUG = "Theshooter21/codex-claude-agents-skills"
MARKET = "codex-claude-agents-skills"


def run(cmd, dry):
    print("  $", " ".join(cmd))
    return 0 if dry else subprocess.call(cmd, shell=(sys.platform == "win32"))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--local", action="store_true", help="usa este clon en vez de GitHub")
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()
    source = str(REPO) if a.local else SLUG
    if not shutil.which("claude"):
        print("CLI `claude` no encontrada. Dentro de Claude Code ejecuta:")
        print(f"  /plugin marketplace add {source}")
        print(f"  /plugin install agents-skills@{MARKET}")
        return 1
    rc = run(["claude", "plugin", "marketplace", "add", source], a.dry_run)
    if rc == 0:
        rc = run(["claude", "plugin", "install", f"agents-skills@{MARKET}"], a.dry_run)
    print("\nListo. Abre una sesión nueva de Claude Code." if rc == 0 else f"\nFalló (código {rc}).")
    return rc


if __name__ == "__main__":
    sys.exit(main())
