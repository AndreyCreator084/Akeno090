def add_everything_up(a, b):
    try:
        return round(a + b, 3)
    except TypeError:
        return str(a) + str(b)



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

"""
1.Функция принимает два аргумента a и b.
2.Она должна сложить эти два аргумента и вернуть результат.
3.Если оба аргумента являются числами, она округляет результат до трех десятичных знаков.
4.Если хотя бы один из аргументов не является числом, она должна вернуть строку,
которая содержит оба аргумента.
5.В блоке try мы пытаемся выполнить операцию сложения.
6.Если оба аргумента являются числами, операция сложения выполнится успешно.
7.Если хотя бы один из аргументов не является числом,
операция сложения вызовет ошибку TypeError.
8.В блоке except мы обрабатываем эту ошибку и возвращаем строку,
которая содержит оба аргумента.
"""

