import mod
import string

# On récupère l'alphabet dans une liste
alphabet = list(string.ascii_lowercase)

mon_fichier = 'mots_pendu.txt'

# On définit le nombre de vies
nombre_de_vie = 6

# On définit la valeur du joker
joker = 1

print("\nJeu du pendu")
print("Règles du jeu :")
print("1) Tu commences avec ", nombre_de_vie, " vies")
print("2) Ne pas écrire de lettre avec des accents")
print("3) Écrire les lettres en minuscule")
print("4) Tu possèdes ", joker, " joker qui s'utilise automatiquement lorsqu'il te reste une vie")
print("La liste des mots est dans le fichier :", mon_fichier)

# Lecture des mots dans le fichier texte, et pour les mettre dans une liste
liste_des_mots = mod.lire_fichier(mon_fichier)
# Choix du mot dans la liste de mot précédente
mot = mod.choisir_mot(liste_des_mots)
# On met le mot sous forme de liste pour faciliter l'utilisation
liste_mot = list(mot)
# On enlève les accents
liste_mot = mod.enlever_accents(liste_mot)
# On crée le mot caché
mot_cache = ['_'] * len(liste_mot)

# print(mot)

print('Le mot choisi contient ', len(liste_mot), 'lettres')

lettres_utilise = []

while nombre_de_vie > 0 and ''.join(mot_cache) != mot:

    lettre = input("\nDonnez une lettre :")

    if lettre in lettres_utilise:
        print('Lettre déjà utilisée')

    elif lettre in liste_mot:
        print('Bien joué')
        lettres_utilise.append(lettre)
        # Si la lettre apparaît plusieurs fois dans le mot
        mot_cache = mod.lettre_dans_mot(lettre, liste_mot, mot_cache, mot)

    elif lettre in alphabet and lettre not in liste_mot:
        print('Faux')
        nombre_de_vie -= 1
        lettres_utilise.append(lettre)

    else:
        print("L'entrée ne respecte pas les conditions des règles")

    print('Le nombre de vie restant est de : ', nombre_de_vie)
    print('Liste des lettres utilisées :\n', ' '.join(lettres_utilise))
    print('Progression : ', ''.join(mot_cache))

    if nombre_de_vie == 1 and joker == 1:
        print("Il ne te reste plus qu'une vie, voici un indice : ")
        mod.last_chance(liste_mot, mot_cache, mot)
        joker -= 1

if nombre_de_vie != 0:
    print('Bien joué tu as gagné !')
else:
    print('Tu as perdu')
    print('Le mot était : ', mot)
