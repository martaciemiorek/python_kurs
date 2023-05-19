
def check_scope(num1, num2, numx):
    if numx <num2 and numx > num1:
        print(f"tak, liczba {numx} znajduje się w zadanym zakresie")
    else:
        print(f"nie, liczba {numx} jest z poza zakresu")

numx = int(input("podaj liczbę: "))
num1 = int(input("podaj początek zakresu: "))
num2 = int(input("podaj koniec zakresu: "))

check_scope(num1, num2, numx)