#Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.
#Możemy wykorzystać pętle for oraz metodę count. Dodajemy do duplikatów liczbę jeśli dana liczba występuje w
# tupli więcej niż 1 raz.
#Dodatkowo można zrobić ifa by do duplikatów daną liczbę dodać tylko raz.
#(spróbuj teraz z tym opisem rozwiązać zadanie).



my_tuple = 1, 6, 3, 3, 3, 3, 2, 2, 5, 5, 5
duplicates = []
for item in my_tuple:
    print(my_tuple.count(item))
    if my_tuple.count(item) >1:
        if item not in duplicates:
            duplicates.append(item)
print(duplicates)

