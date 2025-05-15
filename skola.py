class Skolotajs:
    def __init__(self, skaits, tips, uzvards):
        self.skaits = skaits
        self.tips = tips
        self.uzvards = uzvards
    
    


    
    

class SakumsskolasSkolotajs(Skolotajs):
    def __init__(self, skaits, klase, uzvards):
        super().__init__(self, skaits, uzvards)
        self.klase = klase
    
    tips = int(input("Ievadiet skolotājas tipu (1 - sākumsskolas skolotājs, 3 - vidusskolas skolotājs): "))
    uzvards = input("Ievadiet skolotāja uzvārdu: ")
    klase = input("Ievadiet skolotāja klasi: ")

    skaits = int(input("Ievadiet skolotāju stundu skaitu: "))

    print("Sākumsskolas (tips - 1) skolotājs ",uzvards," māca ",skaits," stundas ",klase," klasē.")

        

class VidusskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, prieksmets1, prieksmets2, stundas1, stundas2):
        self.uzvards = uzvards
        self.prieksmets1 = prieksmets1
        self.prieksmets2 = prieksmets2
        self.stundas1 = stundas1
        self.stundas2 = stundas2

    tips = int(input("Ievadiet skolotājas tipu (1 - sākumsskolas skolotājs, 3 - vidusskolas skolotājs): "))
    uzvards = input("Ievadiet skolotāja uzvārdu: ")
    prieksmets1 = input("Ievadiet pirmo pasniegto priekšmetu: ")
    stundas1 = int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))
    prieksmets2 = input("Ievadiet otro pasniegto priekšmetu: ")
    stundas2 = int(input("Ievadiet otrā priekšmeta stundu skaitu: "))
    
    stundask = stundas1+stundas2
    print("Vidusskolas (tips - 3) skolotājs ",uzvards," māca šādus priekšmetus: ",prieksmets1," un ", prieksmets2," kopā ",stundask," stundas.")


# def ievade():
#     tips = int(input("Ievadiet skolotājas tipu (1 - sākumsskolas skolotājs, 3 - vidusskolas skolotājs): "))

#     if tips == 1:
#         uzvards = input("Ievadiet skolotāja uzvārdu: ")
#         klase = input("Ievadiet skolotāja klasi: ")
#         skaits = int(input("Ievadiet skolotāju stundu skaitu: "))
#         SakumsskolasSkolotajs(skaits, klase, uzvards,tips)
#     elif tips == 3:
#         uzvards = input("Ievadiet skolotāja uzvārdu: ")
#         prieksmets1 = input("Ievadiet pirmo pasniegto priekšmetu: ")
#         stundas1 = int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))
#         prieksmets2 = input("Ievadiet otro pasniegto priekšmetu: ")
#         stundas2 = int(input("Ievadiet otrā priekšmeta stundu skaitu: "))
#         VidusskolasSkolotajs(prieksmets1, prieksmets2, tips, stundas1, stundas2, uzvards)

# ievade()
        

obj2 = SakumsskolasSkolotajs(0,"","")
obj3 = VidusskolasSkolotajs("","",0,"",0)
