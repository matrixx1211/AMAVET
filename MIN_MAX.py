x = int(input("Zadej první číslo: "))
#x - prvotní číslo 
n = int(input("Zadej s kolika čísly chceš porovnávat: "))
#n - počet čísel, které uživatel zadá

min = x
max = x
#min a max - hodnoty minima a maxima, protože i první číslo může být jedno z nich

for i in range(n):
#for - cyklus od 0 po číslo n, opakuje příkazy, které jsou odsazené
    x = int(input("Zadej další číslo: "))
    #další číslo, které budeme porovnávat 
    if x < min:
        min = x
    #if - podmínka -> když x bude menší jak min tak se do min uloží x
    if x > max:
        max = x
    #if - podmínka -> když x bude větší jak max tak se do max uloží x

print("Nejmenší číslo je: ",min,", nejvetší číslo je: ",max)
    
