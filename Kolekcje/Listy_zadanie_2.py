users_input = input("Podaj 10 liczb: ")
users_list = list(users_input.split(" "))

print(users_list)

for item in users_list:
    if item % 2 == 0:
        print(item)

#for item in users_list