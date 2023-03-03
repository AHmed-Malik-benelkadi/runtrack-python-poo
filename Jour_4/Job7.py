"""Développer votre version du célèbre jeu Blackjack. Le but est de faire le plus de points
sans dépasser 21. Chaque carte représente une valeur :
- de 2 à 10 : ces cartes ont pour valeur sa valeur nominale
- une figure a pour valeur 10 points
- un as 1 ou 11 points au choix
Le jeu commence avec les joueurs qui reçoivent chacun 2 cartes. Ensuite, le joueur peut
choisir de "prendre" (recevoir) une ou plusieurs cartes supplémentaires pour tenter
d'améliorer sa main, ou de "passer" et laisser le tour au croupier. Le croupier prend des
cartes jusqu'à ce qu'il ait au moins 17 points, puis s'arrête. Si la main du joueur dépasse
21, il perd immédiatement. Si le total de la main du joueur est supérieur à celui du
croupier, le joueur gagne. Sinon, c'est le croupier qui gagne.
Créer au minimum deux classes Carte et Jeu.
La classe Carte aura au minimum un attribut valeur et couleur. La classe Jeu quant à
elle devra gérer l’ensemble des cartes. Les cartes du jeu seront stockées dans un
attribut paquet représenté par une liste et contenant 52 cartes.
Créer toutes les méthodes nécessaires pour jouer une partie."""
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
