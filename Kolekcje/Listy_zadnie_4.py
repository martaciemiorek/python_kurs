users_input = input("Podaj listę liczb z parzystą liczbą elementów: ")
users_list = list(users_input.split(" "))
print(users_list)
print(len(users_list))

index_1 =int(len(users_list)/2)
print(f"środkowa liczba {index_1}")
index_2 = index_1-1
print(index_2)

print(users_list[index_1])
print(users_list[index_2])

a = int(users_list[index_1])
b = int(users_list[index_2])
print(a)
print(b)
if a == b:
    print("są takie same")
else:
    print("nie są takie same")