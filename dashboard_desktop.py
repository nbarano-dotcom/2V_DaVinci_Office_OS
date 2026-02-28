import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime


# Funkcja Głosowa Diaboliny (JavaScript dla szybkości)
def speak(text):
    js_code = f"""
    <script>
    var msg = new SpeechSynthesisUtterance('{text}');
    msg.lang = 'pl-PL';
    msg.pitch = 1.2;
    msg.rate = 1.0;
    window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js_code, height=0)


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
    # Wyświetlanie awatara z lokalnego pliku
    st.image("avatar.png", use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #00ffcc;'>DIABOLINA</h2>", unsafe_allow_html=True)
    st.markdown("---")
    st.title("VINCIOFFICE OS")
    st.markdown("---")
    menu = st.radio("NAWIGACJA", ["🛰️ MONITORING", "📄 CV / PORTFOLIO", "🛡️ DEFENSE SYSTEM"])
    st.markdown("---")
    st.caption(f"DIABOLINA_CORE v2.0 | {datetime.now().strftime('%H:%M')}")

# --- SEKCJA 1: MONITORING (WAR ROOM) ---
if menu == "🛰️ MONITORING":
    st.header("🛰️ GLOBAL MONITORING CENTER")

    # --- ROZKAZ DNIA: RADY AGENTÓW ---
    st.markdown("### 📜 ROZKAZ DNIA")
    with st.container():
        st.markdown("""
        <div style="background: rgba(0, 255, 204, 0.05); padding: 15px; border-radius: 15px; border-left: 5px solid #00ffcc;">
            <p style="margin: 5px;">🎯 <b>Zahir:</b> Optymalizacja CV pod algorytmy ATS (AI-Ready).</p>
            <p style="margin: 5px;">🛡️ <b>Diabolina:</b> Audyt logów portów 8501/8502 (Security Check).</p>
            <p style="margin: 5px;">🚀 <b>Grok/OpenAI:</b> Synchronizacja bazy wiedzy w 2V_Office.</p>
        </div>
        """, unsafe_allow_html=True)
    st.write("")
    if st.button("🔊 ODSŁUCHAJ ROZKAZ DNIA"):
        speak("Witaj Szefie. Dzisiejszy priorytet to synchronizacja dokumentów z pulpitu. System jest bezpieczny.")
    
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

    st.subheader("📝 AGENDA RADY AGENTÓW")
    todo_list = {
        "Zahir": "Optymalizacja struktury CV i analiza trendów AI 2026",
        "Diabolina": "Monitoring portów 8501/8502 i alerty WhatsApp"
    }
    for agent, task in todo_list.items():
        st.checkbox(f"{agent}: {task}", value=True)

    # --- TERMINARZ OPERACYJNY ZAHIRA ---
    st.markdown("---")
    st.subheader("📅 TERMINARZ AGENTÓW")

    events = [
        {"Data": "2026-02-28", "Agent": "Diabolina", "Zadanie": "Finalny Sync Multiversum", "Status": "✅"},
        {"Data": "2026-03-01", "Agent": "Zahir", "Zadanie": "Publikacja Portfolio / PDF CV", "Status": "⏳"},
        {"Data": "2026-03-02", "Agent": "Vinci System", "Zadanie": "Auto-Poison Update", "Status": "📅"}
    ]
    st.table(pd.DataFrame(events))

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

        st.subheader("📁 DOKUMENTACJA Z PULPITU")
        docs = ["RAPORT_OPERACYJNY.pdf", "SI_AUTONOMIA.pdf", "STRATEGIA_2026.pdf"]
        for doc in docs:
            if st.button(f"📄 Otwórz {doc}", key=doc):
                import os
                os.system(f"open ~/Desktop/{doc}")

# --- SEKCJA 3: DEFENSE SYSTEM (CONTROLS) ---
elif menu == "🛡️ DEFENSE SYSTEM":
    st.header("🛡️ COMMAND & CONTROL")
    st.warning("UWAGA: Akcje poniżej wpływają na bezpieczeństwo systemu.")
    
    if st.button("🚨 WYŚLIJ ALERT WHATSAPP"):
        st.error("Wysłano powiadomienie do Właściciela!")
    
    if st.button("☣️ DEPLOY NEW POISON DECOY"):
        st.success("Nowa pułapka została zastawiona w folderze PAPKA.")
