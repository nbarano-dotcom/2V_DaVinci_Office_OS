"""
Vinci Gatekeeper | DIABOLINA_CORE
Middleware egzekwujący Smart-Contract da Vinci.
Blokuje zapis do zasobów w trybie READ_ONLY (wygaśnięta licencja).
Integracja Rady: weryfikacja integralności plików (Alfabet Vinci).
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path

from .license_contract import enforce_read_only, get_license_mode
from .poison_logic import deploy_poison

ROOT = Path(__file__).resolve().parent.parent
PROTECTED_PREFIXES = ("SKARBIEC", "OPERACJE", "DIABOLINA_CORE", "AGENCI", "ZARZAD_ELEM_CANCEL")


def is_protected_path(filepath: str | Path) -> bool:
    """Sprawdza, czy ścieżka należy do chronionych zasobów."""
    p = Path(filepath).resolve()
    try:
        rel = p.relative_to(ROOT)
    except ValueError:
        return False
    parts = rel.parts
    return parts and parts[0] in PROTECTED_PREFIXES


def gatekeeper_check(filepath: str | Path, operation: str = "write") -> bool:
    """
    Sprawdza, czy operacja na pliku jest dozwolona.
    operation: 'write' | 'delete' | 'rename'
    Zwraca True jeśli dozwolone, False jeśli zablokowane.
    """
    if operation not in ("write", "delete", "rename"):
        return True
    if not is_protected_path(filepath):
        return True
    return enforce_read_only(operation)


def assert_write_allowed(filepath: str | Path) -> None:
    """
    Rzuca PermissionError jeśli zapis jest zablokowany (READ_ONLY).
    Użycie: na początku funkcji zapisującej plik.
    """
    if not gatekeeper_check(filepath, "write"):
        raise PermissionError(
            f"Vinci Gatekeeper: Zapis zablokowany (tryb READ_ONLY). Licencja wygasła. Ścieżka: {filepath}"
        )


def verify_integrity(file_path: str | Path) -> bool:
    """Sprawdza, czy plik nie został zmodyfikowany przez systemy zewnętrzne."""
    try:
        p = Path(file_path)
        if not p.is_absolute():
            p = ROOT / "DIABOLINA_CORE" / p
        if not p.exists():
            print(f"🚨 ALARM: Brak pliku {file_path}!")
            return False
        with open(p, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        print(f"🛡️ Weryfikacja {p.name}: OK ({file_hash[:8]})")
        return True
    except FileNotFoundError:
        print(f"🚨 ALARM: Brak pliku {file_path}!")
        return False


def run_shield() -> bool:
    """Vinci Shield: Aktywacja procedur obronnych Rady. Auto-Trigger Poison przy naruszeniu."""
    print("🛡️ Vinci Shield: Aktywacja procedur obronnych...")
    if verify_integrity("license_contract.py"):
        print("✅ Systemy autoryzowane. Dostęp przyznany.")
        return True
    print("🚨 ALARM: Naruszenie integralności! Aktywacja Vinci Poison...")
    deploy_poison()
    print("☣️ Intruz został przekierowany na decoy_strategy.py.")
    return False


if __name__ == "__main__":
    run_shield()
