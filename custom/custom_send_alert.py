import os, smtplib


def send_custom_alert(email_from, app_pass, email_to,  sms_message):
    sender_email = email_from
    sender_pass = app_pass
    receiver_email = email_to



    message = sms_message

    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        server_ssl.login(sender_email, sender_pass)  

        server_ssl.sendmail(sender_email, receiver_email, message)

        server_ssl.close()

        return {
            "status": "success",
            "sender": sender_email,
            "receiver": receiver_email, 
            "message": message
        }
    except Exception as e:
        print(e)
        return {
            "status": "fail",
            "error": e
        }

