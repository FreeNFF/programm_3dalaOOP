class Cilveks:

    def __init__(self, vards, vecums, dzimums):
        self.vards = vards
        self.vecums = vecums
        self.dzimums = dzimums

    def izvade(self):
        print(f"Manis sauc {self.vards}, man ir {self.vecums} gadi, esmu {self.dzimums}.")

class Skola(Cilveks):
    def __init__(self, vards, vecums, dzimums, skolaNosaukums):
        super().__init__(vards, vecums, dzimums)
        self.skolaNosaukums = skolaNosaukums

    def izvade(self):
        super().izvade()
        print(f"Mācos {self.skolaNosaukums}.")


vards = input("Ievadi savu vārdu: ")
vecums= int(input("Ievadu savu vecumu (skaitli): "))
dzimums = input("Ievadi savu dzimumu: ")
skolaNosaukums = input("Ievadi skolu, kurā mācies: ")

# skolens = Skola("Jānis", 18, "vīrietis", "Ķekavas vidusskolā")
skolens = Skola(vards, vecums, dzimums, skolaNosaukums)
skolens.izvade()

