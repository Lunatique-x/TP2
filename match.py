# match.py

class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score1 = 0
        self.score2 = 0

    def definir_scores(self, score1, score2):
        self.score1 = score1
        self.score2 = score2

    def gagnant(self):
        if self.score1 > self.score2:
            return self.joueur1
        elif self.score2 > self.score1:
            return self.joueur2
        else:
            return None  # égalité
