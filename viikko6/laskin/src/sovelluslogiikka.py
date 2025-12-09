class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo

    def aseta_arvo(self, arvo):
        self._arvo = arvo

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
        pass
