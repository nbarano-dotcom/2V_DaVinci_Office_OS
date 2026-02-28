"""Wysyłanie alertów Rady Agentów na WhatsApp (Twilio)."""
import os
from twilio.rest import Client


def send_vinci_alert(message: str) -> None:
    """Wysyła powiadomienie z Rady Agentów na WhatsApp."""
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID", "TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN", "TWILIO_AUTH_TOKEN")
    to_number = os.environ.get("VINCI_WHATSAPP_TO", "whatsapp:+48XXXXXXXXX")

    if account_sid == "TWILIO_ACCOUNT_SID" or auth_token == "TWILIO_AUTH_TOKEN":
        print("⚠️ Ustaw TWILIO_ACCOUNT_SID i TWILIO_AUTH_TOKEN (env).")
        return

    client = Client(account_sid, auth_token)
    try:
        msg = client.messages.create(
            from_="whatsapp:+14155238886",
            body=f"💎 daVVinci ALERT: {message}",
            to=to_number,
        )
        print(f"✅ WhatsApp wysłany: {msg.sid}")
    except Exception as e:
        print(f"❌ Błąd WhatsApp: {e}")
