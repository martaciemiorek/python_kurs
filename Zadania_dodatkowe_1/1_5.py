user_nbr = int(input("podaj liczbę rzędów gwiazdek: "))



if user_nbr >= 4 and user_nbr <= 10:
    for n in range(1, user_nbr+1):
        print("*" * n)
else:
    print("podaj liczbę większą niż 4 i mniejsza niz 10")


