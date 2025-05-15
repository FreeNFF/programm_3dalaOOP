# klase Skolotajs
class Skolotajs:
    def __init__(self, uzvards, stundu_skaits_nedela, tips):
        self.uzvards = uzvards
        self.stundu_skaits_nedela = stundu_skaits_nedela
        self.tips = tips

    def izdrukat(self):
        pass  # Izdruka tiek norādīta atvasinātajās klasēs


# klase SakumskolasSkolotajs
class SakumskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, klase, stundu_skaits_nedela):
        super().__init__(uzvards, stundu_skaits_nedela, tips=1)# piekļuve vecākās klases metodēm un atribūtiem no atvasinātās klases
        self.klase = klase

    def izdrukat(self):
        print(f"Sākumskolas skolotājs - {self.uzvards}, klase: {self.klase}, stundas nedēļā: {self.stundu_skaits_nedela}")


# klase VidusskolasSkolotajs
class VidusskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, pirmais_prieksmets, otrais_prieksmets, stundu_skaits_pirmais, stundu_skaits_otraiss):
        kop_stundas = stundu_skaits_pirmais + stundu_skaits_otraiss
        super().__init__(uzvards, kop_stundas, tips=1)
        self.pirmais_prieksmets = pirmais_prieksmets
        self.otraiss_prieksmets = otrais_prieksmets
        self.stundu_skaits_pirmais = stundu_skaits_pirmais
        self.stundu_skaits_otraiss = stundu_skaits_otraiss

    def izdrukat(self):
        print(f"Vidusskolas skolotājs - {self.uzvards}, priekšmeti: {self.pirmais_prieksmets}, {self.otraiss_prieksmets}, "
              f"stundas nedēļā kopā: {self.stundu_skaits_nedela}")


# Funkcija datu ievadei un izvadei
def ievade():
    skolotaji = []
    
    while True:
        tips = input("Ievadiet skolotāja tipu (1 - sākumskola, 3 - vidusskola, 0 - beigt ievadi): ")
        
        if tips == '0':
            break
        elif tips == '3':
            uzvards = input("Ievadiet skolotāja uzvārdu: ")
            pirmais_prieksmets = input("Ievadiet pirmā priekšmeta nosaukumu: ")
            otraiss_prieksmets = input("Ievadiet otrā priekšmeta nosaukumu: ")
            stundu_skaits_pirmais = int(input("Ievadiet stundu skaitu pirmajam priekšmetam: "))
            stundu_skaits_otraiss = int(input("Ievadiet stundu skaitu otrajam priekšmetam: "))
            skolotajs = VidusskolasSkolotajs(uzvards, pirmais_prieksmets, otraiss_prieksmets, stundu_skaits_pirmais, stundu_skaits_otraiss)
   
        elif tips == '1':
            uzvards = input("Ievadiet skolotāja uzvārdu: ")
            klase = input("Ievadiet klasi, kurā pasniedz skolotājs: ")
            stundu_skaits = int(input("Ievadiet stundu skaitu nedēļā: "))
            skolotajs = SakumskolasSkolotajs(uzvards, klase, stundu_skaits)
            
        else:
            print("Nepareizs tips! Mēģiniet vēlreiz.")
            continue

        skolotaji.append(skolotajs)
    
    print("\nSkolotāju saraksts:")
    for skolotajs in skolotaji:
        skolotajs.izdrukat()


# Programmas izpilde
ievade()
