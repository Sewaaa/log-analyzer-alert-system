import smtplib
from email.message import EmailMessage
from email.header import Header

def send_email_alert(subject, body, config):
    # Create the email message
    msg = EmailMessage()

    # Set headers
    msg["Subject"] = str(Header(subject, "utf-8"))
    msg["From"]    = config["email"]["from"]
    msg["To"]      = config["email"]["to"]

    # Set plain text body
    msg.set_content(body, subtype="plain", charset="utf-8")

    try:
        # Connect via SSL to the SMTP server (e.g. Gmail: smtp.gmail.com:465)
        with smtplib.SMTP_SSL(config["email"]["smtp_server"], config["email"]["port"]) as smtp:
            smtp.login(config["email"]["username"], config["email"]["password"])
            smtp.send_message(msg)
        return True  # Success
    except Exception as e:
        print(f"Email sending error: {e}")
        return False  # Failure
