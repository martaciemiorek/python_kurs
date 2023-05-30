import random

with open("quotes.txt", encoding= 'UTF-8') as fopen:
    quotes = fopen.readlines()


for i in range(3):
    random_number = random.randrange(0,len(quotes)+1)
    print(quotes[random_number])


