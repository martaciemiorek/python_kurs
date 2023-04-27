password = str(input("podaj haslo "))

if len(password) < 8 :
    print("hasło powinno zawierać co najmniej 8 znaków")
if password.isalnum() and password.isdigit():
    print("hasło powinno zawierać co najmniej jedną literę")
if password.isalnum() and password.isalpha():
    print("hasło powinno zawierać co najmniej jedną cyfrę")
if password.islower():
    print("hasło powinno zawierać co najmniej jedną wielką literę")


