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
        print("Trying to login")

    except smtplib.SMTPAuthenticationError:
        print("Cannont sign in")
        return False
        #         print("\nAUTHENTICATION ERROR!:\n")
        #         print("Cannot sign in. Are you sure this account exists?:")
        #         print(
        #             "\nRight now, the reason you may not log-into your gmail account (if your credentials are right) is because google sees this form of authentication as 'less secure'.\n")
        #         print("How to fix this issue:")
        #         print("""
        # 1. Login to your Gmail Account
        # 2. Open the link:""")
        #         print("https://www.google.com/settings/security/lesssecureapps")
        #         print("3. Allow less secure app access to your gmail account.\n")
        #         print("I allowed unsecured apps. Why is it still not working?:")
        #         print("""\nSo now it appears you typed in your
        # credentials correctly and allowed unsecured apps, but it still doesnt work.
        #
        # This is because google doesn't know if the location of the device accessing your gmail (in this case, the tool itself), is by you.\n""")
        #         print("How to fix this issue as well:")
        #         print("\n1. Allow the location of the device by opening the link:")
        #         print("https://www.google.com/settings/security/lesssecureapps")
        #         print(
        #             "2. If this link does not work, perform it manually from your Gmail account (it should send you a notification that an unknown device tried accessing your account. Allow this device.)")
        #         print("""3. Try to wait at least 1 minute for this to process.
        # It make take an hour for the change to kick-in,
        # so sit back, relax, and grab a coffee.""")
        #         print(
        #             "\n(I personally found that this works best on chrome after signing into my gmail and then clicking on the link.)\n")
        #         input("Please press {ENTER} to continue... ")
    finally:
        return True
