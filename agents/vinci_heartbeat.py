import time
import subprocess

def run_agents():
    while True:
        print("Vinci Heartbeat: Budzenie Agentów...")
        subprocess.run(["python3", "agents/agent_prawny.py"])
        subprocess.run(["python3", "agents/bibliotekarz.py"])
        # Tu system sam sprawdza Google Drive i Keep co minutę
        time.sleep(60)

if __name__ == "__main__":
    run_agents()
