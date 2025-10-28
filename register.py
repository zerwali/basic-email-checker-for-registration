from emailsender import send_email_notification
import random

tryp = 0
attempt = 3

print('-----Register-----')
email = input('email: ')
password = input('password: ')
repassword = input('Re-enter your password: ')

while True:
    if password == repassword:
        break
    else:
        print('the passwords doesnt match')
        password = input('password: ')
        repassword = input('Re-enter your password: ')

subject = 'Verfication Code'
code = random.randint(1111, 9999)
body = f'verfication code: {code}'

send_email_notification(email, subject, body)
print("we've sent u a verfication code in ur email.")
vcode =int(input('entre the code: '))

if code == vcode:
    print('you have been registred succefully')
else:
    while tryp <= 3:
        print('code is incorrect')
        vcode = input('entre the code: ')
        tryp += 1
        print(f'{attempt} attempt left!')
        attempt -= 1

if tryp == 4:
    print('you have to register again.')


