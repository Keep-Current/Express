from smtplib import SMTP
from os import environ

def sendMail(fromaddr, msg):
    try:
        server  = SMTP(environ['SMTP'])
        toaddrs = environ['EMAIL']
        server.login(environ['SMTP_SENDGRID_USER'], environ['SMTP_SENDGRID_PASS'])
        server.sendmail(fromaddr, toaddrs, msg)
    except Exception as e:
        print(e)
    finally:
        server.quit()
