import smtplib, ssl
from config import get_settings


setting = get_settings()

context = ssl.create_default_context()

def send(destination, message):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(setting.email, setting.password)
        for i in destination:
            server.sendmail(setting.email, i, message)

send(['riveramauro278@gmail.com'], 'hola')