my_dict = {'Sasha': 1986, 'Rita': 1995, 'Alex': 2002}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict.get('Rita')}')
print(f'Not existing value: {my_dict.get('Masha', 'Такого ключа нет!')}')
my_dict.update({'Vitia': 2003, 'Sveta': 2010})
print(f'Deleted value: {my_dict.pop('Alex')}')
print(f'Modified dictionary: {my_dict}')

my_set = {5, 6, 7, 'Множество', 45.567, 7, 6, (9, 8, 7)}
print(f'\nSet: {my_set}')
my_set.add('Privet')
my_set.add(83.547)
my_set.discard(45.567)
print(f'Modified set: {my_set}')

