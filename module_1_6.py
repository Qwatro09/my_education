my_dict = {'Sasha': 1986, 'Rita': 1995, 'Alex': 2002} # создали словарь
print(f'Dict: {my_dict}') # распечатали словарь
print(f'Existing value: {my_dict.get('Rita')}') # поискали ключ, который есть в словаре и вывели его значение
print(f'Not existing value: {my_dict.get('Masha', 'Такого ключа нет!')}') # поискали ключ, которого нет в словаре
my_dict.update({'Vitia': 2003, 'Sveta': 2010}) # добавили еще два элемента
print(f'Deleted value: {my_dict.pop('Alex')}') # удалили элемент  с ключом 'Alex' и распечатали его значение
print(f'Modified dictionary: {my_dict}') # снова распечатали обновленный словарь

my_set = {5, 6, 7, 'Множество', 45.567, 7, 6, (9, 8, 7)} # создали множество с повторяющимися значаниями
print(f'\nSet: {my_set}') # распечатали множество
my_set.add('Privet') # добавили элемент
my_set.add(83.547) # и еще один
my_set.discard(45.567) # удалили элемент
print(f'Modified set: {my_set}') # распечатали множество

