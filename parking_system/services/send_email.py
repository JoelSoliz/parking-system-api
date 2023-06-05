# import smtplib, ssl


# EMAIL = "sjmmsoft@gmail.com"
# PASSWORD = "kmeczftpdrzoshmx"

# context = ssl.create_default_context()

# def send(destination, message):
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#         server.login(EMAIL, PASSWORD)
#         for i in destination:
#             server.sendmail(EMAIL, i, message)

# send([""], "hola")
