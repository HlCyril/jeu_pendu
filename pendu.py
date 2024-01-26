import mod
import string

alphabet = list(string.ascii_lowercase)

mon_fichier = 'mots_pendu.txt'
print("\nJeu du pendu")
print("Règle du jeu :")
print("1) Vous commencez avec 6 vies")
print("2) Ne pas écrire de lettre avec des accents")
print("3) Écrire les lettres en minuscule\n")
print("\nLa liste des mots est dans le fichier :", mon_fichier)

# Lecture des mots dans le fichier texte, et pour les mettre dans une liste
liste_des_mots = mod.lire_fichier(mon_fichier)
# Choix du mot dans la liste de mot précédente
mot = mod.choisir_mot(liste_des_mots)
# On a maintenant le mot sous forme de liste pour faciliter la manipulation
liste_mot = list(mot)
# On enlève les accents
liste_mot = mod.enlever_accents(liste_mot)
# On crée le mot caché
mot_cache = ['_'] * len(liste_mot)

print(mot)
print('Le mot choisi contient ', len(liste_mot), 'lettres')
lettres_utilise = []
nombre_de_vie = 6
while nombre_de_vie > 0 and mot_cache != liste_mot:

    lettre = input("\nDonnez une lettre : \n")

    if lettre in lettres_utilise:
        print('Lettre déjà utilisée\n')

    elif lettre in liste_mot:
        print('Bien joué')
        lettres_utilise.append(lettre)
        # Si la lettre apparaît plusieurs fois dans le mot
        mot_cache = mod.lettre_dans_mot(lettre, liste_mot, mot_cache)

    elif lettre in alphabet and lettre not in liste_mot:
        print('Faux')
        nombre_de_vie -= 1
        lettres_utilise.append(lettre)

    else:
        print("L'entrée ne respecte pas les conditions des règles")

    print('\nLe nombre de vie restant est de : ', nombre_de_vie)
    print('Liste des lettres utilisées :\n', ' '.join(lettres_utilise))
    print('Progression : ', ''.join(mot_cache))

print('\n')
if nombre_de_vie != 0:
    print('Bien joué tu as gagné !')
else:
    print('Tu as perdu')
    print('Le mot était : ', mot)
