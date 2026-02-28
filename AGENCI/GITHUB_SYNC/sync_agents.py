#!/usr/bin/env python3
"""
sync_agents.py | daVVinci GITHUB_SYNC
Synchronizacja agentów ZAHIR, DIABOLINA, Compliance z repozytorium GitHub.
Optymalizacja: GPG signing dla niezaprzeczalności commitów (non-repudiation).
"""

import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Ścieżki względem root 2V_Office
ROOT = Path(__file__).resolve().parent.parent.parent
AUDIT_LOG = ROOT / "LOGS" / "SYNC_AUDIT.log"
AGENT_ID = os.environ.get("VVINCI_AGENT", "UNKNOWN")  # ZAHIR | DIABOLINA | COMPLIANCE


def license_allows_write() -> bool:
    """Smart-Contract da Vinci: czy licencja pozwala na zapis (commit/push)."""
    try:
        sys.path.insert(0, str(ROOT))
        from DIABOLINA_CORE.license_contract import license_valid
        return license_valid()
    except Exception:
        return True  # Fallback: brak modułu = zezwól (dev)


def ensure_log_dir():
    """Tworzy katalog LOGS jeśli nie istnieje."""
    AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)


def log_audit(agent: str, action: str, status: str, detail: str = ""):
    """Zapisuje wpis do rejestru audytu synchronizacji."""
    ensure_log_dir()
    ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"{ts} | {agent} | {action} | {status} | {detail}\n"
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(line)


def run_git(args: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    """Uruchamia komendę git. cwd domyślnie ROOT."""
    return subprocess.run(
        ["git"] + args,
        cwd=cwd or ROOT,
        capture_output=True,
        text=True,
    )


def is_gpg_configured() -> bool:
    """Sprawdza, czy Git ma skonfigurowany klucz GPG do podpisywania."""
    r = run_git(["config", "--get", "user.signingkey"])
    return r.returncode == 0 and bool(r.stdout.strip())


def has_unsigned_commits() -> bool:
    """Sprawdza, czy są niepodpisane commity w historii (ostatnie 5)."""
    r = run_git(["log", "-5", "--show-signature", "--format=%G?"])
    if r.returncode != 0:
        return True  # W razie błędu traktuj jako unsigned
    return "N" in r.stdout or "U" in r.stdout  # N=no key, U=unverified


def get_last_commit_hash() -> str:
    """Zwraca hash ostatniego commita."""
    r = run_git(["rev-parse", "HEAD"])
    return r.stdout.strip()[:12] if r.returncode == 0 else ""


def sync_agents(allow_unsigned: bool = False, skip_push: bool = False) -> bool:
    """
    Synchronizuje postępy agentów z repozytorium GitHub.
    Wymaga GPG do podpisywania commitów (non-repudiation).
    """
    os.chdir(ROOT)

    # Smart-Contract da Vinci: blokada przy wygasłej licencji (READ_ONLY)
    if not license_allows_write():
        print("🔒 Vinci Gatekeeper: Licencja wygasła. Tryb READ_ONLY – commit/push zablokowane.")
        log_audit(AGENT_ID, "SYNC_ABORT", "LICENSE_EXPIRED", "Read-Only mode")
        return False

    if not is_gpg_configured() and not allow_unsigned:
        print("⚠️  GPG nie skonfigurowany. Ustaw: git config --global user.signingkey <KEY_ID>")
        print("   Uruchom z --allow-unsigned aby pominąć (tylko dev).")
        log_audit(AGENT_ID, "SYNC_ABORT", "NO_GPG", "GPG signing required")
        return False

    try:
        print("🚀 Inicjacja synchronizacji daVVinci...")
        log_audit(AGENT_ID, "SYNC_START", "OK", "")

        # Sprawdź status
        r = run_git(["status", "--porcelain"])
        if not r.stdout.strip():
            print("📭 Brak zmian do commitowania.")
            log_audit(AGENT_ID, "SYNC_SKIP", "NO_CHANGES", "")
            return True

        # git add
        run_git(["add", "."])
        if run_git(["diff", "--cached", "--quiet"]).returncode != 0:
            pass  # są zmiany

        # git commit z podpisem GPG (jeśli skonfigurowany)
        sign_flag = ["-S"] if is_gpg_configured() else []
        msg = f"Update: Synchronizacja agentów ({AGENT_ID}) | {datetime.utcnow().strftime('%Y-%m-%d %H:%M')}"
        rc = run_git(["commit", "-m", msg] + sign_flag)
        if rc.returncode != 0:
            if "nothing to commit" in (rc.stdout + rc.stderr).lower():
                print("📭 Brak zmian do commitowania.")
                log_audit(AGENT_ID, "SYNC_SKIP", "NO_CHANGES", "")
                return True
            print(f"❌ Błąd commita: {rc.stderr}")
            log_audit(AGENT_ID, "COMMIT_FAIL", "ERROR", rc.stderr[:200])
            return False

        commit_hash = get_last_commit_hash()
        log_audit(AGENT_ID, "COMMIT_OK", "SIGNED" if sign_flag else "UNSIGNED", commit_hash)

        # Weryfikacja przed push (opcjonalnie)
        if is_gpg_configured() and has_unsigned_commits():
            print("⚠️  Wykryto niepodpisane commity w historii. Push zablokowany (non-repudiation).")
            log_audit(AGENT_ID, "PUSH_BLOCK", "UNSIGNED_HISTORY", "")
            return False

        # git push
        if not skip_push:
            rc = run_git(["push", "origin", "main"])
            if rc.returncode != 0:
                print(f"❌ Błąd push: {rc.stderr}")
                log_audit(AGENT_ID, "PUSH_FAIL", "ERROR", rc.stderr[:200])
                return False
            log_audit(AGENT_ID, "PUSH_OK", "OK", commit_hash)
        else:
            print("⏸️  Push pominięty (--skip-push).")
            log_audit(AGENT_ID, "PUSH_SKIP", "SKIP", commit_hash)

        print("✅ Synchronizacja zakończona pomyślnie.")
        return True

    except Exception as e:
        print(f"❌ Błąd synchronizacji: {e}")
        log_audit(AGENT_ID, "SYNC_ERROR", "EXCEPTION", str(e)[:200])
        return False


if __name__ == "__main__":
    allow_unsigned = "--allow-unsigned" in sys.argv
    skip_push = "--skip-push" in sys.argv
    ok = sync_agents(allow_unsigned=allow_unsigned, skip_push=skip_push)
    sys.exit(0 if ok else 1)
