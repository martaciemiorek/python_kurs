
def max_value(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f'{num1} jest największą liczbą')
    elif num2 > num1 and num2 > num3:
        print(f'{num2} jest największą liczbą')
    else:
        print(f'{num3} jest największą liczbą')


num1 = int(input("Podaj liczbę nr 1: "))
num2 = int(input("Podaj liczbę nr 2: "))
num3 = int(input("Podaj liczbę nr 3: "))

max_value(num1, num2, num3)

