import random
print("Zagraj w kamień papier nożyce. Żeby zakończyć grę wpisz KONIEC")

rounds_nbr = int(input("podaj liczbę rund: "))

users_wins = 0
computers_wins = 0

repeats = 0

for n in range(1, rounds_nbr+1):
    repeats = repeats + 1
    user_choice = input("wybierz kamień (k) / papier (p) / nożyce (n): ")
    possibilities = ["k", "p", "n"]
    computers_choice = random.choice(possibilities)
   #print(f'użytkownik: {user_choice}, komputer: {computers_choice}')

    if user_choice == "KONIEC":
        print("KONIEC GRY")
        break

    if user_choice == computers_choice:
            print("Remis!")
    elif user_choice == "k":
        if computers_choice == "p":
            computers_wins += 1
            print("Przegrywasz!")
        else:
            users_wins += 1
            print("Wygrywasz!")
    elif user_choice == "p":
        if computers_choice == "k":
            users_wins += 1
            print("Wygrywasz!")
        else:
            computers_wins += 1
            print("Przegrywasz!")
    elif user_choice == "n":
        if computers_choice == "k":
            users_wins += 1
            print("Wygrywasz!")
        else:
            computers_wins += 1
            print("Przegrywasz!")

print(f'WYNIK: użytkownik vs. komputer {users_wins} : {computers_wins}')