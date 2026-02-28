#!/bin/bash
cd ~/2V_Office

# 1. Odpal Dashboard na Maca (8501)
python3 -m streamlit run dashboard_vvinci.py --server.port 8501 &

# 2. Odpal APPKĘ na Telefon (8502)
python3 -m streamlit run PAPKA/app.py --server.port 8502 &

echo "💎 Systemy aktywne: Mac (8501) | Telefon (8502)"
