import smtplib, ssl
from email.message import EmailMessage
from config import get_settings


setting = get_settings()

context = ssl.create_default_context()

def send(destination, message, asunto):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(setting.email, setting.password)
        url = setting.webapp_url
        for email in destination:
            msg = EmailMessage()

            html_message = """
            <html>
              <head>
                <style>
                  .container {{
                    background-color: white;
                    padding: 5px;
                    width: 50%;
                    margin: 0 auto;
                    border: 1px solid blue
                  }}

                  h1 {{
                    color: blue;
                    font-size: 20px;
                    text-align: center;
                  }}

                  .message {{
                    color: black;
                    font-size: 15px;
                    text-align: left;
                  }}

                  .url{{
                    text-align: center;
                  }}

                  .mensaje{{
                    width: 85%;
                    margin: 0 auto;
                  }}
                </style>
              </head>
              <body>
                <div class="container">
                  <h1>Parking Spot</h1>
                  <div class="mensaje">
                    <p class="message">{}</p>
                  </div>
                  <div class="url">
                    <a calss="url" href="{}">Parkin Spot</a>
                  </div>
                   
                </div>
                
              </body>
            </html>
            """.format(message, url)

            msg.set_content(html_message, subtype= "html")
            msg['Subject'] = asunto
            msg['From'] = setting.email
            msg['To'] = email
            server.send_message(msg)
