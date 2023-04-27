f_temp = 0

for temp in range(0, 200, 20):
    c_temp = 5 / 9 * (f_temp - 32)
    print(c_temp)
    f_temp = f_temp + 20