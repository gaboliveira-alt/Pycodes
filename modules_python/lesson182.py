import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template

from dotenv import load_dotenv

load_dotenv()

PATH_HTML = Path(__file__).parent / "lesson182.html"

example_sender = os.getenv("FROM_EMAIL", "")
example_recipient = example_sender

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = os.getenv("FROM_EMAIL", "")
smtp_password = os.getenv("EMAIL_PASSWORD", "")

with open(PATH_HTML) as html_file:
    read_text = html_file.read()
    template_text = Template(read_text)
    email_text = template_text.substitute(nome="Gabriel")

mime_multipart = MIMEMultipart()
mime_multipart["from"] = example_sender
mime_multipart["to"] = example_recipient
mime_multipart["subject"] = "Its me Mario"

email_body = MIMEText(email_text, "html", "utf-8")
mime_multipart.attach(email_body)

with smtplib.SMTP(smtp_server, smtp_port) as server_example:
    server_example.ehlo()
    server_example.starttls()
    server_example.login(smtp_username, smtp_password)
    server_example.send_message(mime_multipart)
    print("E-mail enviado com sucesso!")
