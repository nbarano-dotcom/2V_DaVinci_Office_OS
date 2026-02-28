# GŁÓWNY ANALITYK LOGICZNY | AUDYT TECHNICZNY
## daVVinci Virtual Council | VVINCI GENESIS & Architektura Agentów

**Data:** 28.02.2026  
**Zakres:** Alfabet Vinci (VVINCI GENESIS), sync_agents.py, Smart-Contract da Vinci

---

# CZĘŚĆ 1: AUDYT ODPORNOŚCI ALFABETU VINCI NA ATAKI STRIPPING

## 1.1 Koncepcja referencyjna

**Alfabet Vinci (VVINCI GENESIS):** Znakowanie każdego znaku UTF-8 unikalnym podpisem cyfrowym w celu ochrony know-how przed nieautoryzowanym trenowaniem LLM na danych daVVinci.

## 1.2 Klasy ataków stripping

| Typ ataku | Opis | Wpływ na watermark |
|-----------|------|---------------------|
| **Metadata stripping** | Usunięcie metadanych pliku (EXIF, XMP, custom attributes) | Całkowita utrata, jeśli podpis w metadata |
| **Format stripping** | Konwersja DOCX→TXT, PDF→TXT, HTML→plain | Utrata formatowania + ewentualnych invisible chars |
| **Zero-width removal** | Sanityzacja U+200B, U+200C, U+200D, U+2060, U+FE00–U+FE0F | **Natychmiastowa utrata** watermarków opartych na ZWC |
| **Unicode normalization** | NFC/NFD/NFKC/NFKD – ujednolicenie znaków | Może zmienić sekwencje combining chars |
| **Whitespace collapse** | Zamiana wielu spacji/tabów na jedną | Utrata watermarków w whitespace |
| **Copy-paste sanitization** | Wklejanie przez edytory (VS Code, Notepad) – często stripują invisible | Powszechny wektor |

## 1.3 Ocena odporności według warstw implementacji

### Warstwa A: Podpis w znakach zero-width (ZWC)
- **Odporność na stripping: NISKA (2/10)**
- Narzędzia typu "Zero-Width Character Remover", "Invisible Character Cleaner" usuwają je w jednym kliknięciu.
- LLM tokenizery często normalizują lub ignorują ZWC – dane i tak mogą "wyciec" bez watermarku.
- **Rekomendacja:** Nie stosować jako jedynej warstwy.

### Warstwa B: Podpis w metadanych pliku
- **Odporność na stripping: BARDZO NISKA (1/10)**
- Każda konwersja formatu (DOCX→TXT, PDF→TXT), upload do chmury, e-mail – metadane znikają.
- **Rekomendacja:** Tylko jako warstwa dodatkowa (forensic trace), nie ochrona główna.

### Warstwa C: Podpis semantyczny (struktura + redundancja)
- **Odporność na stripping: ŚREDNIA–WYSOKA (6–8/10)**
- Watermark rozproszony w strukturze tekstu (np. wybór synonimów, kolejność elementów, wzorce w kodzie).
- Wymaga analizy statystycznej do wykrycia – trudniejsze do automatycznego stripowania.
- **Rekomendacja:** Główna warstwa ochrony dla Alfabetu Vinci.

### Warstwa D: Podpis w widocznym tekście (Alfabet jako notacja)
- **Odporność na stripping: WYSOKA (8/10)**
- Jeśli "Alfabet Vinci" to **widoczna, unikalna notacja/schema** (np. prefiksy, konwencje nazewnictwa, struktura katalogów) – usunięcie = zniszczenie użyteczności treści.
- Stripping wymagałby refaktoryzacji semantycznej – kosztowne i wykrywalne.
- **Rekomendacja:** Fundament – Alfabet jako **wartość użyteczna**, nie ukryta steganografia.

## 1.4 Wnioski i rekomendacje dla VVINCI GENESIS

1. **Architektura wielowarstwowa:** ZWC + metadata = forensic trace (kto, kiedy); struktura + Alfabet = ochrona główna.
2. **Unikać uzależnienia od ZWC:** Traktować jako "drugą linię", nie pierwszą.
3. **Alfabet jako brand:** Siła w **użyteczności i dokumentacji** – trudniejsze do skopiowania niż sam watermark.
4. **Test stripping:** Wprowadzić pipeline CI: każdy eksport danych przez "strip pipeline" (normalizacja Unicode, usunięcie ZWC) – mierzyć wykrywalność watermarku po stripowaniu.

---

# CZĘŚĆ 2: OPTYMALIZACJA sync_agents.py (GITHUB_SYNC)

## 2.1 Cele: niezaprzeczalność commitów w architekturze rozproszonej

- **Non-repudiation:** Każdy commit musi być kryptograficznie podpisany (GPG).
- **Integralność:** Weryfikacja przed push – brak unsigned commits.
- **Audit trail:** Log każdej synchronizacji z timestamp i hashem commitów.
- **Agent attribution:** Identyfikacja, który agent (Zahir, Diabolina, Compliance) wykonał sync.

## 2.2 Implementacja

Plik: `AGENCI/GITHUB_SYNC/sync_agents.py` – zaimplementowano w repozytorium.

### Kluczowe elementy:
- GPG signing (`git commit -S`) – wymaga skonfigurowanego `user.signingkey`
- Weryfikacja przed push: `git log --show-signature` – odrzucenie unsigned
- Rejestr w `LOGS/SYNC_AUDIT.log` – timestamp, agent, hash, status
- Fallback: jeśli GPG nie skonfigurowany – warning + opcja `--no-verify` (tylko dev)

---

# CZĘŚĆ 3: STRUKTURA LOGICZNA SMART-CONTRACTU DA VINCI

## 3.1 Cel

Automatyczne przełączenie zasobów w tryb **Read-Only** w przypadku wygaśnięcia licencji. Brak możliwości zapisu = egzekucja licencji bez centralnego serwera.

## 3.2 Komponenty logiczne

```
┌─────────────────────────────────────────────────────────────────┐
│                    SMART-CONTRACT DA VINCI                       │
├─────────────────────────────────────────────────────────────────┤
│  INPUTS:                                                         │
│  • license_expiry_date (ISO 8601)                                │
│  • license_key_hash (SHA-256) – opcjonalna weryfikacja           │
│  • current_timestamp (NTP lub system)                            │
│  • resource_manifest (lista ścieżek: SKARBIEC, OPERACJE, ...)    │
├─────────────────────────────────────────────────────────────────┤
│  LOGIC:                                                          │
│  IF current_timestamp >= license_expiry_date:                    │
│      mode = READ_ONLY                                            │
│  ELSE:                                                           │
│      mode = READ_WRITE                                           │
│  END                                                             │
├─────────────────────────────────────────────────────────────────┤
│  OUTPUTS / ACTIONS:                                              │
│  • mode → przekazany do Vinci Gatekeeper (middleware)            │
│  • READ_ONLY:                                                    │
│      - Blokada: git commit, git push, zapis plików w SKARBIEC,   │
│        OPERACJE, DIABOLINA_CORE                                  │
│      - Dozwolone: git pull, odczyt plików, uruchomienie dashboard│
│  • READ_WRITE: pełny dostęp                                     │
├─────────────────────────────────────────────────────────────────┤
│  ENFORCEMENT POINTS:                                             │
│  • sync_agents.py – sprawdza mode przed commit/push              │
│  • Vinci Gatekeeper (wrapper przy zapisie plików)                │
│  • dashboard_vvinci.py – ukrycie/disable przycisków edycji      │
└─────────────────────────────────────────────────────────────────┘
```

## 3.3 Plik licencji (struktura)

```json
{
  "license_id": "VVINCI-2V-2026-XXXX",
  "licensee": "Profil 2V",
  "expiry": "2026-12-31T23:59:59Z",
  "scope": ["SKARBIEC", "OPERACJE", "DIABOLINA_CORE", "AGENCI"],
  "signature": "<base64 GPG signature of above>"
}
```

## 3.4 Miejsca egzekucji (enforcement)

| Punkt | Akcja przy READ_ONLY |
|-------|----------------------|
| `sync_agents.py` | Odmowa `git commit` / `git push` |
| Vinci Gatekeeper (nowy moduł) | Intercept zapisu pliku → sprawdza `license_valid()` → blokada |
| `dashboard_vvinci.py` | `st.session_state["license_mode"] = "read_only"` → ukrycie formularzy edycji |
| Aplikacja `.app` | Przy starcie: sprawdzenie licencji → jeśli expired, uruchom tylko w trybie podglądu |

## 3.5 Ograniczenia (brutalnie szczere)

- **Offline bypass:** Użytkownik może cofnąć zegar systemowy – wymaga okresowej weryfikacji online lub hardware TPM.
- **Kopiowanie plików:** Read-Only blokuje zapis *w* Vinci, ale nie kopiowanie plików *poza* system – to ograniczenie koncepcyjne.
- **Git local:** `git commit` można wykonać lokalnie mimo blokady – enforcement musi być w `sync_agents.py` przed push, oraz w pre-commit hook.

---

*Audyt przygotowany przez GŁÓWNEGO ANALITYKA LOGICZNEGO | daVVinci Virtual Council*
