# Магический шар 8
# Описание проекта: магический шар 8 (шар судьбы) — шуточный способ предсказывать будущее.
# Программа должна просить пользователя задать некий вопрос, чтобы случайным образом на него ответить.

import random, time
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет, Мир! Я магический шар, который знает ответ на любой твой вопрос.')
name = input('Как тебя зовут, мой дорогой друг?\n')
print(f'Здравствуй, {name.capitalize()}!')

while True:
    ask = input('Задайте свой вопрос!\n')
    print(f'Ответ на вопрос: "{random.choice(answers)}"')
    ask_again = input(f'Хотите спросить снова? Да/Нет\n').lower()

    if ask_again == 'нет' or ask_again == 'ytn':
        print('Возвращайся если возникнут вопросы!')
        break

    elif ask_again == 'lf' or ask_again == 'да':
        continue

    else:
        print('Вы ввели некорректный ответ на вопрос!\nИгра окончена!!!\nВопросник перезапустится через 5 секунд\nУдачи!!!\n')
        time.sleep(5)

