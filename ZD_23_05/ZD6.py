def open_file():
    with open("credit_card_numbers.txt",'r') as fopen:
        cards = fopen.readlines()
        cards_list = []
        for card in cards:
            card_nb = card.strip().split(",")
            cards_list.extend(card_nb)
    return cards_list


def is_visa(card):
    """Function that checks visa numbers"""
    return card[0] == '4' and (len(card) == 16 or len(card) == 13)
    # if card_num[0] == '4' and (len(card_num) == 16 or len(card_num) == 13):
    #     return True
    # else:
    #     return False


def is_mastercard(card):
    """Function that checks mastercard numbers"""
    start_condition = int(card[0:2]) in range(51, 56) or int(card[0:4]) in range(2221, 2721)

    return len(card) == 16 and start_condition
    # if len(card_num) == 16 and start_condition:
    #     return True
    # else:
    #     return False


def is_amex(card):
    """Function that checks amex numbers"""
    return len(card) == 15 and card[0:2] in ('34', '37')
    # if len(card_num) == 15 and card_num[0:2] in ('34', '37'):
    #     return True
    # else:
    #     return False


def main(cards_list):
    visa_file = []
    mastercard_file = []
    amex_file = []

    for card in cards_list:
        print('💳 :', card)

        if is_visa(card):
            visa_file.append(card)
        elif is_mastercard(card):
            mastercard_file.append(card)
        elif is_amex(card):
            amex_file.append(card)

    with open ("visa_card_numbers.txt", "w") as visa:
        for number in visa_file:
            visa_file.write(number + ",")

    with open ("mastercard_card_numbers.txt", "w") as mastercard:
        for number in mastercard_file:
            mastercard_file.write(number + ",")

    with open ("amex_card_numbers.txt", "w") as amex:
        for number in amex_file:
            amex_file.write(number + ",")

# --- main part of the program


cards_list = open_file()
main(cards_list)