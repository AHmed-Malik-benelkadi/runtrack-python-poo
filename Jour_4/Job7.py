import random
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"
class Jeu:
    def __init__(self):
        self.paquet = []
        self.carte = Carte
        self.couleur = ["coeur", "carreau", "pique", "trefle"]
        self.valeur = [2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi", "as"]
        for couleur in self.couleur:
            for valeur in self.valeur:
                self.paquet.append(Carte(valeur, couleur))
    def __str__(self):
        return f"{self.paquet}"
    def melanger(self):
        random.shuffle(self.paquet)
    def tirer(self):
        return self.paquet.pop()
    def distribuer(self, joueur):
        joueur.main.append(self.tirer())
        joueur.main.append(self.tirer())
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []
    def __str__(self):
        return f"{self.nom} a comme main {self.main}"
    def total(self):
        total = 0
        for carte in self.main:
            if carte.valeur == "valet" or carte.valeur == "dame" or carte.valeur == "roi":
                total += 10
            elif carte.valeur == "as":
                if total <= 10:
                    total += 11
                else:
                    total += 1
            else:
                total += carte.valeur
        return total
    def tirer(self):
        self.main.append(jeu.tirer())
    def passer(self):
        pass
    def gagner(self):
        print("Vous avez gagné !")


    def perdre(self):
        print("Vous avez perdu !")



jeu = Jeu()
jeu.melanger()
joueur = Joueur("Bob")
jeu.distribuer(joueur)
print(joueur)
print(joueur.total())
joueur.tirer()
print(joueur)
print(joueur.total())
joueur.passer()
print(joueur)
print(joueur.total())
joueur.gagner()
print(joueur)
print(joueur.total())
joueur.perdre()
print(joueur)
print(joueur.total())
