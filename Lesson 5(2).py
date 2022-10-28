numbers = [5, 2, 7]

#Неправильно создавать элементы!
#numbers[3] = 100

numbers.append(100)
numbers.insert(1, True)
b = [5 ,6 , 7, 8]
numbers.extend(b)
numbers.sort()
numbers.pop(-2)
numbers.remove(7)
#numbers.clear()
print(len(numbers))