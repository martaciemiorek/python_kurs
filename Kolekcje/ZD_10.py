user_num = int(input("Podaj liczbę: "))

user_list = []
for num in range(1, user_num+1):
    user_list.append(num)
print(user_list)

sqr_list = []
for num in range(1, user_num+1):
    sqr = num * num
    sqr_list.append(sqr)
print(sqr_list)

sqr_dict=dict(zip(user_list,sqr_list))
print(sqr_dict)
