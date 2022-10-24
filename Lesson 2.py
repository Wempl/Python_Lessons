# coding 'utf-8'
#Float
Digit = 4.5

#Int
Number = 4

#String
Lesson = "Hello"

#Bool
Jou = True

# Неправильно
# print(Digit + Number)
# Нельзя! Нельзя соединять переменные разных типов!
# Но, есть варианты обойти:
Number2 = 4.5       #Float
Number3 = "Привет"  #String
print(Number2, Number3)
#Проверьте!


#Практика:
num1 = int(input("Введите первое число -"))
num2 = int(input("Введите второе число -"))
print("Resultat:", num1 + num2)
print("Resultat:", num1 - num2)
print("Resultat:", num1 / num2)
print("Resultat:", num1 * num2)
print("Resultat:", num1 ** num2)
print("Resultat:", num1 // num2)