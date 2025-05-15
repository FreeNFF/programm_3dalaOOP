class Auto:
    def __init__(self, zimols, modelis, datums, masa, degviela):
        self.zimols = zimols
        self.modelis = modelis
        self.datums = datums
        self.masa = masa
        self.degviela = degviela
    
    def izvade(self):
        print(f"Zīmols: {self.zimols}\nModelis: {self.modelis}\nReģistrācijas datums: {self.datums}\nPilna masa: {self.masa}\nDegvielas veids:{self.degviela}")

obj= Auto("Audi","A4","22.10.2019",1800,"BG")
obj.izvade()

