class Doktorats:
    def __init__(self, nosaukums, skaits):
        self.nosaukums = nosaukums
        self.skaits = skaits

    def ievade(self):
        self.nosaukums = str(input("Ievadiet doktorāta nosaukumu: "))
        self.skaits= int(input("Ievadiet doktorāta pacientu skaitu: "))

    def izvade(self):
        print("Doktorāts ",self.nosaukums," apkalpo ",self.skaits," pacientu.")

doktors = Doktorats("",0)
doktors.ievade()
doktors.izvade()


#if __name__ == "__main__":
    #doktorats = Doktorats()
    #doktorats.ievade()
    #doktorats.izvade()
