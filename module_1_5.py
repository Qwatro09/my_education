immutable_var = (1, 2, 3, "Symbol", True, [1, 2])
print(f'Immutable tuple: {immutable_var}')
# immutable_var[1] = 21 # попробовали изменить элемент кортежа с индексом 1. Не вышло.
                        # убедились, что кортеж относится к неизменяемому типу данных
immutable_var[5][0] = 21
print(immutable_var[5][0]) # но, если в составе кортежа есть изменяемый тип данных
                           # например, список, его элементы можно менять
print(immutable_var[::2]) # напечатаем каждый второй элемент

mutable_list = [4, 5, 6, "My_list", False, [7, 8, 9]]
print(f'Mutable list: {mutable_list}')

mutable_list[3] = 'They_list'
mutable_list[5][2] = 121
print(f'Mutable list: {mutable_list}')
print(mutable_list[::-2]) # а здесь напечатаем каждый второй элемент с конца

