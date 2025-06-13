class Darbinieks():
    def __init__(self, vards, uzvards):
        self.vards = vards
        self.uzvards = uzvards

    def izvade(self):
        return print(f"Darbinieka vārds un uzvārds: {self.vards} {self.uzvards}")
    
    def bruto(self):
        return 0

    def neto(self):
        return self.bruto() * 0.8
    
        
    
class OfisaDarbinieks(Darbinieks):
    def __init__(self, vards, uzvards, nauda_stunda, stundas):
        super().__init__(vards,uzvards)
        self.nauda_stundas = nauda_stunda
        self.stundas = stundas

    def izvade(self):
        return print(f"Ofisa darbinieka vārds un uzvārds: {self.vards} {self.uzvards}")

    def bruto(self):
        return self.nauda_stundas * self.stundas
    

    
class RupniecibasDarbinieks(Darbinieks):
    def __init__(self, vards, uzvards, nauda_stunda, stundas, maina):
        super().__init__(vards,uzvards)
        self.nauda_stundas = nauda_stunda
        self.stundas = stundas
        self.maina = maina

    def izvade(self):
        return print(f"Rūpniecības darbinieka vārds un uzvārds: {self.vards} {self.uzvards}")

    def bruto(self):
        if self.maina.lower() == "nakts":
            return self.nauda_stundas * self.stundas * 1.1
        else:
            return self.nauda_stundas * self.stundas
        

d1 = OfisaDarbinieks("Zigmārs", "Liepiņš", 10, 160)
print(d1.izvade())
print(f"Bruto: {d1.bruto():.2f}")
print(f"Neto: {d1.neto():.2f}")

d2 = RupniecibasDarbinieks("Ansis", "Liepiņš", 8, 160, "Nakts")
print(d2.izvade())
print(f"Bruto: {d2.bruto():.2f}")
print(f"Neto: {d2.neto():.2f}")
    


        
