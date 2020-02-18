

def repertoire(rep):
    import os
    liste = []
    liste1 = []
    liste2 = []
    liste3 = []
    liste4 = []

    from pathlib import Path

    p = Path(rep)

    for f in list(p.glob('**/*.txt')):
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
    liste = repertoire(rep)
    doc_etud = liste[n]
    return doc_etud





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