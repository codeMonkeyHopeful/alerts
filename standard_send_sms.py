import os, smtplib
from dotenv import load_dotenv

load_dotenv()


def send_alert(sms_message):
    sender_email = os.getenv("SEND_EMAIL")
    sender_pass = os.getenv("APP_PW")
    receiver_email = os.getenv("RECEIVER_EMAIL")



    message = sms_message

    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        server_ssl.login(sender_email, sender_pass)  

        test = server_ssl.sendmail(sender_email, receiver_email, message)

        server_ssl.close()

        return {
            "code": 1,
            "status": "success",
            "sender": sender_email,
            "receiver": receiver_email, 
            "message": message
        }
    except Exception as e:
        print(e)
        return {
            "code": 0,
            "status": "fail",
            "error": e
        }
