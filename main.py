import os, smtplib
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("SEND_EMAIL")
sender_pass = os.getenv("APP_PW")
receiver_email = os.getenv("RECEIVER_EMAIL")



message = """
Put your test message here.
"""

try:
    server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    server_ssl.login(sender_email, sender_pass)  

    server_ssl.sendmail(sender_email, receiver_email, message)

    server_ssl.close()
except Exception as e:
    print(e)