import smtplib, ssl
import time
from tqdm import tqdm
from pyfiglet import Figlet
from termcolor import colored
f = Figlet(font = 'slant')
banner=(f.renderText('py-mail'))
print (colored(banner,"blue"))
print (colored('made by Ro706','red'))
print (colored('v.1.0','magenta'))
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = 'rohitmandal21062004@gmail.com'
x = { 'mom': 'monidipa2106@gmail.com','papa':'sudheshmandal18@gmail.com','riya':'lisabake35@gmail.com','me':'rohitmandal99091@gmail.com'}
name = input("name :")
for key, value in x.items():
    if key == name:
        a =value
    else:
        pass
receiver_email = a
password = 'rohitmandal21'
message = input('message: ')
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
for i in tqdm(range(100)):
    time.sleep(0.1)
print ('successfully send mail....')

