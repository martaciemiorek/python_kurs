
def bmi_calc(waga, wzrost):
    return waga / (wzrost * wzrost)

wzrost = input("podaj wzrost w m ")
waga = input("podaj wagę w kg ")

wzrost = float(wzrost.replace(",", "."))
waga = float(waga.replace(",", "."))

bmi_calc(waga, wzrost)

if bmi_calc(waga, wzrost) < 18.5:
    print("Twoje BMI to ", round(bmi_calc(waga, wzrost),2), ", masz niedowagę")
elif bmi_calc(waga, wzrost) >=18.5 and bmi_calc(waga, wzrost) < 25:
    print("Twoje BMI to ", round(bmi_calc(waga, wzrost),2), ", masz wagę w normie")
elif bmi_calc(waga, wzrost) >= 25 and bmi_calc(waga, wzrost) < 30:
    print("Twoje BMI to ", round(bmi_calc(waga, wzrost),2), ", masz nadwagę")
elif bmi_calc(waga, wzrost) >= 30:
    print("Twoje BMI to ", round(bmi_calc(waga, wzrost), 2), ", jesteś otyły")

print(f'Your BMI is: {bmi_calc(waga, wzrost)}')