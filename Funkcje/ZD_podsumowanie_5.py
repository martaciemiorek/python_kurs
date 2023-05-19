import random

computer_nbr = random.randint(0, 100)
print(computer_nbr)
#user_nbr = int(input("podaj liczbę "))
def cieplo_zimno():
    trial = 0
    for n in range(1, 7):
        trial = trial +n
        user_nbr = int(input("podaj liczbę "))

        if user_nbr == computer_nbr:
            print("Wygrywasz!")
            break
        elif user_nbr > computer_nbr +10 or user_nbr < computer_nbr -10:
            print("zimno, spróbuj jeszcze raz")
        else:
            print("ciepło")
            user_nbr = int(input("podaj liczbę "))
    print("Komputer wygrywa!")


cieplo_zimno()