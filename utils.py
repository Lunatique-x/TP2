# utils.py

import csv
import json

def lire_csv(chemin):
    """
    Lire un fichier CSV et retourner la liste des lignes.
    Chaque dictionnaire correspond à une ligne du fichier.
    """
    # Ouvre le fichier CSV en mode lecture
    with open(str(chemin), "r", encoding="utf-8") as f :
        fichier = csv.reader(f)
        # Crée une liste vide pour stocker le contenu du fichier
        contenue_par_ligne = []
        for ligne in fichier:
            # Ajoute chaque ligne à la liste
            contenue_par_ligne.append(ligne)
        # Retourne la liste contenant toutes les lignes du fichier
        return contenue_par_ligne

def sauvegarder_json(data, chemin):
    """
    Sauvegarder des données dans un fichier JSON.
    - data : un objet Python (par exemple, un dictionnaire ou une liste)
    - chemin : chemin du fichier JSON à écrire
    Utiliser json.dump avec indentation pour que le fichier soit lisible.
    """
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def ecrire_texte(contenu, chemin):
    """
    Écrire du texte brut dans un fichier texte (.txt).
    - contenu : texte à écrire
    - chemin : chemin du fichier texte à créer
    """
    with open(chemin, "w") as f:
        f.write(contenu)
