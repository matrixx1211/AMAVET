'''
| Vypiš složenou větu podle uživatelského výběru.
'''
#ČÁST 1
pocitadlo = 1
p = ["Ahoj já jsem", "Jak se máš", "Kde se sejdeme"]
for i in p:
    print(pocitadlo, ".", i)
    pocitadlo += 1
pz = int(input("Zadej větu, kterou sis vybral."))

#ČÁST 2
pocitadlo = 1
print("\n", p[pz-1], "\n")
if pz == 1:
    d = ["Marek", "Petr", "Evžen"]
elif pz == 2:
    d = ["dobře", "špatně", "docela to jde", "luxusně", "..."]
elif pz == 3:
    d = ["na Špilasu", "u koně", "pod hodinama"]

for i in d:
    print(pocitadlo, ".", i)
    pocitadlo += 1
dz = int(input("Zadej větu, kterou sis vybral."))

print("\n", p[pz-1], d[dz-1], "\n")
