try:
    n = int(input('Введите целое число: '))
    sum = 0
    # while n > 0:
    #     sum += n ** 3
    #     n -= 1
    for i in range(1, n + 1):
        sum += i ** 3
    print(sum)
except ValueError:
    print('Неверный ввод')
