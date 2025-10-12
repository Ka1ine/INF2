class PoupeeRusse:
    def __init__(self, nom , taille):
        """Responsable de l’initialisation de la poupée avec un nom et une taille positifs."""
        self.__nom = nom
        self.__taille = taille
        self.__est_ouverte = False
        self.__dans = None
        self.__contient = None

    # Getters
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

    # Setters
    @est_ouverte.setter
    def est_ouverte(self, est_ouverte):
        if isinstance(est_ouverte, bool):
            self.__est_ouverte = est_ouverte
        else:
            raise TypeError('Il doit être de type booléen')

    @dans.setter
    def dans(self, dans_autre):
        if dans_autre is not None and not isinstance(dans_autre, PoupeeRusse):
            raise TypeError("dans doit être une autre poupée ou None")
        if dans_autre is self:
            raise ValueError("Une poupée ne peut pas être dans elle-même")
        self.__dans = dans_autre

    @contient.setter
    def contient(self, contient):
        if contient is not None and not isinstance(contient, PoupeeRusse):
            raise TypeError("contient doit être une autre poupée ou None")
        if contient is self:
            raise ValueError("Une poupée ne peut pas se contenir elle-même")
        self.__contient = contient

    # Fonctions
    def ouvrir(self):
        """Ouvre la poupée si elle n’est pas déjà ouverte et n’est pas dans une autre."""
        if not self.__est_ouverte and self.__dans is None:
            self.__est_ouverte = True

    def fermer(self):
        """Ferme la poupée si elle n’est pas déjà fermée et n’est pas dans une autre."""
        if self.__est_ouverte and self.__dans is None:
            self.__est_ouverte = False

    def placer_dans(self, p):
        """Place la poupée courante dans p si les conditions sont respectées."""
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
        """Sort la poupée courante d’une autre si la contenante est ouverte."""
        if self.__dans is not None and self.__dans.est_ouverte:
            self.__dans.__contient = None
            self.__dans = None

    def __str__(self):
        """Retourne les caractéristiques de la poupée."""
        etat = "ouverte" if self.__est_ouverte else "fermée"
        dans = self.__dans.__nom if self.__dans is not None else "aucune"
        contient = self.__contient.__nom if self.__contient is not None else "aucune"

        return (
            f"Nom : {self.__nom} - "
            f"Taille : {self.__taille} - "
            f"État : {etat} - "
            f"Dans : {dans} - "
            f"Contient : {contient}"
        )

def main():
    poupee1 = PoupeeRusse("Sophia", 10)
    poupee2 = PoupeeRusse("Jade", 20)

    print("--- Tests des méthodes ---")
    poupee2.ouvrir()
    poupee1.placer_dans(poupee2)
    print("Après placement :")
    print(poupee1)
    print(poupee2)

    print("\n--- Test de sortie ---")
    poupee2.ouvrir()
    poupee1.sortir_de()
    print("Après sortie :")
    print(poupee1)
    print(poupee2)

    print("\n--- Vérification de l’état ---")
    print(f"La poupée {poupee1.nom} est {'ouverte' if poupee1.est_ouverte else 'fermée'}")
    print(f"La poupée {poupee2.nom} est {'ouverte' if poupee2.est_ouverte else 'fermée'}")

    print("\n--- Affichage des caractéristiques ---")
    print(poupee1)
    print(poupee2)

if __name__ == '__main__':
    main()