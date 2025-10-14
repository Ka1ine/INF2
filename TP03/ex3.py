import random

class Pokemon:
    def __init__(self, nom, pv, atk):
        """------------"""
        self.nom = nom
        self.pv = pv
        self.atk = atk

    # Getters
    @property
    def nom(self):
        return self.__nom

    @property
    def pv(self):
        return self.__pv

    @property
    def atk(self):
        return self.__atk

    # Setters
    @nom.setter
    def nom(self, nom):
        if not isinstance(nom, str):
            raise TypeError("Il doit s'agir d'une chaîne")
        self.__nom = nom

    @pv.setter
    def pv(self, pv):
        if not isinstance(pv, int) or pv <= 0:
            raise ValueError("La valeur doit être un entier positif.")
        self.__pv = pv

    @atk.setter
    def atk(self, atk):
        if not isinstance(atk, int) or atk <= 0:
            raise ValueError("La valeur doit être un entier positif.")
        self.__atk = atk

    @property
    def est_ko(self):
        """------------"""
        return self.__pv <= 0

    def attaquer(self, autre):
        """------------"""
        degats = random.randint(0, self.atk)
        nouveaux_pv = autre.pv - (degats*calc_multiplicateur(self,autre))
        autre.pv = nouveaux_pv
    def combattre(self,autre):
        tours = 0
        while not est_ko(self) and not est_ko(autre):
            attaquer(self, autre)
            if not est_ko(autre):
                attaquer(autre,self)
            tours += 1    
        if est_ko(self):
            return(autre, tours)
        elif est_ko(autre):
            return(self,tours)
    def __str__(self):
        if est_ko(self):
            statut = "K.0"
        else:
            statut = f"{self._pv}"
        return f"Nom : {self._nom}, PV : {statut}, atk : {self._atk}, "
            
class PokemonNormal(Pokemon):
    def calc_multiplicateur(self,autre):
        return 1.0
            
class PokemonFeu(Pokemon):
    def calc_multiplicateur(self,autre):
        if isinstance(autre, PokemonPlante):
            return 2.0
        elif isinstance(autre ,(PokemonEau,PokemonFeu))):
            return 0.5
        else:
            return 1.0

class PokemonEau(Pokemon):
    def calc_multiplicateur(self,autre):
        if isinstance(autre, PokemonFeu):
            return 2.0
        elif isinstance(autre, (PokemonPlante , PokemonEau)):
            return 0.5
        else:
            return 1.0
class PokemonPlante(Pokemon):
    def calc_multiplicateur(self, autre):
        if isinstance(autre, PokemonEau):
            return 2.0
        elif isinstance(autre,(PokemonFeu,PokemonPlante)):
            return 0.5
        else:
            return 1.0
def main():
    Pokemon1 = PokemonNormal("Evee",100,20)
    Pokemon2 = PokemonFeu("Incineroar", 300, 80)
    Pokemon3 = PokemonPlante("Snivy" , 150, 30)
    Pokemon4 = PokemonEau("Squirtle", 120, 40)
    print(Pokemon1.combattre(Pokemon2))
    print(Pokemon3.combattre(Pokemon4))
if __name__ == "__main__" :
    main()
    
            
