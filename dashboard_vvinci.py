import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide", page_title="Vinci Office OS - Rada Agentów")

st.title("🛡️ VINCI OFFICE OS - DASHBOARD OPERACYJNY")
st.markdown("---")

# Tworzymy 4 kolumny (4 okienka dla Agentów)
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.header("😈 DIABOLINA (Strategia)")
    st.info("Status: Analiza Kontekstu Chmurowego\n\nOstatnie: Operat Smarków - WYMAZANY. Focus: Fundacja Rodzinna.")
    if st.button("Wymuś Raport Strategiczny"):
        st.write("Generowanie raportu...")

with col2:
    st.header("⚖️ AGENT PRAWNY (Wolska/Emery)")
    if os.path.exists("LOGS/legal_audit.log"):
        with open("LOGS/legal_audit.log", "r") as f:
            logs = f.readlines()[-5:] # Ostatnie 5 linii
            for log in logs:
                st.warning(log)
    else:
        st.error("Błąd: Brak logów prawnych! Uruchom agents/agent_prawny.py")

with col3:
    st.header("👤 ZAHIR (Logistyka/Teren)")
    st.success("Operacja EXIT (Tarnowskie Góry): 85% gotowości\nStatus: Monitoring pooperacyjny.")
    st.image("https://via.placeholder.com/400x200?text=Mapa+Operacji+Vinci", caption="Podgląd Terenowy")

with col4:
    st.header("📚 BIBLIOTEKARZ (Baza Danych)")
    st.write("Indeksowanie Google Drive: AKTYWNE")
    st.progress(100)
    st.write("Ostatni sync: Przed chwilą (z GitHub)")

st.markdown("---")
st.write("Status Połączenia: **CORTEX AI CONNECTED** | Token GitHub: **ACTIVE**")
