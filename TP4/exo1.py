import math
import os


def extraire_pi():
    with open('poeme.txt') as f:
        contenu = f.read()
        texte_nettoye = contenu.replace(",", "").replace(".", "").replace("'", " ").replace("?", "").replace("!", "").replace("\n","")
        mots = texte_nettoye.split(" ")
        pi = float(0)
        i = 0
        for m in mots:
            pi += float(len(m)) * (10.0 ** float(i))
            i -= 1
    return (pi)

def ecrire_pi():
    with open("chiffre.txt",'x') as f:
        f.write(str(extraire_pi()))


def main():
    print(os.getcwd())
    print(f"Valeur calculé : {extraire_pi()}")
    print(f"Valeur importé : {math.pi}")
    ecrire_pi()


if __name__ == '__main__':
    main()
