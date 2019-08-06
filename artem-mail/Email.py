#!/usr/bin/python

# smtplib module send mail
# server.login(gmail_sender, gmail_passwd)
# server.sendmail(gmail_sender, [TO], BODY)

import sys
import smtplib
import os
import imaplib

# defines the server for gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
# mail = imaplib.IMAP4_SSL('imap.gmail.com')  # port 993
server.ehlo()
server.starttls()
server.ehlo()

# defines everything for the webpage
url = "https://mail.google.com/mail/u/0/#inbox"


def inbox(username, password):
    FROM = username
    TO = "123rex100@gmail.com"
    SUBJECT = "Test subject"

    TEXT = "Testing message"

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % FROM,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])
    try:
        server.sendmail(username, [TO], BODY)
        print('Your email was sent!')
    except:
        print("Error sending mail! Does the recipient's email exist?")


# LOGIN INTO GMAIL
def sendMail():
    gmail_sender = "ericnguyencode@gmail.com"
    gmail_passwd = "schoolsucks"
    try:
        authenticate(gmail_sender, gmail_passwd)
        inbox(gmail_sender,gmail_passwd)
    except:
        raise


# LOGGING INTO THE ACCOUNT
def authenticate(username, password):
    try:
        server.login(username, password)

    except smtplib.SMTPAuthenticationError:

        print("\nUTHENTICATION ERORR!:\n")
        print("Cannot sign in. Are you sure this account exists?:")
        print(
            "\nRight now, the reason you may not log-into your gmail account (if your cresidentials are right) is because google sees this form of authentication as 'less secure'.\n")
        print("How to fix this issue:")
        print("""
1. Login to your Gmail Account
2. Open the link:""")
        print("https://www.google.com/settings/security/lesssecureapps")
        print("3. Allow less secure app access to your gmail account.\n")
        print("I allowed unsecure apps. Why is it still not working?:")
        print("""\nSo now it appears you typed in your
cresidentials correctly and allowed unsecure apps, but it still doesnt work. 

This is because google doesn't know if the location of the device accessing your gmail (in this case, the tool itself), is by you.\n""")
        print("How to fix this issue as well:")
        print("\n1. Allow the location of the device by openining the link:")
        print("https://www.google.com/settings/security/lesssecureapps")
        print(
            "2. If this link does not work, perform it manually from your Gmail account (it should send you a notification that an unknown device tried accessing your account. Allow this device.)")
        print("""3. Try to wait at least 1 minute for this to process.
It make take an hour for the change to kick-in, 
so sit back, relax, and grab a coffee.""")
        print(
            "\n(I personally found that this works best on chrome after signing into my gmail and then clicking on the link.)\n")
        input("Please press {ENTER} to continue... ")


sendMail()
