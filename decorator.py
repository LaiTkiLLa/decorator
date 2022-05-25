import datetime


def parametrized_decor(parameter):

    def logger(old_function):

        def function(*args, **kwargs):
            start = datetime.datetime.now()
            start = start.strftime('%m/%d/%y %H:%M:%S')
            result = old_function(*args, **kwargs)
            end = datetime.datetime.now()
            end = end.strftime('%m/%d/%y %H:%M:%S')
            with open(parameter, 'a', encoding='utf-8') as file:
                file.write(f'Функция {old_function} была вызвана {start} с аргументами {args} и {kwargs}'
                            f'\nПолучен результат {result} \nВремя окончания функции {end}\n')
                print(f'Логи сохранены на по пути {parameter}')

            return result
        return function
    return logger





