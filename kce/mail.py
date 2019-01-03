from smtplib import SMTP
from os import environ

def sendMail(fromaddr, msg):
    server  = SMTP(environ['SMTP'])
    toaddrs = environ['EMAIL']
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
