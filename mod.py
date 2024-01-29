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


def lettre_dans_mot(lettre, liste_mot, mot_cache, mot):
    indices = [i for i in range(len(liste_mot)) if lettre in liste_mot[i]]
    for i in range(len(indices)):
        mot_cache[indices[i]] = mot[indices[i]]
    return mot_cache


def last_chance(liste_mot, mot_cache, mot):
    lettres = []
    for i in range(len(liste_mot)):
        if liste_mot[i] != mot_cache[i]:
            lettres.append(mot[i])
    print(random.choice(lettres))
