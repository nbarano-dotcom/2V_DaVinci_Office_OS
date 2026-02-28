"""
Smart-Contract da Vinci | DIABOLINA_CORE
Automatyczne przełączenie zasobów w tryb Read-Only przy wygaśnięciu licencji.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

# Ścieżka do pliku licencji (w root 2V_Office)
ROOT = Path(__file__).resolve().parent.parent
LICENSE_FILE = ROOT / ".vvinci_license.json"
DEFAULT_SCOPE = ["SKARBIEC", "OPERACJE", "DIABOLINA_CORE", "AGENCI"]


def _now_utc() -> datetime:
    """Aktualny czas UTC."""
    return datetime.now(timezone.utc)


def load_license() -> dict | None:
    """Wczytuje plik licencji. Zwraca None jeśli brak lub błąd."""
    if not LICENSE_FILE.exists():
        return None
    try:
        with open(LICENSE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def license_valid() -> bool:
    """
    Główna logika Smart-Contractu da Vinci.
    Zwraca True jeśli licencja jest ważna (READ_WRITE), False jeśli wygasła (READ_ONLY).
    """
    lic = load_license()
    if not lic:
        # Brak pliku = tryb dev / grace period → domyślnie READ_WRITE
        return True

    expiry_str = lic.get("expiry")
    if not expiry_str:
        return True

    try:
        expiry = datetime.fromisoformat(expiry_str.replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return True

    return _now_utc() < expiry


def get_license_mode() -> str:
    """Zwraca 'read_write' lub 'read_only'."""
    return "read_write" if license_valid() else "read_only"


def get_license_info() -> dict:
    """Zwraca informacje o licencji (do dashboardu / logów)."""
    lic = load_license()
    if not lic:
        return {"status": "NO_LICENSE", "mode": "read_write", "expiry": None}
    valid = license_valid()
    return {
        "status": "VALID" if valid else "EXPIRED",
        "mode": "read_write" if valid else "read_only",
        "expiry": lic.get("expiry"),
        "licensee": lic.get("licensee", "Unknown"),
        "license_id": lic.get("license_id", ""),
    }


def enforce_read_only(operation: str) -> bool:
    """
    Sprawdza, czy operacja zapisu jest dozwolona.
    Zwraca True jeśli zapis OK, False jeśli blokada (READ_ONLY).
    """
    if license_valid():
        return True
    # READ_ONLY: blokada zapisu
    return False


# Przykład pliku licencji (.vvinci_license.json):
# {
#   "license_id": "VVINCI-2V-2026-XXXX",
#   "licensee": "Profil 2V",
#   "expiry": "2026-12-31T23:59:59Z",
#   "scope": ["SKARBIEC", "OPERACJE", "DIABOLINA_CORE", "AGENCI"],
#   "signature": "<base64 GPG signature>"
# }
