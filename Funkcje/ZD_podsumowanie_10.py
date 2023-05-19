import random
print("Zagrajmy w wisielca. Masz 10 prób.")
words_list = ['kot', 'pies', 'dom', 'samochód', 'kwiat', 'książka', 'drzewo', 'telefon', 'muzyka', 'piłka']
random_number= random.randint(0,len(words_list)-1)
print(random_number)
word = words_list[random_number]
print(word)
guessed_letters =[]

def puzzle_length():
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("-", end=" ")

def check_letter(user_letter):
    if user_letter in word:
       print("Trafione")
       print(user_letter, end="")
       guessed_letters.append(user_letter)
    elif user_letter in word:
        print("-", end="")
    else:
        print("Nietrafione, spróbuj jeszcze raz!")


puzzle_length()


for n in range(1,11):
    user_letter = input("podaj literę: ")
    check_letter(user_letter)
    puzzle_length()


