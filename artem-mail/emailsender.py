#!/usr/bin/python
import smtplib

# special smtp server addresses
email_dictionary = {"yahoo": "smtp.mail.yahoo.com", "outlook": "smtp.live.com", "icloud": "smtp.mail.me.com"}
services = list(email_dictionary.keys())
# smtp Servers that work with algorithm : gmail,zoho,yandex,aol

# place holders
domain = "smtp.gmail.com"
server = smtplib.SMTP(domain, 587)
user = ""
passw = ""


def login_to_email(username, password):
    global server, user, passw, domain
    match = False
    user = username
    passw = password

    domain = "smtp." + username.split("@")[1]
    # if domain is in list of special smtp servers
    if domain.split(".")[1] in services:
        server = smtplib.SMTP(email_dictionary[domain.split(".")[1]], 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        print("Special smtp server address found")
    else:
        server = smtplib.SMTP(domain, 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        print("Normal smtp server")

    login_success = authenticate()
    if login_success:
        print("Yay you are logged in")
        return True
    print("NUUUUUUUUUUUUUUUUUU")
    return False


def sendEmail(sendto, subject, text, attachments=[]):
    FROM = user
    TO = sendto
    SUBJECT = subject

    TEXT = text

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % FROM,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])
    try:
        server.sendmail(user, [TO], BODY)
        server.quit()
        print('Your email was sent!')
    except:
        print("Error sending mail! Does the recipient's email exist?")
        raise


# LOGGING INTO THE ACCOUNT
def authenticate():
    try:
        server.login(user, passw)
        return True
    except smtplib.SMTPAuthenticationError:
        return False


