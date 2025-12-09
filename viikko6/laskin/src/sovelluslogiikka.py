class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._historia = []
        self._arvo = arvo

    def aseta_arvo(self, arvo, tallenna_historiaan=True):
        if tallenna_historiaan:
            self._historia.append(self._arvo)

        self._arvo = arvo

    def onko_historia_tyhja(self):
        return len(self._historia) == 0

    def poista_historiasta(self):
        return self._historia.pop()

    def arvo(self):
        return self._arvo

class Miinus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self, arvo):
        self.sovelluslogiikka.aseta_arvo(self.sovelluslogiikka.arvo() - arvo)

class Plus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self, arvo):
        self.sovelluslogiikka.aseta_arvo(self.sovelluslogiikka.arvo() + arvo)

class Nollaa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self, _arvo):
        self.sovelluslogiikka.aseta_arvo(0)

class Kumoa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self, _arvo):
        if not self.sovelluslogiikka.onko_historia_tyhja():
            self.sovelluslogiikka.aseta_arvo(self.sovelluslogiikka.poista_historiasta(), tallenna_historiaan=False)
