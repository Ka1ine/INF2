def nb_min(mdp):
    minuscules=0
    for i in mdp: #On parcours le mot de passe
        if "a" <= i <= "z": #si la lettre est minuscule on augmente le compteur min
            minuscules+=1
    return minuscules

def nb_maj(mdp):
    majuscules = 0
    for i in mdp:      #On parcours le mot de passe
        if i.isupper():       #Si la lettre est majuscule on augmente le compteur
            majuscules += 1
    return majuscules

def nb_non_alpha(mdp):
    return len(mdp)- nb_min(mdp)- nb_maj(mdp) #On enleve les caracteres alphabetiques de la longeur du mot de passe

def long_min(mdp):
    liste = [] #On cree une liste pour ajouter les differentes longeurs des chaines de minuscules
    n = 0
    for i in mdp:
        if i.islower(): #si le caractère est une lettre minuscule on augmente le compteur
            n += 1
        else:
            liste.append(n) #si le caractère n'est pas une lettre minuscule on garde le dernier comteur dans la liste et on réinitialise le compteur
            n = 0
    liste.append(n)
    return max(liste)

def long_maj(mdp):
    liste = [] #On cree une liste pour mettre les differentes longeurs des chaines de minuscules dans le mot de passe
    n = 0
    for i in mdp:
        if i.isupper(): #si le caractère est une lettre majuscule on augmente le compteur
            n += 1
        else: # si le caractère n'est pas une lettre majuscule on garde le compteur dans la liste et on reinitialise le compteur.
            liste.append(n)
            n = 0
    liste.append(n)
    return max(liste)

def score(mdp):
    s_len = len(mdp) * 4
    s_up = (len(mdp) - nb_maj(mdp)) * 2
    s_low = (len(mdp) - nb_min(mdp)) * 3
    s_sym = nb_non_alpha(mdp) * 5 #
    p_low = long_min(mdp) * 2
    p_up = long_maj(mdp) * 3 #On cree les variables qui créent une ponctuation pour les influenceurs du score du mot de passe

    total = s_len + s_up + s_low + s_sym - p_low - p_up #on somme le résultat du mot de passe
    return total

def main():
    mot_de_passe = str(input("Donnez un mot de passe : "))
    if 40 <= score(mot_de_passe) < 80:
        print("Fort")
    elif 20 <= score(mot_de_passe) < 40:
        print("faible")
    elif score(mot_de_passe) < 20:
        print("Très faible")
    else:
        print("Très fort")

if __name__ == "__main__":
    main()

