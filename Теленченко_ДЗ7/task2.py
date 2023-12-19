# Создайте декоратор, который в качестве аргумента принимает
# тип данных (str, bool, int, float) и проверяет соответствует ли
# аргумент функции данному типу. Если это не соответствует,
# нужно вывести "Bad type".
# Подсказка: для проверки используйте
# isinstance(object, type_of_object) или type(object).

def type_check(correct_type):
    def inner(func):
        def wrapper(arg):
            if type(arg) == correct_type:
                return func(arg)
            else:
                return 'Bad type'
        return wrapper
    return inner


@type_check(int)
def times2(num):
    return num * 2

@type_check(str)
def first_letter(word):
    return word[0]

print(times2(2))
print(times2(True))

print(first_letter('Hello, World!'))
print(first_letter(1.5))
