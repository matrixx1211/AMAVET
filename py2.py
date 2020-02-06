class Calc():  # objekt s názvem Calc
    """docstring for Calc."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):  # funkce objektu Calc s jménem add
        return float(x)+float(y)

    def div(self):  # funkce objektu Calc s jménem div-ide
        return float(x)/float(y)

    def mul(self):  # funkce objektu Calc s jménem mul-tiply
        return float(x)*float(y)

    def sub(self):  # funkce objektu Calc s jménem sub-tract
        return float(x)-float(y)


z = "A"
# z.upper() == "" -> ENTER -> odeslání prázdného stringu
while z.upper() == "A" or z.upper() == "":
    x = input("Zadej první číslo: ")
    op = input("Zadej operátor: ")
    y = input("Zadej druhé číslo: ")
    prob = Calc(x, y)
    #  instance třídy Calc s parametry x a y
    if op == '+':
        print(prob.add())
    elif op == '-':
        print(prob.sub())
    elif op == '*':
        print(prob.mul())
    elif op == '/':
        print(prob.div())
    z = input("Chceš pokračovat ? (A/N)")
else:
    print("Děkuji za použití toho programu. :)")
