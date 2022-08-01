import os
import time
import xml.etree.ElementTree as ET
from os import listdir

# Definicion de la funcion de renombre

conteo = 0

def renameFile(file):
    rename = 0
    tree = ET.parse(file)
    root = tree.getroot()
    
    for child in root:
        Rfc = child.get('Rfc')
        rename = rename + 1
        
        if rename == 2:
            print "Renombrando: ", Rfc
            os.rename(file, "./XML/" + Rfc + ".xml")

# Inicio del programa principal

for fileNames in listdir("./XML"):
    renameFile( "./XML/" + fileNames )
    conteo = conteo + 1

print "Se renombraron ", conteo ," archivos."
time.sleep(5)