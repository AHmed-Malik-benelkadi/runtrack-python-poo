class Forme:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return 0

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def aire(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        super().__init__(longueur, largeur)

    def aire(self):
        return self.__longueur * self.__largeur


aire = Rectangle(10,12)
print("l'air du rectangle est de : ",aire.aire())

cercle1 = Cercle(5)
print("l'air du cercle est de : ",cercle1.aire())