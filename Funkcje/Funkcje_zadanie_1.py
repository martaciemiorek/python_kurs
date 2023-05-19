

def circle_area(diameter):
    return 3.14 * diameter**2 / 4

diameter = int(input("podaj średnicę: "))
area = circle_area(diameter)
print(f'pole powierzchni to {area}')