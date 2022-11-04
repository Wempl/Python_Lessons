from multiprocessing.sharedctypes import Value


country = {'code': 'RU', 'name': 'Russia', 'population': 144}
# country = dict(code='RU', name='RU',)
# print((country['population']))
for key, value in country.items():
    print(key, ' - ', value)