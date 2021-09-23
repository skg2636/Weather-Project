import math, random
def generateOTP(n):
    digits = "0123456789"
    OTP = ""
    for i in range(n):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendOTP(to_email,otp):
    msg = MIMEMultipart()
    msg['To'] = to_email;
    msg['From'] = 'sender_email'
    msg['Subject'] = 'OTP Verification'

    plain = f"Dear {to_email} your One Time Password is {otp} and is valid for 3 minutes. Please don't share this OTP with anyone\n\nThankyou"

    p = MIMEText(plain,'plain')
    msg.attach(p)
    host = 'smtp.gmail.com'
    port = 465

    password = "password"
    try:
        with smtplib.SMTP_SSL(host,port,context=ssl.create_default_context()) as server:
            server.login(msg['From'],password)
            server.sendmail(msg['From'],msg['To'],msg.as_string())
            return True, "OTP Sent Successfully"
    except Exception as err:
        return False, err




