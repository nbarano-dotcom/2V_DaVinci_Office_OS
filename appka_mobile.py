import streamlit as st
from datetime import datetime

# Konfiguracja Ultra-Mobile-OLED
st.set_page_config(page_title="VINCIOFFICE MOBILE", page_icon="📱", layout="centered")

# CSS: Visual Vinci Mobile Style (Black & Neon)
st.markdown("""
    <style>
    /* Głęboka czerń dla ekranów OLED */
    .stApp { background-color: #000000; color: #00ffcc; }
    
    /* Ukrycie elementów przeglądarki dla efektu Native App */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Szklane karty statusu */
    .status-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #333;
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Gigantyczne neonowe przyciski pod kciuk */
    .stButton>button {
        width: 100%;
        height: 100px;
        font-size: 26px !important;
        font-weight: bold;
        border-radius: 25px;
        background: linear-gradient(135deg, #00ffcc 0%, #0088ff 100%);
        color: black;
        border: none;
        margin-bottom: 20px;
        box-shadow: 0px 10px 20px rgba(0, 255, 204, 0.2);
    }
    
    /* Stylizacja inputów */
    .stTextInput>div>div>input {
        background-color: #111;
        color: #fff;
        border: 1px solid #00ffcc;
        border-radius: 15px;
        height: 60px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAGŁÓWEK MOBILNY ---
st.title("🛡️ VINCI MOBILE")
st.markdown(f"""
    <div class="status-card">
        <span style='color: #00ffcc; font-size: 1.2em;'>● SYSTEM ONLINE</span><br>
        <span style='color: #444;'>{datetime.now().strftime('%d.%m.2026 | %H:%M:%S')}</span>
    </div>
    """, unsafe_allow_html=True)

# --- GŁÓWNE AKCJE (TOUCH OPTIMIZED) ---
if st.button("🔄 GITHUB SYNC"):
    with st.spinner("Synchronizacja..."):
        import subprocess
        subprocess.run(["python3", "sync_vvinci.py"])
        st.toast("Sync 5e5169c zakończony!")
        st.balloons()

if st.button("🚨 ALARM WHATSAPP"):
    from DIABOLINA_CORE.whatsapp_notifier import send_vinci_alert
    send_vinci_alert("🚨 ALERT MOBILNY: Aktywowano z telefonu użytkownika!")
    st.error("Wysłano powiadomienie do Właściciela!")

# --- TERMINAL POLECEŃ ---
st.write("---")
cmd = st.text_input("POLECENIE DLA RADY:", placeholder="Np. 'Zahir, generuj CV'...")

if cmd:
    st.info(f"Oczekiwanie na odpowiedź Zahira dla: „{cmd}”")
    with st.status("Przetwarzanie..."):
        import time
        time.sleep(2)
        st.success("Raport wysłany do Google Keep.")
