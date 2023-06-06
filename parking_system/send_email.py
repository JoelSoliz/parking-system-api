import smtplib, ssl
from email.message import EmailMessage
from config import get_settings


setting = get_settings()

context = ssl.create_default_context()

def send(destination, message, asunto):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(setting.email, setting.password)
        for email in destination:
            msg = EmailMessage()
            msg.set_content(message)
            msg['Subject'] = asunto
            msg['From'] = setting.email
            msg['To'] = email
            server.send_message(msg)
