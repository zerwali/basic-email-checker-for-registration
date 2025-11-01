import time
import random
from emailsender import send_email_notification

tryp = 0
attempt = 3

print('-----Register-----')
name = input('entre ur name: ')
while True:
    email = input('email: ')
    if '@gmail.com' in email:
        break
    else:
        print('not appropriate format (@gmail.com)')

password = input('password: ')
while True:
    if len(password) < 8:
        print('password lenght not enough')
        password = input('Re-enter your password: ')
    else:
        repassword = input('confirm your password: ')
        if password == repassword:
            break
        else:
            print('the passwords doesnt match')
            password = input('Re-enter your password: ')

subject = 'Verfication Code'
code = random.randint(1111, 9999)
body = f'verfication code: {code}'

send_email_notification(email, subject, body)
print("we've sent u a verfication code in ur email.")
vcode =int(input('entre the code: '))

while tryp < 3:
    if code == vcode:
        file =  open('login.txt', 'a')
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        file.write(f'[{timestamp}] {name} = {email}:{password}')
        file.close()
        print('you have been registred succefully')
        break
    else:
        print('code is incorrect')
        print(f'{attempt} attempt left!')
        vcode = int(input('Re-entre the code: '))
        tryp += 1
        attempt -= 1

if tryp == 3:
    print('0 attempt left!')
    print('you have to register again.')


