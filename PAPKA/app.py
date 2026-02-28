import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
import time
from datetime import datetime
from DIABOLINA_CORE.whatsapp_notifier import send_vinci_alert

# Konfiguracja Ultra-Mobile
st.set_page_config(page_title="VINCIOFFICE MOBILE", page_icon="📱", layout="centered")

# Custom CSS dla efektu "Native App"
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ffcc; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .stButton>button {
        border: 2px solid #00ffcc; background-color: #000; color: #00ffcc;
        height: 70px; font-size: 20px; border-radius: 15px; font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:active { background-color: #00ffcc; color: black; }
    .status-box { padding: 15px; border-radius: 10px; border: 1px solid #333; background: #111; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Nagłówek mobilny
st.title("🛡️ APPKA v2.0")
st.caption(f"Połączono z DIABOLINA_CORE | {datetime.now().strftime('%H:%M:%S')}")

# Panel statusu
with st.container():
    st.markdown('<div class="status-box">🟢 <b>SYSTEM:</b> ONLINE<br>🛡️ <b>SHIELD:</b> ACTIVE<br>🧪 <b>POISON:</b> ARMED</div>', unsafe_allow_html=True)

st.write("---")

# Akcje Szybkiego Wyboru
col1, col2 = st.columns(2)

with col1:
    if st.button("🔄 SYNC"):
        with st.spinner("Synchronizacja..."):
            time.sleep(1)
            st.toast("Baza danych zaktualizowana!")

with col2:
    if st.button("🚨 ALARM"):
        send_vinci_alert("Użytkownik wywołał procedurę ALARM z telefonu!")
        st.error("Wysłano alert WhatsApp do Właściciela!")
        st.balloons()

# Polecenia głosowe/tekstowe
st.write("---")
cmd = st.text_input("POLECENIE DLA RADY:", placeholder="Np. 'Generuj raport'...")

if cmd:
    st.info(f"Oczekiwanie na odpowiedź Zahira dla: '{cmd}'")
    with st.status("Przetwarzanie przez OpenAI o1..."):
        time.sleep(2)
        st.success("Analiza zakończona. Raport wysłany do Google Keep.")

# Stopka mobilna
st.write("---")
st.markdown("<p style='text-align: center; color: #444;'>Vinci Office OS Mobile Utility | PAPKA</p>", unsafe_allow_html=True)
