#Funkce bez argumentu libovolnyNazevFunkce()
'''
def libovolnyNazevFunkce():
    #příkazy funkce
    print("Tohle je výpis funkce")

libovolnyNazevFunkce()
'''
#Funkce s argumentem libovolnyNazevFunkce(x, y)
'''
def libovolnyNazevFunkce(x, y):
    #příkazy Funkce
    print("\nTohle je výpis z funkce")
    x = int(x)
    y = int(y)
    print(x,"+",y,"=",x+y)


x = input("Zadej číslo x: ")
y = input("Zadej číslo y: ")
print(x+y)

libovolnyNazevFunkce(x,y)

print("\nPo funkci",x+y)
'''

def prvni():
    x = int(input("Zadej číslo x: "))
    y = int(input("Zadej číslo y: "))
    #Funkce vracející hodnotu
    #return vrací hodnotu
    return x*y

def druha():
    x = float(input("Zadej číslo x: "))
    y = float(input("Zadej číslo y: "))
    return x/y

#volání funkcí
'''prvni()
druha()'''

#volaní funkcí ve funkci print
print("print funkce")
print(prvni())
print(druha())

#print podílu funkcí
print("print podílu")
print(prvni()/druha())
