#!/bin/bash
cd ~/2V_Office

# 1. ZAMKNIJ STARE PROCESY (żeby nie było błędów z portami)
pkill -f streamlit

# 2. URUCHOM DASHBOARD (Port 8501) W TLE
nohup python3 -m streamlit run dashboard_vvinci.py --server.port 8501 --server.headless true > /dev/null 2>&1 &

# 3. URUCHOM APPKĘ (Port 8502) W TLE
nohup python3 -m streamlit run PAPKA/app.py --server.port 8502 --server.headless true > /dev/null 2>&1 &

# Czekamy 5 sekund, aż serwery "odetchną"
sleep 5

# 4. OTWÓRZ DASHBOARD W PRZEGLĄDARCE
open http://localhost:8501

echo "💎 Systemy aktywne: Dashboard (8501) | APPKA (8502)"
