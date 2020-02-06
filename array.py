cars = ["Ford", "Volvo", "BMW", "Renault", "Ferrari", "Lamborghini"]
#n = int(input("Zadej počet položek, \nkteré chceš přidat do pole
a = input("Chceš začít vkládat A/N: ")

if a.upper() == "A":
    log = True

while log:
    novapolozka = input("Zadej novou položku: \n")
    cars.append(novapolozka)
    a = input("Chceš pokračovat ve vkládání A/N: ")
    if a.upper() == "A" or a == "":
        log = True
    else:
        log = False
        
    

'''for i in range(n):
    novapolozka = input("Zadej novou položku: \n")
    cars.append(novapolozka)'''

pocitadlo = 0  
print("\nPole:\n ")
for j in cars:
    pocitadlo += 1
    print(pocitadlo, j)








#print(cars) #vypíše pole
#print(cars[0]) #vypíše první (0) položku v poli

'''cars[2] = "CDE" #změní 3 položku s indexem 2 na CDE

cars.append("ABC") #přidá položku ABC

print("Od A - Z")
cars.sort() #seřadí pole od A-Z

for x in cars: #vypíše všechny položky z pole
  print(x)

print("\n") #musí být \ - nový řádek

print("Od Z - A")
cars.sort(reverse=True) #seřadí pole od Z-A

for x in cars: #vypíše všechny položky z pole
  print(x)''' 
