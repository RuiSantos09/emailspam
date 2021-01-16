import smtplib, ssl
import random
from deep_translator import GoogleTranslator
from email.mime.text import MIMEText

password = input("Type your password and press enter: ")
number_of_emails = 100  # Number of emails

while number_of_emails > 0:
    language_list = ['english','german','russian','italian','french','spanish','dutch','czech','hungarian','arabic','afrikaans','hebrew','hindi','japanese','korean','danish','greek','latin','somali','samoan','urdu','zulu','nepali']
    swear_list = ['Porra', 'Foda-se', 'Caralho', 'Cona', 'Colhão', 'Merda', 'Puta', 'Cabrão']

    sender_email = 
    receiver_email = 
    rand_language = random.randint(0,22)
    rand_swear = random.randint(0,7)
    language = language_list[rand_language]
    swear = swear_list[rand_swear]
    message = GoogleTranslator(source="portuguese", target=language).translate(text=swear) + '\n ' + swear + ' ----> ' + language

    text_type = 'plain'
    text = message
    subj = 'o que quiseres como subject' + str(number_of_emails)
    msg = MIMEText(text, text_type, 'utf-8')
    msg['Subject'] = subj
    msg['From'] = sender_email
    msg['To'] = receiver_email

    port = 465  # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg)

    number_of_emails -= 1
