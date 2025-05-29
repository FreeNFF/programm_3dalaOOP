class Skolotajs:
    def __init__(self, uzvards, stundu_skaits, tips):
        self.uzvards = uzvards
        self.stundu_skaits = stundu_skaits
        self.tips = tips

    def izvade(self):
        pass

class SakumsskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, stundu_skaits, klase):
        super().__init__(uzvards, stundu_skaits, tips=1)
        self.klase = klase

    def izvade(self):
        print(f"Sākumskolas (tips – {self.tips}) skolotājs {self.uzvards} māca {self.stundu_skaits} stundas {self.klase} klasē.")

class VidusskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, stundas_pirmais, stundas_otrais, prieksmets_viens, prieksmets_divi):
        stundu_skaits = stundas_pirmais + stundas_otrais
        super().__init__(uzvards, stundu_skaits, tips=3)
        self.stundas_pirmais = stundas_pirmais
        self.stundas_otrais = stundas_otrais
        self.prieksmets_viens= prieksmets_viens
        self.prieksmets_divi = prieksmets_divi
        
        

    def izvade(self):
        print(f"Vidusskolas (tips – {self.tips}) skolotājs {self.uzvards} māca šādus priekšmetus: {self.prieksmets_viens} un {self.prieksmets_divi}, kopā {self.stundu_skaits} stundas.")

def sakumsskola():
    uzvards = input("Ievadiet sākumskolas skolotāja uzvārdu: ")
    klase =input("Ievadiet skolotāja klasi: ")
    stundu_skaits = int(input("Ievadiet skolotāja stundu skaitu: "))
    return SakumsskolasSkolotajs(uzvards, stundu_skaits, klase)
    

def vidusskola():
    uzvards = input("Ievadiet vidusskolas skolotāja uzvārdu: ")
    prieksmets_viens = input("Ievadiet pirmo pasniegto priekšmetu: ")
    stundas_pirmais = int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))
    prieksmets_divi = input("Ievadiet otro pasniegto priekšmetu: ")
    stundas_otrais = int(input("Ievadiet otrā priekšmeta stundu skaitu: "))
    return VidusskolasSkolotajs(uzvards,  stundas_pirmais, stundas_otrais, prieksmets_viens, prieksmets_divi)
    

def programma():
    input("Ievadiet skolotāju tipu (1 - sākumsskola): ")
    skolotajs1 = sakumsskola()
    input("Ievadiet skolotāju tipu (3 - vidussskola): ")
    skolotajs2 = vidusskola()

    skolotajs1.izvade()
    skolotajs2.izvade()

programma()


