'''
n = int(input("Počet kolikrát se cyklus provede: "))
i = 1

while i < n+1:
    print(i)
    i += 1
'''

z = int(input("Zadej číslo, které se bude umocňovat: "))
n = int(input("Zadej na kolikátou: "))
pom = z
i = 1

while i < n+1:
    print(i,".krok - ",z)
    i += 1
    z = pom * z
    

