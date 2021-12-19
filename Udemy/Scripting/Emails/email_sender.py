import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Siam Sarker'
email['to'] = 'msarker192014@bscse.uiu.ac.bd'
email['subject'] = 'What\'s up'

email.set_content('I am learning Python. ')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sarkersiam2@gmail.com', '**********')
    smtp.send_message(email)
    print('All good!')


