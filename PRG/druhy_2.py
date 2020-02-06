a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
x = int(input("x: "))

if x == 0: #když x je 0
    print("x je nula -> NELZE ! :)")
else:
    vysledek = a * pow(x, 2) + b * x + c
    print("Výsledek: ",vysledek)

if x != 0: #když x není 0
    print("Výsledek: ",a * (x*x) + b * x + c)

if (x == 1 and a == 1 and b == 1 and c == 1):
    print("Výsledek je 3")

#x = a * (x*x) + b * x + c
#print("Výsledek: ", x)
