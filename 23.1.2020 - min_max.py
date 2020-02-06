'''
#Zadání
# Naprogramuj program, který bude hledat
# nejmenší a největší číslo.
# 1) po načtení všech čísel
# 2) v průběhu načítaní
'''
#1)
print("První varianta.\n")
cisla = []
n = int(input("Zadej počet čísel, které chceš zadat: "))
x = int(input("Zadej číslo: "))
#musí se nastavit nějaké hodnoty
mini = x
maxi = x

for i in range(n-1):
    x = input("Zadej číslo: ")
    cisla.append(int(x))
z = 0
for i in cisla:
    
    if cisla[z] < mini:
        mini = cisla[z]

    if cisla[z] > maxi:
        maxi = cisla[z]
    z +=1
print("\nMinumum je: ",mini,".\nMaximum je: ",maxi,".")










#2)
print("\nDruhá varianta.\n")
n = int(input("Zadej počet čísel, které chceš zadat: "))

x = int(input("Zadej číslo: "))
#musí se nastavit nějaké hodnoty
mini = x
maxi = x

for i in range(n-1):
    x = int(input("Zadej číslo: "))
    if x > maxi:
        maxi = x
    if x < mini:
        mini = x
print("\nMinumum je: ",mini,".\nMaximum je: ",maxi,".")





