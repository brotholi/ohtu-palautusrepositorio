KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Väärä kapasiteetti")

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise ValueError("Väärä kasvatuskoko")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def _luo_lista(self, koko):
        return [0] * koko

    def kuuluu(self, n):
        if n in self.ljono:
            return True
        return False

    def lisaa(self, n):
        if n not in self.ljono:
            if self.alkioiden_lkm == len(self.ljono):
                self.kasvata_listaa()
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm +=  1
            return True
        return False

    def kasvata_listaa(self):
        uusi_koko = self.alkioiden_lkm + self.kasvatuskoko
        uusi_lista = self._luo_lista(uusi_koko)
        self.kopioi_lista(self.ljono, uusi_lista)
        self.ljono = uusi_lista


    def poista(self, n):
        if n not in self.ljono:
            return False
        self.ljono.remove(n)
        self.alkioiden_lkm -= 1
        return True

    def kopioi_lista(self, kopioitava_lista, kohde_lista):
        for i in range(0, len(kopioitava_lista)):
            kohde_lista[i] = kopioitava_lista[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        
        for joukko in [a, b]:
            for luku in joukko.to_int_list():
                yhdiste.lisaa(luku)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        for joukko in [a, b]:
            for luku in joukko.to_int_list():
                if luku in a.to_int_list() and luku in b.to_int_list():
                    leikkaus.lisaa(luku)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        for joukko in [a, b]:
            for luku in joukko.to_int_list():
                if luku in a.to_int_list() and luku not in b.to_int_list():
                    erotus.lisaa(luku)

        return erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        
        lista_str = ', '.join([str(luku) for luku in self.to_int_list()])
        return "{" + lista_str + "}"

