class Cercle():

    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, rayon):
        self.rayon = rayon

    def afficherInfos(self):
        print("Le rayon est de: ", self.rayon)

    def circonference(self):
        return 2 * 3.14 * self.rayon

    def aire(self):
        return 3.14 * self.rayon * self.rayon
    def diametre(self):
        return 2 * self.rayon


object1 = Cercle(4)
object1.afficherInfos()
print("la circonférence est de: ", object1.circonference())
print("le diametre est de: ", object1.diametre())
print("l'aire est de: ", object1.aire())

object2 = Cercle(7)
object2.afficherInfos()
print("la circonférence est de: ", object2.circonference())
print("le diametre est de: ", object2.diametre())
print("l'aire est de: ", object2.aire())

