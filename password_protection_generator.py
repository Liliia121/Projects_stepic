import random
# Генератор безопасных паролей
# Описание проекта: программа генерирует заданное количество паролей и
# включает в себя умную настройку на длину пароля,
# а также на то, какие символы требуется в него включить, а какие исключить.

digits = '0123456789'.strip()
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'.strip()
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.strip()
punctuation = '!#$%&*+-=?@^_'.strip()
chars = ''
kolich = int(input('Введите количество паролей для генерации.\n'))
dlina_odnogo = int(input('Какая длина  необходима для генерации одного пароля?\n'))

add_digits = input('Включать ли цыфры от "0" до "9"  в пароль?\n Да? или Нет?\n')
if add_digits.lower() in ('да', 'д', 'yes', 'y'):
    chars += digits
add_uppercase_letters = input('Включать  ли прописные буквы от "А" до "Я"?\n Да? или Нет?\n')
if add_uppercase_letters.lower() in ('да', 'д', 'yes', 'y'):
    chars += uppercase_letters
add_lowercase_letters = input('включать ли строчные буквы от "а" до "я"?\n Да? или Нет?\n')
if add_lowercase_letters.lower() in ('да', 'д', 'yes', 'y'):
    chars += lowercase_letters
add_punctuation = input('Включить ли пунктуацию "!#$%&*+-=?@^_"?\nДа? или Нет?\n')
if add_punctuation.lower() in ('да', 'д', 'yes', 'y'):
    chars += punctuation
if fig.lower() == ('да', 'д', 'yes', 'y'):
      stroka.replace('i', '')
      stroka.replace('l', '')
      stroka.replace('1', '')
      stroka.replace('L', '')
      stroka.replace('o', '')
      stroka.replace('0', '')
      stroka.replace('O', '')


def generate_password(dlina_odnogo, chars):
    password = ''
    for j in range(dlina_odnogo):
        password += random.choice(chars)
    return password

for _ in range(kolich):
    generate_password(dlina_odnogo, chars)
    print(generate_password(dlina_odnogo, chars))


