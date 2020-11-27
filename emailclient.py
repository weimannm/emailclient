import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Der Code wird größtenteils kopiert von realpython.com
sender_email = "testmaxmustermann870@gmail.com"
receiver_email = "marco.weimann@gmail.com"
password = open("password.txt").read()
file = "blankwall.png" # Verzeichnis wie im Skript

message = MIMEMultipart()
message["Subject"] = "Emailclient-Aufgabe"
message["From"] = sender_email
message["To"] = receiver_email
text = "Halli Hallo!"
html = """\
    <html>
        <head></head>
        <body>
            <p>Hallo, das ist HTML.</p>
        </body>
    </html>
    """

message.attach(MIMEText(text, "plain")) # Textnachricht anfügen
message.attach(MIMEText(html, "html")) # Textnachricht anfügen

attach_file = open(file, "rb") # Datei öffnen
report = MIMEBase("application", "octate-stream")
report.set_payload((attach_file).read())
encoders.encode_base64(report)
report.add_header("Content-Disposition", "attachment", filename = file)
message.attach(report)

# Sichere Verbindung mit Server herstellen und E-Mail senden
session = smtplib.SMTP('smtp.strato.de', 587)
session.starttls() #enable security
session.login(sender_email, password) # Login mit Mail und Passwort
session.sendmail(sender_email, receiver_email, message.as_string())
session.quit()
print("Mail gesendet!")