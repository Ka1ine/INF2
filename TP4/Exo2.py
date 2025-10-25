class Etudiant:
    def __init__(self,nom,a,gpa,connais_python):
        self._nom=nom
        self._annee_naissance = a
        self._gpa = gpa
        self._connais_python = connais_python
    @property
    def nom(self):
        return self._nom
    @property
    def annee_naissance(self):
        return self._annee_naissance
    @property
    def gpa(self):
        return self._gpa
    @property
    def connais_python(self):
        return self._connais_python
    @nom.setter
    def nom(self,nom):
        if isinstance(nom,str):
            self._nom = nom
    @nom.getter
    def nom(self):
        return self._nom
    @annee_naissance.setter
    def annee_naissance(self,a):
        if isinstance(a,int):
            self._annee_naissance = a
    @annee_naissance.getter
    def annee_naissance(self):
        return self._annee_naissance
    @gpa.setter
    def gpa(self,gpa):
        if isinstance(gpa,float):
            self._gpa = gpa
    @gpa.getter
    def gpa(self):
        return self._gpa
    @connais_python.setter
    def connais_python(self,connais_python):
        if isinstance(connais_python, bool):
            self._connais_python = connais_python
    @connais_python.getter
    def connais_python(self):
        return self._connais_python
    def to_dict(self):
        etudico={}
        etudico["nom"]=self.nom
        etudico["annee_naissance"]=self.annee_naissance
        etudico["gpa"]=self.gpa
        etudico["connais_python"]=self.connais_python
        return etudico
class Groupe:
    def __init__(self):
        self._etudiants=[]
    def ajouter_etudiant(self,etudiant):
        if isinstance(etudiant,Etudiant):
            self._etudiants.append(etudiant)
