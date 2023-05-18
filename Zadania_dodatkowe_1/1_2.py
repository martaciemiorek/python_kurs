user_num = int(input("Podaj liczbę: "))

for i in range(1, 11):
    result = i * user_num
    print(f'{user_num} * {i} = {result}')