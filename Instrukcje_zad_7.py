wzrost = input("podaj wzrost w m ")
waga = input("podaj wagę w kg ")

wzrost = float(wzrost.replace(",", "."))
waga = float(waga.replace(",", "."))

BMI = waga / (wzrost * wzrost)

if BMI < 18.5:
    print("Twoje BMI to ", round(BMI,2), ", masz niedowagę")
elif BMI >=18.5 and BMI < 25:
    print("Twoje BMI to ", round(BMI,2), ", masz wagę w normie")
elif BMI >= 25 and BMI < 30:
    print("Twoje BMI to ", round(BMI,2), ", masz nadwagę")
elif BMI >= 30:
    print("Twoje BMI to ", round(BMI, 2), ", jesteś otyły")