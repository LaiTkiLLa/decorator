import datetime
import os


def logger(old_function):

    def function(*args, **kwargs):
        start = datetime.datetime.now()
        start = start.strftime('%m/%d/%y %H:%M:%S')
        result = old_function(*args, **kwargs)
        end = datetime.datetime.now()
        end = end.strftime('%m/%d/%y %H:%M:%S')
        if os.name == 'nt':
            desktop_win = os.getenv("USERPROFILE") + '\\Desktop\\logs.txt'
            with open(desktop_win, 'a', encoding='utf-8') as file:
                file.write(f'Функция {old_function} была вызвана {start} с аргументами {args} и {kwargs}'
                           f'\nПолучен результат {result} \nВремя окончания функции {end}\n')
                print(f'Логи сохранены на рабочем столе по пути {desktop_win}')
        elif os.name == 'posix':
            desktop_linux = '/home/' + os.getlogin() + '/Desktop/logs.txt'
            with open(desktop_linux, 'a', encoding='utf-8') as file:
                file.write(f'Функция {old_function} была вызвана {start} с аргументами {args} и {kwargs}'
                           f'\nПолучен результат {result} \nВремя окончания функции {end}\n')
                print(f'Логи сохранены на рабочем столе по пути {desktop_linux}')
            return result
    return function
