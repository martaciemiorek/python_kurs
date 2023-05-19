names_in_countries = {
    'Poland': ['Sophia', 'Olivia', 'Zuzanna', 'Julia', 'Hanna', 'Lena', 'Maja', 'Zofia', 'Amelia', 'Alicja'],
    'Germany': ['Emma', 'Mia', 'Hannah', 'Emilia', 'Lina', 'Mila', 'Lea', 'Sophie', 'Lena', 'Anna'],
    'France': ['Emma', 'Louise', 'Alice', 'Chloé', 'Inès', 'Léa', 'Lola', 'Camille', 'Zoé', 'Julia'],
    'Italy': ['Sofia', 'Giulia', 'Aurora', 'Alice', 'Emma', 'Ginevra', 'Marta', 'Bianca', 'Mia', 'Ludovica'],
    'Spain': ['Lucía', 'Sofía', 'Martina', 'María', 'Paula', 'Julia', 'Valeria', 'Daniela', 'Alba', 'Emma'],
    'United Kingdom': ['Olivia', 'Amelia', 'Isla', 'Ava', 'Emily', 'Isabella', 'Mia', 'Poppy', 'Ella', 'Lily'],
    'Sweden': ['Alice', 'Maja', 'Ella', 'Ebba', 'Wilma', 'Olivia', 'Astrid', 'Alma', 'Klara', 'Saga'],
    'Netherlands': ['Emma', 'Sophie', 'Julia', 'Mila', 'Tess', 'Zoë', 'Sara', 'Eva', 'Anna', 'Lotte'],
    'Greece': ['Maria', 'Sophia', 'Eleni', 'Despoina', 'Georgia', 'Katerina', 'Alexandra', 'Ioanna', 'Antonia', 'Anna'],
    'Portugal': ['Mariana', 'Matilde', 'Leonor', 'Beatriz', 'Carolina', 'Margarida', 'Sofia', 'Alice', 'Ana', 'Francisca']
}
all_names = []

for country in names_in_countries:
    names = names_in_countries[country]
    all_names += names

print(all_names)


name_count = []
for name in all_names:
    if all_names.count(name) >=3 and name not in name_count:
        name_count.append(name)
print(name_count)