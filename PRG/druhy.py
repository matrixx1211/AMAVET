#x - proměnná
#print("text") / print(x) - vypsání textu/proměnné
#x = input("text") / x = input() - uživatelský vstup
#komentář - neovlivní kód
#float - desetinná čísla, int - celá kladná (1,2,3)
x = int(input("Zadej číslo, které chceš násobit: "))
y = int(input("Zadej kolikrát ho chceš násobit: "))
z = int(input("Zadej čím chceš násobit: "))

if x == 0 or y == 0 or z == 0:
    print("Zadal si nulu.")

else:
    for i in range(y): #cyklus od 0 - y
        x = z * x
    print(x) #výpis výsledku


