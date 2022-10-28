n = input("Enter legth:")
i = 0
user_list = []
while i * n:
    string = "Enter element" + str(i + 1) + ": "
    user_list.append(input(string))
    i += 1
print(user_list)
