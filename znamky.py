'''
Zadání:
1. Uživatel bude zadávat známky (1..5) do pole, které
    bude velké, tak jak uživatel určí.
    ( for cyklus a v něm pole.append() )
2. Součet všech známek se stejnou hodnotou
    -> kolik jsem dostal jedniček, kolik dvojek...

'''
pc = int(input("Zadej počet známek: ")) #počet známek
znamky = []
j = 0
d = 0
t = 0
c = 0
p = 0

for i in range(pc):
    nzn = int(input("Zadej novou známku: ")) # nová známka
    if nzn == 1:
        j += 1
    elif nzn == 2:
        d += 1
    elif nzn == 3:
        t += 1
    elif nzn == 4:
        c += 1
    elif nzn == 5:
        p += 1
    znamky.append(nzn)

print("\nPočet:","\n1:", j,"\n2:",d,"\n3:",t,"\n4:",c,"\n5:",p)
print("Průměr známek je: ",(j+(d*2)+(t*3)+(c*4)+(p*5))/pc)

