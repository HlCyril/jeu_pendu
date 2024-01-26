import mod

liste_mots = mod.lire_fichier('mots_pendu.txt')
print(liste_mots)

mot = mod.choisir_mot(liste_mots)
print(mot)

liste_mot = list(mot)
print(liste_mot)

liste_mot = mod.enlever_accents(liste_mot)
print(liste_mot)