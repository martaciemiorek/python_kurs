dystans= input("podaj długość trasy [km]: ")
spalanie = input("podaj spalanie na 100 km [l/km]: ")
cena_1l_paliwa = input("podaj cenę paliwa [zł/l]: ")

dystans = float(dystans.replace(",","."))
spalanie = float(spalanie.replace(",","."))
cena_1l_paliwa = float(cena_1l_paliwa.replace(",","."))

koszt_trasy = spalanie * dystans * cena_1l_paliwa /100

print("koszt trasy to", koszt_trasy, "zł")