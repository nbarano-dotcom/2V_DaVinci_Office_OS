import streamlit as st
import pandas as pd
from datetime import datetime

# Konfiguracja strony
st.set_page_config(page_title="Vinci Office | Control Center", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS dla mrocznego stylu
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e0e0e0; }
    .stMetric { background-color: #1c1c1c; padding: 15px; border-radius: 10px; border: 1px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ VINCI OFFICE | DASHBOARD STRATEGICZNY")
st.markdown("---")

# SEKCJA 1: SKARBIEC (API & FINANSE)
st.subheader("💰 SKARBIEC")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("BUDŻET API", "184.50 / 400 EUR", "46.1%")
with c2:
    st.metric("DPD CZYNSZ", "97 367,80 PLN", "OCZEKUJE")
with c3:
    st.metric("POŻYCZKA RBL", "200 000 PLN", "TERM: 13.03", delta_color="inverse")
with c4:
    st.metric("PORY 80", "5.2 mln GBP", "DEPOZYT")

# SEKCJA 2: AKTYWA & RYZYKA
st.markdown("---")
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📂 STATUS AKTYWÓW (ASTON)")
    data = {
        "Aktywo": ["SMARKÓW (Hałda)", "ORZYSZ", "TARNOWSKIE GÓRY"],
        "Wycena": ["69.3 MLN PLN", "W TOKU", "12.5 MLN PLN"],
        "Status": ["OPERAT OK", "EGZEKUCJA", "DO NAPRAWY (DACH)"]
    }
    st.table(pd.DataFrame(data))

with col_right:
    st.subheader("⚖️ TERMINY KRYTYCZNE")
    st.error("🔥 13.03 - Aneks Pożyczki RBL")
    st.warning("⚖️ 17.03 - Rozprawa Ryczywolska")
    st.info("📅 31.03 - Zamknięcie Kwartału API")

# SEKCJA 3: STATUS AGENTÓW
st.markdown("---")
st.caption(f"System daVVincci online | Ostatnia synchronizacja: {datetime.now().strftime('%H:%M:%S')}")

