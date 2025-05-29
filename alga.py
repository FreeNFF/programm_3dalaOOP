from ast import Str


class Darbinikes:

    def __init__(self, vards, stundas_likme, nostradatas_stundas):
        self.vards = vards
        self.stundas_likme = stundas_likme
        self.nostradatas_stundas = nostradatas_stundas
    
    def aprekini(self):
        return self.stundas_likme * self.nostradatas_stundas

class Stradnieks(Darbinikes):

    def aprekinat_algu(self):
        if 0 < self.nostradatas_stundas <= 160:
            return super().aprekini
        elif self.nostradatas_stundas>160:
            virsstundas = self.nostradatas_stundas - 160
            parasta_alga = 160 * self.stundas_likme
            virsstundas_alga = virsstundas * 1.5 * self.stundas_likme
            kop_alga = parasta_alga + virsstundas_alga

            return kop_alga
        else:
            print("Nav pareizi ievadīti dati.")
        
class Programmetajs(Stradnieks):
    def __init__(self, vards, stundas_likme, nostradatas_stundas, bonuss):
        super().__init__(vards, stundas_likme, nostradatas_stundas)
        self.bonuss = bonuss

    def aprekinat_algu(self):
        return super().aprekinat_algu() + self.bonuss

d = Darbinikes("Zigmunds",10.0, 150)
s = Stradnieks("Marks", 12.0, 180)
p = Programmetajs("Miks", 18.7, 200, 70)

print(f"Darbinieka vārds ir {d.vards}, pelna {d.aprekini()} eiro.")
print(f"Darbinieka vārds ir {s.vards}, pelna {s.aprekinat_algu()} eiro.")
print(f"Darbinieka vārds ir {p.vards}, pelna {p.aprekinat_algu()} eiro.")