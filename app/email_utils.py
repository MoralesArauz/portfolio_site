import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()


def send_contact_email(name, email, subject, message_body):
    sender_email = os.getenv("EMAIL_USER")
    receiver_email = "morales.arauz@gmail.com"  # You can send to yourself
    password = os.getenv("EMAIL_PASS")  # Use an app password if using Gmail

    # Compose message
    subject_line = f"Portfolio Contact: {subject}"
    body = f"From: {name} <{email}>\n\n{message_body}"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject_line
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Contact email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")