# Написать декоратор к 2м любым функциям который бы считал и выводил время их выполнения.
import time

def counter(function):
    def wrapper(n):
        t1 = time.time()
        function(n)
        t2 = time.time() - t1
        print(f'{function.__name__} took {t2} sec.')
    return wrapper

@counter
def count_to(n):
    for i in range(n):
        print(i)

@counter
def say_hello(name):
    print(f'Hello, {name}!')

count_to(1_000_000)
say_hello('Sergey')
