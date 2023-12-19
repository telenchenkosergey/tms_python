# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итоговом файле должны быть 4 строки, каждая из которых должна начинаться с 
# новой строки.

str_1 = input('Enter first string: ')
str_2 = input('Enter second string: ')
str_3 = input('Enter third string: ')
str_4 = input('Enter fourth string: ')

f = open('task.txt', 'w')
f.write(str_1 + '\n')
f.write(str_2 + '\n')
f.close()

f = open('task.txt', 'a')
f.write(str_3 + '\n')
f.write(str_4 + '\n')
f.close()
