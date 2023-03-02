class Forme:
    def __int__(self):
        pass
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self,longeur,largeur):
        self.__longeur = longeur
        self.__largeur = largeur
        Forme.__init__(self)
    def aire(self):
        return self.__longeur*self.__largeur

aire = Rectangle(10,12)
print("l'air du rectangle est de : ",aire.aire())