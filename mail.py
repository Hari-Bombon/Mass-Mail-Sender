import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import time
import re
import os


sender_email = "haripriyamax1427@gmail.com"
password = "tlsleabaxjjryjjw"
message = MIMEMultipart("alternative")
message["Subject"] = "Testing App"
message["From"] = sender_email
context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
server.ehlo()
server.login(sender_email, password)
with open('mail.html', 'r', encoding="utf8") as file:
    data = file.read().replace('\n', '')
count = 0
with open("BULKEMAIL.csv") as file:
    reader = csv.reader(file)
    next(reader)    
    for  email in reader:
        for check in email:
            pat = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
            obj = re.match(pat, check)
            if obj:
                print("Valid Email")
            else:
                print("Invalid")
        
        html = "This is msg from Max"
        message.attach(MIMEText(html, "html"))
        server.sendmail(
            sender_email, email, message.as_string()
        )
        count += 1
        print(str(count)," Sent to ",email)
        if(count%80 == 0):
            server.quit()
            print("Server cooldown for 100 seconds")
            time.sleep(2000)
            server.ehlo()
            server.login(sender_email, password)
server.quit()