#Policz wszystkie znaki w napisie
#Nie modyfikując zmiennej wyświetl słowo wisdom
#Wyświetl tylko pierwszą połowę tekstu
#Wyświetl tylko kropkę
#Wyświetl od połowy tylko co trzecią literę cytatu
#Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
#Wyświetl cały cytat odwrotnie
#Zamień wisdom na słowo friendship


quote = "Honesty is the first chapter in the book of wisdom."

print(len(quote))
print(quote[-7:-1])
print(quote[:25])
print(quote[-1])
print(quote[25:51:3])
print((quote[::2]))
print(quote.)
print(quote.replace("wisdom","friendship"))
