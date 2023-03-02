class Rectangle ():
    def __init__(self,longueur,largeur):
        self.__longueur=longueur
        self.__largeur=largeur
    def set_longueur(self,longueur):
        self.__longueur=longueur
    def set_largeur(self,largeur):
        self.__largeur=largeur

    def get_longueur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur

    def __str__(self):
        return "longueur: "+str(self.__longueur)+" largeur: "+str(self.__largeur)

rec1=Rectangle(10, 5) # longueur=10, largeur=5
print(rec1)
rec1.set_longueur(30)
rec1.set_largeur(25)
print(rec1)

