import random


def lire_fichier(fichier_txt):
    with open(fichier_txt, 'r', encoding='utf-8') as fichier:
        lignes = fichier.readlines()
        liste_mots = [mot.strip() for mot in lignes]
    return liste_mots


def choisir_mot(liste_mots):
    return random.choice(liste_mots)


def enlever_accents(mot):
    a = ['à', 'ä', 'â']
    e = ['é', 'è', 'ë', 'ê']
    i = ['î', 'ï']
    o = ['ô', 'ö']
    u = ['ù', 'û', 'ü']
    for k in range(len(mot)):
        if mot[k] in a:
            mot[k] = 'a'
        if mot[k] in e:
            mot[k] = 'e'
        if mot[k] in i:
            mot[k] = 'i'
        if mot[k] in o:
            mot[k] = 'o'
        if mot[k] in u:
            mot[k] = 'u'
    return mot
