# main.py

from tournoi import Tournoi

def afficher_menu():
    print("\n=== Gestionnaire de Tournoi ===")
    print("1. Créer un nouveau tournoi")
    print("2. Charger les joueurs depuis un fichier CSV")
    print("3. Charger les matchs depuis un fichier CSV")
    print("4. Saisir les scores")
    print("5. Afficher le classement")
    print("6. Sauvegarder le tournoi en JSON")
    print("7. Générer le rapport texte")
    print("0. Quitter")

def main():
    tournoi = None

    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == "1":
            nom = input("Nom du tournoi : ")
            tournoi = Tournoi(nom)
        elif choix == "2":
            if tournoi:
                chemin = input("Chemin du fichier CSV des joueurs : ")
                tournoi.charger_joueurs(chemin)
            else:
                print("Veuillez d'abord créer un tournoi.")
        elif choix == "3":
            if tournoi:
                chemin = input("Chemin du fichier CSV des matchs : ")
                tournoi.charger_matchs(chemin)
            else:
                print("Veuillez d'abord créer un tournoi.")
        elif choix == "4":
            if tournoi:
                tournoi.saisir_scores()
            else:
                print("Veuillez d'abord créer un tournoi.")
        elif choix == "5":
            if tournoi:
                tournoi.afficher_classement()
            else:
                print("Veuillez d'abord créer un tournoi.")
        elif choix == "6":
            if tournoi:
                chemin = input("Chemin du fichier JSON : ")
                tournoi.sauvegarder(chemin)
            else:
                print("Veuillez d'abord créer un tournoi.")
        elif choix == "7":
            if tournoi:
                chemin = input("Chemin du fichier texte : ")
                tournoi.generer_rapport(chemin)
            else:
                print("Veuillez d'abord créer un tournoi.")
        elif choix == "0":
            print("Merci d'avoir utilisé le gestionnaire de tournoi !")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
