from tuomari import Tuomari

class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()

        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            # toka siirtäjä ei saa tietää ekaa siirtoa valitessaan siirtoa
            edellinen_ekan_siirto = ekan_siirto
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(edellinen_ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, edellinen_ekan_siirto):
        raise Exception("Tämä metodi pitää korvata aliluokassa")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"


def luo_peli(tyyppi):
    from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
    from kps_tekoaly import KPSTekoaly
    from kps_parempi_tekoaly import KPSParempiTekoaly

    if tyyppi == "a":
        return KPSPelaajaVsPelaaja()
    elif tyyppi == "b":
        return KPSTekoaly()
    elif tyyppi == "c":
        return KPSParempiTekoaly()

    return None
