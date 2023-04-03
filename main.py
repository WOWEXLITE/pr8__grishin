
from random import choices

symbols = 'ABCDEFGHJKLMNOPQRSUVWXYZ'
symbolslow = 'abcdefghjklmnopqrstuvwxyz'
digits = '0123456789'

chars = ''

pwd_lenght = int(input('Введите длинну пароля: '))
pwd_auto = (input('Сгенерировать пароль автоматически? (y,n): ')=='y')

for text, seq in(
                 ('Включить верхний регистор', symbols ),
                 ('Включить нижний регистор', symbolslow ),
                 ('Включить цифры', digits )
    if pwd_auto or(input(text + '  (y,n): ') == 'y'):
       chars += seq

password = ''.join(choices(chars, k=pwd_lenght))

print ('\n', password '\n', sep='')
