# Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет
# принимать данные числа (т. е. ключи будут типом int), а в качестве
# значений – количество этих чисел в имеющейся последовательности.
# Вывести на экран словарь из 3-х самых часто встречаемых чисел

string = '00000000035999999327835645923052650312302984'
dictionary = { string.count(i) : i for i in string }
dictionary = dict(sorted(dictionary.items())[:-4:-1])
print(dictionary)
for k, v in dictionary.items():
    print(f'{v} встречается {k} раз.')
