from re import sub
import smtplib


mailFrom = 'python'
mailTo = 'kryki9669@gmail.com'

subject = 'Email wyslany z pythona'
body = '''
Hello
python is able to send emails automaticlly!!!
Best regards 
Krzysztof Ragan'''

message = '''From: {}
Subject: {}

{}
'''.format(mailFrom , subject , body)

user = 'kryki9669@gmail.com'
password = 'piotrekjestjebanymfrajerem'


try:
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.ehlo()
  server.login(user , password)
  server.sendmail(user, mailTo, message)
  server.close()
  print('mail sent')

except:
  print('error ocured')
