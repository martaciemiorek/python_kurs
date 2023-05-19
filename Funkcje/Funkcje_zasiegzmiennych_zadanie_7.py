

def is_card_number(num):
    if num.isdigit():
        return True
    else:
        return False
def card_input_length():
    if len(card_number) >= 13 and len(card_number)<17:
        print("to karta")
    else:
        print("to nie karta")
card_input_length()

def is_visa():
    if card_number[0] == '4' and len(card_number) == 16:
        print("nowa visa")
    elif card_number[0] == '4' and len(card_number) == 13:
        print("stara visa")
    else:
        print("to nie visa")
is_visa()

def is_mastercard():
    if card_number[0] != 5:
        print("to nie mastercard")
    elif card_number[1]>=1 and card_number[1] <=5:
        print("mastercard")
    else:
        print("nie mastercard")

def is_americanexpress():
    if card_number[0] == 34:
        print


card_number = input("Podaj numer karty: ")