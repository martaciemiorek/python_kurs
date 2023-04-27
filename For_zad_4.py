input = int(input("Podaj liczbę : "))

if input >8:
    print("Podaj liczbę pomiędzy 1 a 8:")
else:
    print(input, "! = ")

    silnia = 1

    for num in range(2, silnia+1):
        silnia = silnia * num
        print(silnia)




