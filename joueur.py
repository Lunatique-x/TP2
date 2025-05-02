# joueur.py

class Joueur:
    def __init__(self, pseudo):
        self.pseudo = pseudo
        self.victoires = 0

    def enregistrer_victoire(self):
        self.victoires += 1

    def to_dict(self):
        return {
            "pseudo": self.pseudo,
            "victoires": self.victoires
        }

    @staticmethod
    def from_dict(data):
        joueur = Joueur(data["pseudo"])
        joueur.victoires = data.get("victoires", 0)
        return joueur
