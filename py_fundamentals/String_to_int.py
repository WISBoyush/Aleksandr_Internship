# Напишите функцию, которая будет преобразовывать строку в число аналогично функции int только без ее использования.
# Функция должна иметь набор проверок и поднимать исключения если переданные данные не являются валидными.


def string_to_int(string):
    if not string.startswith('-') and not string.isdigit():
        raise ValueError(
            f'Вами введено не число \n\n'
            f'Ошибка в ({string})'
        )
    elif string.startswith('-') and not string[1:].isdigit():
        raise ValueError(
            f'Вами введено не число \n\n'
            f'Ошибка в ({string})'
        )
    else:
        positive = False if string.startswith('-') else True
        string = string[1:] if not positive else string
        number = 0

        for i in string:
            number *= 10
            number += (ord(i) - 48)
        return number if positive else number * -1


try:
    print(string_to_int('1340324'))

    print(string_to_int('-123'))

    print(string_to_int('0asd123'))

except ValueError as e:
    print(f'__!!! WARNING !!!__\n{e}')
