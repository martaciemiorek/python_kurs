names = input("wprowadz liste imion rozdzielonych przecinkiem lub spacja ")
name_list = names.replace(" ", ",").split(",")

for name in name_list:
    print("czesc ", name)