"""
Créer une classe Produit qui possède les attributs suivants :
- nom
- prixHT
- TVA
"""
class Produit():
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CaclulerPrixTTC(self):
        return self.prixHT + self.TVA

    def afficherNom(self):
        print("le nom est: ", self.nom)

    def afficherPrixHT(self):
        print("le prix HT est: ", self.prixHT)

    def afficherPrixTTC(self):
        print("le prix TTC est: ", self.CaclulerPrixTTC())

    def changerNom(self, nom):
        self.nom = nom

    def changerPrixHT(self, prixHT):
        self.prixHT = prixHT

    def afficher(self):
        print("le nom est: ", self.nom)
        print("le prix HT est: ", self.prixHT)
        print("le prix TTC est: ", self.CaclulerPrixTTC())

object1 = Produit("Banane", 1.40, 0.20)
object1.afficherNom()
object1.afficherPrixHT()
print(object1.CaclulerPrixTTC())
object1.afficherPrixTTC()
object1.changerNom("Pomme")
object1.changerPrixHT(1.10)
object1.afficher()





