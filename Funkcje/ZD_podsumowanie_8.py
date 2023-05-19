car_dict = {'marka': 'Renault', 'model' : 'Clio', 'rocznik' : 2015}
print(car_dict)

def check_age():
    prod_year=car_dict['rocznik']
    brand = car_dict['marka']
    if prod_year <= 1998:
        print(f"Gratulacje! Twój samochód {brand} może być zarejestrowany jako zabytek.")
    else:
        print(f'Twój samochód {brand} jest jeszcze zbyt młody.')

check_age()