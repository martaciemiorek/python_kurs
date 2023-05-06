title = str(input("podaj tutyl  "))
surname = str(input("podaj nazwisko autora "))
pages = str(input("podaj liczbe stron "))

print(title.isalpha())
print(pages.isdigit())

capitalized_title = title.capitalize()
capitalized_surname = surname.capitalize()
print(capitalized_title)
print(capitalized_surname)

book = capitalized_title + " " + capitalized_surname + " " + pages
print(book)
print(len(book))
