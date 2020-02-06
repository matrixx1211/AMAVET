otazky = ['Hlavní město ČR?', "Co je za rok?"]
odpovedi = [['PRAHA', 'BRNO', 'OLOMOUC', "OSTRAVA", "LIBIREC", "PLZEŇ", "MORAVANY", "ŽIDLOCHOVICE", "JEDOVNICE"],["2025","1915", "2020"]]
spravnaodpoved = ["1","3"]

#počáteční hodnota pro body
body = 0

for i in range(len(otazky)):
    print (otazky[i])
    for j in range(len(odpovedi[i])):
        print (j+1,". ",odpovedi[i][j])
    moje = input("Zadej svoji odpověď ?")
    if (moje == spravnaodpoved[i]):
        body += 1
        print ("Odpověděl si správně. [",body,"]")
    else:
        print ("Odpověděl si špatně. [",body,"]")

print ("Tvůj počet bodů je: ",body)
