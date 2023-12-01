import sys

while True:
    name = input('Добро пожаловать в программу! Как тебя зовут?' + 
                '(для выхода введите "q") ')
    if name.lower() == 'q':
        break

    age = input('Сколько вам лет? (Для выхода введите "q") ')
    if age == 'q':
        break

    answers = [
        'Ошибка, повторите ввод.',
        f'Привет, шкет {name}',
        f'Как жизнь {name}?',
        f'Что желаете {name}?',
        f'{name}, вы лжете - в наше время столько не живут...' 
    ]

    try:
        age = int(age)
    except ValueError:
        sys.exit(answers[0])

    if age <= 0:
        print(answers[0])
    elif age > 0 and age < 10:
        print(answers[1])
    elif age >= 10 and age <= 18:
        print(answers[2])
    elif age > 18 and age < 100:
        print(answers[3])
    else:
        print(answers[4])
