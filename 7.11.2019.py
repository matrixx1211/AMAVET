'''
Zadaní zkuste zadat nějakou větu
a najít v ní počet
libovolných znaků.
'''
pocdia = 0
veta = input("Zadej větu: \n")
cislo = ["0", "1", "2", "3", "4", "5", "6"]
dia = ["ě","š","č","ř","ž","ý","á","í","é","ď","ň","ů"]
znaky = []




# prohledávání věty od 0 - konec věty
for i in range(len(veta)):
    # když věta na pozici i+1 se bude rovnat
    # znaku, který zadáme ... něco udělej
    if veta[i] in dia:
        pocdia += 1
    elif veta[i] not in cislo and veta[i] not in dia:
        znaky.append(veta[i])

print("Počet znaků s háčkem nebo čárkou je: ", pocdia)
print("Počet znáků, které nepočítáme: ")
print(len(veta)-(pocdia))
# print(dict(znaky))

