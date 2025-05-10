# utils.py

import csv
import json

def lire_csv(chemin):
    """
    Lire un fichier CSV et retourner la liste des lignes.
    Chaque dictionnaire correspond à une ligne du fichier.
    """
    with open(str(chemin), "r", encoding="utf-8") as f :
        fichier = csv.reader(f)
        for ligne in fichier:
            print (ligne)

def sauvegarder_json(data, chemin):
    """
    Sauvegarder des données dans un fichier JSON.
    - data : un objet Python (par exemple, un dictionnaire ou une liste)
    - chemin : chemin du fichier JSON à écrire
    Utiliser json.dump avec indentation pour que le fichier soit lisible.
    """
<<<<<<< HEAD
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(data,f, indent=4, ensure_ascii=False)

def ecrire_texte(contenu, chemin):
    """
    Écrire du texte brut dans un fichier texte (.txt).
    - contenu : texte à écrire
    - chemin : chemin du fichier texte à créer
    """
    with open(chemin, "w") as f:
        f.write(contenu)

lire_csv("./data/joueurs.csv")