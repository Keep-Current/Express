from smtplib import SMTP
from os import environ

from email.mime.text import MIMEText


def sendMail(fromaddr, content):
    server  = SMTP(environ['SMTP'])
    
    try:
        server.login(environ['SMTP_SENDGRID_USER'], environ['SMTP_SENDGRID_PASS'])

        toaddrs = environ['EMAIL']

        msg = MIMEText(content)
        msg['From'] = fromaddr
        msg['To'] = toaddrs
        msg['Subject'] = 'a message from Keep-Current site'

        server.send_message(msg)
    except Exception as e:
        print(e)
    finally:
        server.quit()
