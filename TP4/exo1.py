import math
import os
def extraire_pi():
    with open('poeme.txt') as f:
        contenu = f.read()
        texte_nettoye = contenu.replace(",", " ").replace(".", " ").replace("'", " ") \
            .replace("?", " ").replace("!", " ").replace("\n", " ")
        #Nettoyage des élements de ponctuation
        mots = texte_nettoye.split(" ")
        #sauvegarde des mots sans ponctuation dans des chaines de caractères individuelles
        mots_propres=[]
        for m in mots:
            if m != "":
                mots_propres.append(m)
        #Nettoyage des mots vides qui peuvent alterer le programme
        pi = float(0)
        i = 0
        for m in mots_propres:
            pi += float(len(m)%10) * (10.0 ** float(i))
            i -= 1
        #Écriture de pi en utilisant les puissances de 10
    return (pi)
def creer_fichier_pi():
    with open('pi.txt','x'):
        pass
#création du fichier qui va contenir pi


def ecrire_pi():
    with open("pi.txt",'w') as f:
        f.write(str(extraire_pi()))
#écriture de pi dans le fichier crée


def main():
    print(os.getcwd())
    print(f"Valeur calculé : {extraire_pi()}")
    print(f"Valeur importé : {math.pi}")
    print(extraire_pi()==math.pi)
    creer_fichier_pi()
    ecrire_pi()


if __name__ == '__main__':
    main()
