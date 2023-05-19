user1 = input("Podaj 4 przedmioty szkolne: ")
user2 = input("Podaj 4 przedmioty szkolne: ")
user3 = input("Podaj 4 przedmioty szkolne: ")
user4 = input("Podaj 4 przedmioty szkolne: ")
user5 = input("Podaj 4 przedmioty szkolne: ")

user1_list = list(user1.lower().split())
user2_list = list(user2.lower().split())
user3_list = list(user3.lower().split())
user4_list = list(user4.lower().split())
user5_list = list(user5.lower().split())

all_classes =  user2_list+user1_list + user5_list + user4_list + user3_list

print(all_classes)

popular_class = {}
for subject in all_classes:
    if subject in popular_class:
        popular_class[subject] += 1
    else:
        popular_class[subject] = 1

print(popular_class)


most_popular_class = max(popular_class, key=popular_class.get)
print(f'najczęściej wybierany przedmiot to: {most_popular_class}')