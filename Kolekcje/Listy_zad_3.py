users_input = input("Podaj listę liczb: ")
users_list = list(users_input.split(" "))
print(users_list)
print(users_list[0])
print(users_list[-1])

if users_list[0] == users_list[-1]:
    print('pierwszy i ostatni element jest taki sam')
else:
    print("pierwszy i ostatni element nie jest taki sam")