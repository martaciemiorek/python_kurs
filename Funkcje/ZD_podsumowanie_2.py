
def min_value(num1, num2,num3):
    if num1 < num2 and num1<num3:
        print(f'{num1} jest najmniejszą liczbą')
    elif num2 < num1 and num2 <num3:
        print(f'{num2} jest najmniejszą liczbą')
    else:
        print(f'{num3} jest najmniejszą liczbą')


num1 = int(input("Podaj liczbę nr 1: "))
num2 = int(input("Podaj liczbę nr 2: "))
num3 = int(input("Podaj liczbę nr 3: "))

min_value(num1, num2, num3)

