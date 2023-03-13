#функция посимвольного превращения строки в число с помощью функции ord
def str_int(line):
    st = 0
    for el in line:
        st += ord(el)
    return st

#функция хэширования, которая создает словарь ключ: индекс
def hash_multi(m, keys, A):
    h = {}
    for el in keys:
        if el.isdigit():
            k = int(el)
        else:
            k = str_int(el)
        index = int(m * ((k * A) % 1))
        h[el] = index
    return h

def test():
    print('Введите длину хэш-таблицы:')
    m = int(input())
    print('Через пробел введите ключи:')
    keys = input().split()
    A = (5 ** 0.5 - 1) / 2

    print('Значения хэш-функции для введенных ключей:')
    h = hash_multi(m, keys, A)
    for el in h:
        print(f'h({el}) =', h[el])

test()
