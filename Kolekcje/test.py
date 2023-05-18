abrakadabra = "abrakadabra"
print(abrakadabra[4])

print("----------")
i=0
for i in range(len(abrakadabra)):
    if i % 2 != 0:
        print(abrakadabra[i])
print("----------")

for i in range(1, len(abrakadabra), 2):
    print(abrakadabra[i])
print("----------")

i = 0
while i < len(abrakadabra):
    if i % 2 != 0:
        print(abrakadabra[i])
    i += 1