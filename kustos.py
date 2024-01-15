from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class Karta:
    id: str
    jmeno: str
    prijmeni: str

class Kustos():

    def __init__(self):
        self.seznam = {}

    def pridej_kartu(self, id_karty: str, jmeno: str, prijmeni: str) -> Optional[Karta]:
        if id_karty not in self.seznam:
            nova_karta = Karta(id=id_karty, jmeno=jmeno, prijmeni=prijmeni)
            self.seznam[id_karty] = nova_karta
            return nova_karta
        else:
            print("Karta s tímto ID již existuje.")
            return None

    def odeber_kartu(self, id_karty: str) -> Optional[Karta]:
        if id_karty in self.seznam:
            odebrana_karta = self.seznam.pop(id_karty)
            return odebrana_karta
        else:
            print("Karta s tímto ID neexistuje.")
            return None

    def muze_vstoupit(self, id_karty: str) -> bool:
        return id_karty in self.seznam

# kontrola
kustos = Kustos()
karta1 = kustos.pridej_kartu("123", "Matyáš", "Táborský")
if kustos.muze_vstoupit("123"):
    print("Vstup povolen.")
else:
    print("Vstup zakázán.")

odebrana_karta = kustos.odeber_kartu("123")

if kustos.muze_vstoupit("123"):
    print("Vstup povolen.")
else:
    print("Vstup zakázán.")
