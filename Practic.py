file = open('out.txt', 'w')
file.write(input('Введите логин: ') + ' ' + input('Введите пароль: ')+'\n')
file.close()