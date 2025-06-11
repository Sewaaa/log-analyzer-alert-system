# Script to test the correct sending of emails

import yaml
from utils.alert import send_email_alert

# Load configuration
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Test message
subject = "🔔 Test Email from Log Analyzer"
body = """
This is a test for sending alerts via email.
If you are reading this message, the SMTP system is working correctly! ✅

Please do not reply to this message.
"""

# Send the email
success = send_email_alert(subject, body.strip(), config)

if success:
    print("Email sent successfully!")
else:
    print("Error while sending the email.")
