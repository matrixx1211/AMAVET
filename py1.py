z = input("Chceš začít počítat A/N: ")
if z.upper() == 'A':
    start = True
else:
    start = False
    print("Děkuji za využití programu")
while start:
    x = input("Zadej číslo x: ")
    op = input("Zadej operátor: ")
    y = input("Zadej číslo y: ")
    for i in range(len(x)):
        if x[i] == ',':
            x[i] = '.'
    if op == '+':
        print(float(x)+float(y))
    elif op == '-':
        print(float(x)-float(y))
    elif op == '*':
        print(float(x)*float(y))
    elif op == '/':
        print(float(x)/float(y))
    else:
        print("Zadal si neplatné znaky...")
    z = input("Chceš pokračovat A/N: ")
    if z.upper() == 'A':
        start = True
    else:
        start = False
        print("Děkuji za využití programu")
