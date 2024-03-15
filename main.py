# imports
import os, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# send email function
def send_email(sender, password, recipients=[], subject, message, file_paths=[]):

    # ensure that recipients and file_paths are list types
    if type(recipients) != type([]): recipients = [recipients]
    if type(file_paths) != type([]): file_paths = [file_paths]

    # create email_msg object
    email_msg = MIMEMultipart()
    email_msg['From'] = sender
    email_msg['To'] = ','.join(recipients)
    email_msg['Subject'] = subject
    email_msg.attach(MIMEText(message, "plain"))

    # attach encoded files from paths to email_msg
    for file_path in file_paths:
        file = MIMEBase('application', 'octet-stream')
        with open(file_path, 'rb') as attachment:
            file.set_payload(attachment.read())
        encoders.encode_base64(file)
        filename = os.path.basename(file_path)
        file.add_header('Content-Disposition', f'attachment; filename= {filename}')
        email_msg.attach(file)

    # login to server and send email_msg over smtp
    smtp_port = 465
    server = smtplib.SMTP_SSL('smtp.gmail.com', smtp_port)
    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, recipients, email_msg.as_string())
    server.close()

# example variables
my_email = 'your.email@gmail.com'
my_password = 'aaaa aaaa aaaa aaaa' # must be obtained as an app password from your email account after 2-factor authentication is enabled
recipients = ['person.1.example@gmail.com', 'person.2.example@gmail.com', 'person.3.example@gmail.com']
subject = 'Email subject line'
message = 'Hello, this is a test email sent with python!'
file_paths = ['path/to/file_1.ext', 'path/to/file_2.ext', 'path/to/file_3.ext']

# example function call
send_email(my_email, my_password, recipients, subject, message, file_paths)
