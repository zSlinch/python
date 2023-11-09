import os
import smtplib
from email.message import EmailMessage
from segredos import senha

#configurar email e senha

EMAIL_ADRESS = 'seu email'
EMAIL_PASSWORD = senha

#criar email 

msg = EmailMessage()
msg['Subjects'] = 'assunto'
msg['From'] = 'eseu email'
msg['To'] = 'email que vai receber '
msg.set_content('tema sobre o qual quer falar')

#enviar um email

with smtplib.SMTP_SSl('smtp.gmail.com' , 465) as smtp:
    smtp.login(EMAIL_ADRESS , EMAIL_PASSWORD)
    smtp.send_message(msg)