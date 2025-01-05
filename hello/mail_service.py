import os
from email.message import EmailMessage
import ssl
import smtplib
from web_project.settings import EMAIL_HOST, EMAIL_HOST_PASSWORD
def send_mail(email, text, subject):
    email_receiver = email

    subject = subject

    body = text

    em = EmailMessage()
    em['From'] = EMAIL_HOST
    em['To'] =  email_receiver
    em['Subject'] = subject
    em.set_content(body)

    #add a layer of security
    context = ssl.create_default_context()

    #sending the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: 
        smtp.login(EMAIL_HOST,EMAIL_HOST_PASSWORD)
        smtp.sendmail(EMAIL_HOST,email_receiver, em.as_string())