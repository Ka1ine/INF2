class PoupeeRusse:
    def __init__(self, nom , taille):
        self.__nom = nom
        self.__taille = taille
        self.__est_ouverte = False
        self.__dans = None
        self.__contient = None

    # -- Getters --
    @property
    def nom(self):
        return self.__nom

    @property
    def taille(self):
        return self.__taille

    @property
    def est_ouverte(self):
        return self.__est_ouverte

    @property
    def dans(self):
        return self.__dans

    @property
    def contient(self):
        return self.__contient

    # -- Setters --

    @est_ouverte.setter
    def est_ouverte(self, est_ouverte):
        if isinstance(est_ouverte, bool):
            self.__est_ouverte = est_ouverte
        else:
            raise TypeError('Il doit être de type booléen')

    @dans.setter
    def dans(self, dans_autre):
        if dans_autre is None or isinstance(dans_autre, PoupeeRusse):
            self.__dans = dans_autre
        else:
            raise TypeError("Il faut que ce soit une autre poupée ou None")

    @contient.setter
    def contient(self, contient):
        if contient is None or isinstance(contient, PoupeeRusse):
            self.__contient = contient
        else:
            raise TypeError("Il faut que ce soit une autre poupée ou None")

    # -- Fonctions --

    def ouvrir(self):
        if not self.__est_ouverte and self.__dans is None:
            self.__est_ouverte = True

    def fermer(self):
        if self.__est_ouverte and self.__dans is None:
            self.__est_ouverte = False

    def placer_dans(self, p):
        if (
            self.__dans is None
            and p.__contient is None
            and p.est_ouverte
            and not self.__est_ouverte
            and p.__taille > self.__taille
        ):
            p.__contient = self
            self.__dans = p

    def sortir_de(self):
        if self.__dans is not None and self.__est_ouverte:
            self.__dans.__contient = None
            self.__dans = None

    def __str__(self):
        return(f"Nom : {self.__nom},"
              f"Taille : {self.__taille},"
              f"Etat d'ouverture : {self.__est_ouverte},",
              f"Dans : {self.__dans.__nom}",
              f"Contient : {self.__contient.__nom}")



def main():
    poupee1 = PoupeeRusse("Sophia", 10)
    poupee2 = PoupeeRusse("Jade", 20)

    poupee1.ouvrir()
    poupee1.placer_dans(poupee2)
    print(poupee1)

if __name__ == '__main__':
    main()






