from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KiviPaperiSakset):
    def _toisen_siirto(self, ekan_siirto):
        tekoaly_parannettu = TekoalyParannettu(10)
        tokan_siirto = tekoaly_parannettu.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        tekoaly_parannettu.aseta_siirto(ekan_siirto)

        return tokan_siirto
