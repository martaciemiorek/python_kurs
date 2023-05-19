def calculate_sum(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum

user_list = input("podaj liczby: ")
int_list = [int(num) for num in user_list.split()]
result = calculate_sum(int_list)

print(f'suma liczb to: {result}')


