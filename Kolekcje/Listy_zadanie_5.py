lista_danych = [
    ["Dorota", "Wellman", "dziennikarka"],
    ["Adam", "Małysz", "sportowiec"],
    ["Robert", "Lewandowski", "piłkarz"]
]

for item in lista_danych:
    print(item)
    for item2 in item:
        print(item2, end= " -")