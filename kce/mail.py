from smtplib import SMTP
from os import environ

from email import encoders
from email.mime.text import MIMEText
from email.mime.message import MIMEMessage


def sendMail(fromaddr, content):
    server  = SMTP(environ['SMTP'])
    
    try:
        server.login(environ['SMTP_SENDGRID_USER'], environ['SMTP_SENDGRID_PASS'])

        toaddrs = environ['EMAIL']
        msg = MIMEMessage()
        msg.attach(MIMEText(content, 'plain'))
        msg.add_header('From', fromaddr)
        msg.add_header('To', toaddrs)
        msg.add_header('Subject', 'a message from Keep-Current site')

        server.sendmail(fromaddr, toaddrs, msg.as_string())
    except Exception as e:
        print(e)
    finally:
        server.quit()
