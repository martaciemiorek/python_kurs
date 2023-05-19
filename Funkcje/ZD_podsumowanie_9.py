car_dict = {'marka': 'Renault', 'model' : 'Clio', 'rocznik' : 1980}
print(car_dict)
car_dict['if_original'] = True
print(car_dict)
def check_age():
    prod_year=car_dict['rocznik']
    brand = car_dict['marka']
    originality = car_dict['if_original']
    if prod_year <= 1998 and originality == True:
        print(f"Gratulacje! Twój samochód {brand} może być zarejestrowany jako zabytek.")
    else:
        print(f'Twój samochód {brand} jest jeszcze zbyt młody.')

check_age()