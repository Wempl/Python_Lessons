#Мы можем создавать функции для строк!
#Это поможет в распределении команд и нагрузок через листы и списки!

#Практика:
word = 'Footbal, basketball, skate'
#print(word.count('i'))
#print(word.capitalize())
# print(word.find('p'))
hobby = word.split(', ')
for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()
result = ', '.join(hobby)
print(result)
