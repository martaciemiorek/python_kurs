def even_number(number):
    if number % 2 ==0:
        print("jest parzysta")
    else:
        print("nie jest parzysta")

number = int(input("podaj liczbe: "))
even_number(number)