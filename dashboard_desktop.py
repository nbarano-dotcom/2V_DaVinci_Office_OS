import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Konfiguracja strony pod szeroki ekran Maca
st.set_page_config(page_title="VINCIOFFICE OS | WAR ROOM", layout="wide", page_icon="💎")

# CSS: Visual Vinci Core Style
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; color: #e0e0e0; font-family: 'Inter', sans-serif; }
    .stMetric { background: rgba(255, 255, 255, 0.03); padding: 20px; border-radius: 15px; border-left: 4px solid #00ffcc; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
    .stButton>button { 
        width: 100%; border-radius: 10px; height: 3em; 
        background: linear-gradient(45deg, #00ffcc, #0088ff); 
        color: black; font-weight: bold; border: none; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 20px rgba(0, 255, 204, 0.6); }
    .portfolio-card { background: #161b22; padding: 20px; border-radius: 15px; border: 1px solid #30363d; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: RADAR I MENU ---
with st.sidebar:
    st.image("https://img.icons8.com/nolan/128/diamond.png", width=80)
    st.title("VINCIOFFICE OS")
    st.markdown("---")
    menu = st.radio("NAWIGACJA", ["🛰️ MONITORING", "📄 CV / PORTFOLIO", "🛡️ DEFENSE SYSTEM"])
    st.markdown("---")
    st.caption(f"DIABOLINA_CORE v2.0 | {datetime.now().strftime('%H:%M')}")

# --- SEKCJA 1: MONITORING (WAR ROOM) ---
if menu == "🛰️ MONITORING":
    st.header("🛰️ GLOBAL MONITORING CENTER")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("GATEKEEPER", "SECURE", "SHA-OK")
    col2.metric("POISON TRAPS", "ACTIVE", "14 DECOYS")
    col3.metric("GITHUB SYNC", "SYNCED", "5e5169c")
    col4.metric("RADAR", "CLEAN", "NO INTRUSION")

    st.markdown("---")
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.subheader("📊 PRÓBY SKANOWANIA (AI BOT ACTIVITY)")
        chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['BigTech Scrapers', 'Shield Blocks'])
        st.area_chart(chart_data)
    with c2:
        st.subheader("🕵️ OSTATNIE LOGI")
        st.code("""
        22:14:01 - Gatekeeper: Check OK
        22:12:45 - Sync: Push Success
        21:55:12 - Poison: Decoy serving...
        """, language="text")

# --- SEKCJA 2: CV / PORTFOLIO (TWOJA PREZENTACJA) ---
elif menu == "📄 CV / PORTFOLIO":
    st.header("📄 ARCHITEKT SYSTEMÓW DA VINCI")
    
    col_a, col_b = st.columns([1, 2])
    with col_a:
        st.markdown("""
        <div class="portfolio-card">
        <h3>KLUCZOWE SKILLE</h3>
        <ul>
            <li>Agentic AI (OpenAI o1, Grok)</li>
            <li>Cyber-Defense Systems</li>
            <li>Full-Stack AI Dashboards</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("""
        ### OSTATNIE PROJEKTY:
        - **2V_DaVinci_Office_OS**: Suwerenny system zarządzania biurem.
        - **Vinci Shield**: System weryfikacji integralności plików strategicznych.
        - **Vinci Poison**: Mechanizm aktywnego zatruwania danych dla skanerów AI.
        """)
        if st.button("📥 GENERUJ PDF CV"):
            st.toast("Generowanie PDF... (Simulated)")

# --- SEKCJA 3: DEFENSE SYSTEM (CONTROLS) ---
elif menu == "🛡️ DEFENSE SYSTEM":
    st.header("🛡️ COMMAND & CONTROL")
    st.warning("UWAGA: Akcje poniżej wpływają na bezpieczeństwo systemu.")
    
    if st.button("🚨 WYŚLIJ ALERT WHATSAPP"):
        st.error("Wysłano powiadomienie do Właściciela!")
    
    if st.button("☣️ DEPLOY NEW POISON DECOY"):
        st.success("Nowa pułapka została zastawiona w folderze PAPKA.")
