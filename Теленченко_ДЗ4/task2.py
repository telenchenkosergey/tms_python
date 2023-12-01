# Дан словарь, поменять местами ключ и значение. Если значения
# повторяются, ключи объединить в список

dictionary = {
    'London' : 'England',
    'Rome' : 'Italy',
    'Berlin' : 'Germany',
    'Manchester' : 'England',
    'Milan' : 'Italy',
    'Madrid' : 'Spain'
}

modified_dictionary = {}

for k, v in dictionary.items():
    if v not in modified_dictionary:
        modified_dictionary[v] = k
    else:
        tmp = []
        tmp.append(modified_dictionary[v])
        tmp.append(k)
        modified_dictionary[v] = tmp

for k, v in modified_dictionary.items():
    print(k, v)
