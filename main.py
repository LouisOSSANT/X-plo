

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


#main
rep = 'C:/Users/Louis programmation/X-plo/maket/'

print(X())
print(repertoire(rep))