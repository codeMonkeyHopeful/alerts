import os, smtplib, ssl
from dotenv import load_dotenv

load_dotenv()


port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = os.getenv("SEND_EMAIL")
sender_pass = os.getenv("SENDER_EMAIL_PASS")
receiver_email = os.getenv("RECEIVER_EMAIL")

message = """
Sending test email from script
"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, sender_pass)
    server.sendmail(sender_email, receiver_email, message)
