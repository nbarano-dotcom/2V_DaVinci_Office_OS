import os
import subprocess

def sync_vvinci_agents():
    """Synchronizuje postępy agentów ZAHIR i DIABOLINA z repozytorium GitHub."""
    try:
        print("🚀 Inicjacja synchronizacji daVVinci...")
        # Dodanie wszystkich zmian w folderze 2V_Office
        subprocess.run(["git", "add", "."], check=True)
        # Commit z flagą synchronizacji rady
        subprocess.run(["git", "commit", "-m", "SYNC: Rada Agentów (Diabolina, Zahir, Grok, OpenAI)"], check=True)
        print("✅ Synchronizacja lokalna zakończona. Gotowy na raporty od Groka i OpenAI.")
    except Exception as e:
        print(f"❌ Błąd synchronizacji: {e}")

if __name__ == "__main__":
    sync_vvinci_agents()
