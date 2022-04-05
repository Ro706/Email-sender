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
sender_email = input('sender mail id:')
receiver_email = input('receiver mail id:')
password = input('password:')
message = input('message: ')
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
for i in tqdm(range(100)):
    time.sleep(0.1)
print ('successfully send mail....')

