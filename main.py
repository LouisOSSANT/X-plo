
liste = []


def listing_de_fichiers(rep):
    """convertir les fichiers jpg odt et docx en txt"""

    liste1 = []
    liste2 = []
    liste3 = []


    from pathlib import Path


    p = Path(rep)

    for f in list(p.glob('**/*.txt')):

        liste1 += [f]

    for f in list(p.glob('**/*.odt')):
        liste2 += [f]

    for f in list(p.glob('**/*.docx')):
        liste3 += [f]

    liste = liste1 + liste2 + liste3

    return (liste)


def prend_doc_dans_liste(liste):


    import os.path
    liste = listing_de_fichiers(rep)
    doc_etud = os.path.basename(liste[n])
    return doc_etud
    



def cherche_mot(doc):
    
    doc = document_analyse
    fichier = open(doc, "rt", encoding="utf8")
    for lignes in fichier:
        trouver = False
        if mot in lignes:
            trouver = True
            return trouver
        else:
            trouver = False
            return trouver
    fichier.close()


def determine_nbr_de_fichier(liste):

    liste = listing_de_fichiers(rep)
    nb_fichiers = len(liste) - 1
    return nb_fichiers







#     MAIN     #


n = 0

rep = input("quelle est votre répertoire à examiner? : ")
"""
print(determine_nbr_de_fichier(liste))
print(listing_de_fichiers(rep))
"""

repertoire = listing_de_fichiers(rep)
nb_fichiers = determine_nbr_de_fichier(liste)
mot = input("quelle mot chercher vous ? :")

document_analyse = prend_doc_dans_liste(liste)
print(document_analyse)
trouve = cherche_mot(document_analyse)
print(trouve)
"""
while n < nb_fichiers :

    document = prend_doc_dans_liste(liste)
    trouve = cherche_mot(document)

    if trouve:  # c'est moche moi je n'aurais pas utilise de variable globale
        print(document)

    n = n + 1
"""