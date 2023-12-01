import random

print('Добро пожаловать в "Угадай число"!')
guesses = 5
current_guess = 1
guess = 0
print(f'Попробуй отгадать число от 1 до 100 за {guesses} попыток!')
num = random.randint(1, 100)
# print(num) # раскомментировать, что бы узнать загаданное число

try:
    while guess != num and current_guess <= guesses:
        guess = int(input(f'Попытка № {current_guess} '))
        if guess > num:
            print('Нужно меньше')
        elif guess < num:
            print('Нужно больше')
        else:
            print('Вы угадали!')
            break
        current_guess += 1
    if current_guess > guesses:
        print('Вы проиграли :(')
        print(f'Загаданное число: {num}')
except ValueError:
    print('Неверный ввод. До свидания :(')
