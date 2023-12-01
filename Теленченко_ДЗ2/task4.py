# Задание 4

user_input = input('Введите строку: ')

even = user_input[0::2]
odd = user_input[1::2]

# print(user_input.strip())
print(f'Введена строка: {user_input}\n\n')
print(even, odd, sep='     ', end='\n!!!')
