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
mail = imaplib.IMAP4_SSL('imap.gmail.com')  # port 993
server.ehlo()
server.starttls()
server.ehlo()

# defines everything for the webpage
url = "https://mail.google.com/mail/u/0/#inbox"


def quit():
    sys.quit()


def inbox(username, password):
    try:
        while True:
            answer = input(core.red + "G" + core.white + "mail" + core.yellow + " > " + core.r + "")
            answer = answer.split(" ")
            if answer[0] == "help":
                print("\n-----------\n")
                print(core.ul + "The Help/Command Menu" + core.r)
                print("\nhelp - Opens this help menu")
                print("send <spoofemail@fakewebsite.com> <sendingto@gmail.com> - Send an email with your gmail account")
                print("exit - Go back to the homepage")
                print("\n-----------\n")
            elif answer[0] == "send":
                try:
                    FROM = answer[1]
                    TO = answer[2]
                    SUBJECT = input("\nSubject: ")

                    TEXT = ""

                    BODY = '\r\n'.join(['To: %s' % TO,
                                        'From: %s' % FROM,
                                        'Subject: %s' % SUBJECT,
                                        '', TEXT])
                    try:
                        server.sendmail(username, [TO], BODY)
                        print('Your email was sent!')
                    except:
                        print("Error sending mail! Does the recipient's email exist?")
                except:
                    print("\nError: Could not send email! Your command was incorrectly set.\n")
            else:
                print("\nCommand '" + str(answer) + "' was not found. Please type 'help' for help.\n")
    except KeyboardInterrupt:
        main.startup()
    except:
        print("\nError: Can't find input.\n")


# LOGGING INTO THE ACCOUNT
def authenticate(username, password):
    try:
        server.login(username, password)
        mail.login(username, password)
        inbox(username, password)
    except smtplib.SMTPAuthenticationError:
        print("Login error")
