class Rectangle:
    def __init__(self, longueur, largeur):
        """Initialise un rectangle avec longueur et largeur positives."""
        self.set_longueur(longueur)
        self.set_largeur(largeur)

    # Getters
    def get_largeur(self):
        return self._largeur

    def get_longueur(self):
        return self._longueur

    # Setters
    def set_largeur(self, l):
        if not isinstance(l, float):
            raise TypeError("La largeur doit être de type float")
        if l <= 0:
            raise ValueError("La largeur doit être un réel positif")
        self._largeur = l

    def set_longueur(self, l):
        if not isinstance(l, float):
            raise TypeError("La longueur doit être de type float")
        if l <= 0:
            raise ValueError("La longueur doit être un réel positif")
        self._longueur = l

    def perimetre(self):
        """Retourne le périmètre du rectangle."""
        return (self.get_longueur() + self.get_largeur()) * 2

    def aire(self):
        """Retourne l'aire du rectangle."""
        return self.get_longueur() * self.get_largeur()

    def est_carre(self):
        """Vérifie si le rectangle est un carré."""
        return self.get_longueur() == self.get_largeur()

    def le_plus_grand(self, other):
        """Compare l’aire de deux rectangles et retourne le plus grand."""
        if not isinstance(other, Rectangle):
            raise TypeError("Le paramètre doit être de type Rectangle")
        return self if self.aire() >= other.aire() else other

    def afficher(self):
        """Affiche les caractéristiques du rectangle."""
        est_carre_txt = "C’est un carré" if self.est_carre() else "Ce n’est pas un carré"
        print(
            f"Longueur : {self.get_longueur()} - "
            f"Largeur : {self.get_largeur()} - "
            f"Périmètre : {self.perimetre()} - "
            f"Aire : {self.aire()} - "
            f"{est_carre_txt}"
        )

def main():
    rectangle = Rectangle(15.0, 12.0)
    carre = Rectangle(10.0, 10.0)

    print("--- Tests des méthodes ---")
    print(f"Périmètre du rectangle : {rectangle.perimetre()}")
    print(f"Périmètre du carré : {carre.perimetre()}")
    print(f"Aire du rectangle : {rectangle.aire()}")
    print(f"Aire du carré : {carre.aire()}")

    print("\n--- Vérification de la forme ---")
    print(f"Le rectangle est {'un carré' if rectangle.est_carre() else 'un rectangle'}")
    print(f"Le carré est {'un carré' if carre.est_carre() else 'un rectangle'}")

    print("\n--- Comparaison des aires ---")
    plus_grand = rectangle.le_plus_grand(carre)
    print(f"Le plus grand des deux a une aire de : {plus_grand.aire()}")

    print("\n--- Affichage des caractéristiques ---")
    rectangle.afficher()
    carre.afficher()

if __name__ == '__main__':
    main()
