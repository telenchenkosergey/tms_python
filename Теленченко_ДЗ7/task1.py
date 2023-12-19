# Написать декоратор, который будет запускать функцию только
# в рабочие часы (с 9 до 18)
from datetime import datetime

def working_hours_only(func):
    def wrapper():
        hour = datetime.now().hour
        if 9 <= hour < 18:
            func()
        else:
            print('Работать нельзя!')
    return wrapper

@working_hours_only
def work():
    print('Работаем')


work()
