import random #vloží knihovnu random a všechny její příkazy
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')

def a():
    hlasky = ["První drsná hláška", "Druhá krutopřísně neskutečná hláška", "Třetí fakt nejdál hláška"]
    n = random.randrange(0,len(hlasky),1) #příkazy z random
    print(hlasky[n])
    
def b():
    print("b")
    
def c(parametr):
    parametr = 12 * (parametr / 4)
    print("Dvanácti násobek podílu zadaného čísla a 4 je: ",parametr)

start = "A"

while start == "A" or start == "":
    vyber = input("Vyber, co chceš dělat \n A-hláška,\n B-b,\n C-výpočet s parametrem,\n K-konec\nTvůj výběr: ")
    if vyber.upper() == "A":
        a()
    elif vyber.upper() == "B":
        b()
    elif vyber.upper() == "C":
        parametr = int(input("Zadej číslo: "))
        c(parametr)
    elif vyber.upper() == "K":
        start = "K"
