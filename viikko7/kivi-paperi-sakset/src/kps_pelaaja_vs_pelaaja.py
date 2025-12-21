from kps import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, edellinen_ekan_siirto):
        return input("Toisen pelaajan siirto: ")
