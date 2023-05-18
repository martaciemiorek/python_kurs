txt = input("podaj tekst ")

upper = 0
lower = 0
numbers = 0
specials = 0

for sign in txt:
    if sign.isupper():
        upper = upper + 1
print(upper)
print(f'jest {upper} wielkich liter')

for sign in txt:
    if sign.islower():
        lower = lower + 1
print(f'jest {lower} małych liter')

for sign in txt:
    if sign.isnumeric():
        numbers = numbers + 1
print(f'jest {numbers} cyfr')

for sign in txt:
    if not sign.isalnum():
        specials = specials + 1
print(f'jest {specials} znaków specjalnych')
