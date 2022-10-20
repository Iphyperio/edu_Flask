'''

#функция "обёртка" внутри функции
def coffee():
    print('Кофе')
def command(func):
    def wrap():
        print('Сейчас готовится')
        func()
    return wrap


makeCoffee=command(coffee)
makeCoffee()


def decorator(func):
    def wrap():
        print('Обертка перед функцией')
        func()
        print('Обертка после функции')
    return wrap

@decorator
def hello():
    print('hello')
hello()


#ПРИМЕР ДЕКОРАТОРА
import datetime
def candy_wrapper(func):
    def wrap():
        print('-------------------')
        func()
        print('-------------------')
    return(wrap)
#candy_wrapper(datetime.datetime.now)


@candy_wrapper
'''
'''
#Время выполнения функции
def stopwatch(func):
    import time
    def wrap():
        t=time.time()        
        func()
        print('Время выполнения функции: ', '%.2f' % (time.time()-t),'секунд')
    return(wrap)
@stopwatch
def ask():
    return input('Введите текст: ')

ask()
'''
'''
#инспектор
def inspector(func):
    s=set()
    def wrap(name):
        if name in s:
            print('Такое имя уже было')
        else:
            s.add(name)
            func(name)
    return wrap


@inspector
def hello(name):
    print(f"Привет, {name}")

hello('Вася')
hello('Петя')
hello('Вася')

hello('Вася')
hello('Коля')
'''