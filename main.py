import os
liste = []


from pathlib import Path

def repertoire(rep):
    """convertir les fichiers jpg odt et docx en txt"""
    import os
    liste1 = []
    liste2 = []
    liste3 = []
    liste4 = []

    p = Path(rep)

    for f in list(p.glob('**/*.txt')):
        #definir f pour qu'il n'y ai plus le chemin mais que le fichier texte 
        liste1 += [f]

    for f in list(p.glob('**/*.jpg')):
        liste2 += [f]

    for f in list(p.glob('**/*.odt')):
        liste3 += [f]

    for f in list(p.glob('**/*.docx')):
        liste4 += [f]

    liste = liste1 + liste2 + liste3 + liste4

    return liste


def X():
    liste = repertoire(rep)
    X = len(liste)-1
    return X

def doc_etud(n):
    """enlever le chemin pr n'avoir que le nom du fichier"""
    liste = repertoire(rep)
    doc_etud = liste[n]
    return doc_etud

def cherche_mot(doc):
    doc = doc_etud(n)
    fichier = open(doc,"rt",encoding = "utf8")
    for lignes in fichier:
        trouver = False
        if mot in lignes:
            trouver = True
            return trouver
        else:
            trouver = False
            return trouver
    fichier.close()




#main


n = 0
rep = 'C:/Users/mot Louis programmation/X-plo/maket/'



mot = input("quelle mot chercher vous ? :")
repertoire = repertoire(rep)
X = X()
while n < X-1:
    doc_etud = doc_etud(n)
    chercher_mot(doc_etud)
    if cherche_mot = True:
        print(doc_etud)
        print(phrase_du_mot())
        n = n + 1
    else:
        n = n + 1



