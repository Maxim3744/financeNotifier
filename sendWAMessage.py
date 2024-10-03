from twilio.rest import Client
import os


def send_whatsapp_message(message_body):
    # Twilio Account SID und Auth Token
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    # Nachricht senden
    client.messages.create(
        from_='whatsapp:+14155238886',  # Twilio WhatsApp-Sandbox-Nummer
        body=message_body,
        to='whatsapp:+4915770319514'  # target number
    )
