from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib

SMTP_SERVER = os.environ.get('SMTP_SERVER')
SMTP_PORT = os.environ.get('SMTP_PORT')
SMTP_USERNAME = os.environ.get('SMTP_USERNAME')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')

DEFAULT_TO_EMAIL = os.environ.get('TO_EMAIL')


def build_message(to_email, subject, body):
    message = MIMEMultipart()
    message['From'] = f'Natan Bot'
    message['To'] = to_email
    message['Subject'] = subject
    mime_text = MIMEText(body, 'plain')
    message.attach(mime_text)

    return message.as_string()


def send_email(subject=None, body=None, to_email=DEFAULT_TO_EMAIL, from_email=SMTP_USERNAME):
    message = build_message(to_email, subject, body)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as session:
        session.starttls()
        session.login(SMTP_USERNAME, SMTP_PASSWORD)
        session.sendmail(from_email, to_email, message)


if __name__ == '__main__':
    send_email(subject='Test', body='Test message')
