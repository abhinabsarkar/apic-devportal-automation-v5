import smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Importing configuration parser
import configparser

# Parser to read configuration values
config = configparser.ConfigParser()
config.read("config.ini")

smtp_server = config["Default"]["smtp_server"]
smtp_port = config["Default"]["smtp_port"]
sender_email = config["Default"]["sender_email"]
body = "Attached is the list of Apps that have been subscribed to API"

def send_mail(receiver, filename, subject):
    # Use the id who sends the request
    receiver_email = receiver + "@domain.com"

    # Create a secure SSL context
    # context = ssl.create_default_context()
    context = ssl._create_unverified_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,smtp_port)
        server.starttls(context=context) # Secure the connection

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        # Send email here
        server.sendmail(sender_email, receiver_email, text)
    except Exception as e:
        raise
    finally:
        server.quit()