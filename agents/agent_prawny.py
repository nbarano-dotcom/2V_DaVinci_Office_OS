import datetime
import os

def run_audit():
    log_path = "LOGS/legal_audit.log"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = f"[{timestamp}] AUDYT: Sprawa Wolska/Emery - Aktywna. Operat Smarkow - WYMAZANY.\n"
    with open(log_path, "a") as f:
        f.write(status)
    print("Agent Prawny: Logi zaktualizowane.")

if __name__ == "__main__":
    run_audit()
