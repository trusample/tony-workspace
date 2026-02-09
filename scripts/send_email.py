#!/usr/bin/env python3
"""
Simple email sender using SMTP
Usage: python3 send_email.py <to> <subject> <body_file>
"""

import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Config (Google Workspace / Gmail SMTP)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.environ.get("EMAIL_USER", "MHERNANDEZ@CELLABIOS.COM")
SENDER_PASSWORD = os.environ.get("EMAIL_PASS", "")
SENDER_NAME = os.environ.get("EMAIL_NAME", "Tony Montana")

def send_email(to_email: str, subject: str, body: str, html: bool = False):
    msg = MIMEMultipart("alternative")
    msg["From"] = f"{SENDER_NAME} <{SENDER_EMAIL}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    
    if html:
        msg.attach(MIMEText(body, "html"))
    else:
        msg.attach(MIMEText(body, "plain"))
    
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
    
    print(f"✅ Email sent to {to_email}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 send_email.py <to> <subject> <body_file>")
        sys.exit(1)
    
    to = sys.argv[1]
    subject = sys.argv[2]
    body_file = sys.argv[3]
    
    with open(body_file, "r") as f:
        body = f.read()
    
    send_email(to, subject, body)
