import os
liste = []


from pathlib import Path

p = Path('F:\X-plo\maket')

for f in list(p.glob('**/*.txt')):
    liste1 = [f]

for f in list(p.glob('**/*.jpg')):

    os.environ['CLASSPATH'] = "/path/to/tika-app.jar"

    from jnius import autoclass


    Tika = autoclass('org.apache.tika.Tika')
    Metadata = autoclass('org.apache.tika.metadata.Metadata')
    FileInputStream = autoclass('java.io.FileInputStream')

    tika = Tika()
    meta = Metadata()
    text = tika.parseToString(FileInputStream(f), meta)
    liste2 = [text]

for f in list(p.glob('**/*.odt')):


    os.environ['CLASSPATH'] = "/path/to/tika-app.jar"

    from jnius import autoclass

    Tika = autoclass('org.apache.tika.Tika')
    Metadata = autoclass('org.apache.tika.metadata.Metadata')
    FileInputStream = autoclass('java.io.FileInputStream')

    tika = Tika()
    meta = Metadata()
    text = tika.parseToString(FileInputStream(f), meta)
    liste3 = [text]

for f in list(p.glob('**/*.docx')):


    os.environ['CLASSPATH'] = "/path/to/tika-app.jar"

    from jnius import autoclass

    Tika = autoclass('org.apache.tika.Tika')
    Metadata = autoclass('org.apache.tika.metadata.Metadata')
    FileInputStream = autoclass('java.io.FileInputStream')

    tika = Tika()
    meta = Metadata()
    text = tika.parseToString(FileInputStream(f), meta)
    liste4 = [text]

liste = liste1 + liste2 + liste3 + liste4
print (liste)


