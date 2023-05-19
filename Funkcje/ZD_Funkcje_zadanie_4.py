def even_number(number):
    if number % 2 ==0:
        return True
        print("jest parzysta")
    else:
        return False
        print("nie jest parzysta")

number_list = (input("podaj liczby: "))
int_list = [int(num) for num in number_list.split()]
for number in int_list:
    if even_number(number):
        print(number)


