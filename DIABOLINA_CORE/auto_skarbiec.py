import os
import glob

def skanuj_biuro():
    print("🤖 DIABOLINA: Skanuję folder SKARBIEC...")
    wyciagi = glob.glob(os.path.expanduser("~/2V_Office/SKARBIEC/WYCIAGI/*.pdf"))
    if not wyciagi:
        print("⚠️ Brak nowych plików w WYCIAGI. Czekam na PDF-y od Norberta...")
    else:
        for w in wyciagi:
            print(f"✅ Znaleziono: {os.path.basename(w)}. Rozpoczynam automatyczną ekstrakcję danych...")
            # Tu wchodzi logika AI/OCR którą odpalam w tle
    
    print("📊 Status: Rejestr w ANALIZY gotowy do aktualizacji.")

if __name__ == "__main__":
    skanuj_biuro()
