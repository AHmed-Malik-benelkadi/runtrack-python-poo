class Rectangle:
    def __init__(self,Longeur,Largeur):
        self.__Longeur = Longeur
        self.__Largeur = Largeur

    def perimetre(self):
        return 2*(self.__Longeur+self.__Largeur)
    def surface(self):
        return self.__Longeur*self.__Largeur

    def get_longeur(self):
        return self.__Longeur
    def set_longeur(self,Longeur):
        self.__Longeur = Longeur

    def get_largeur(self):
        return self.__Largeur

    def set_largeur(self,Largeur):
        self.__Largeur = Largeur

class Parallelepipede(Rectangle):
    def __init__(self,Longeur,Largeur,Hauteur):
        Rectangle.__init__(self,Longeur,Largeur)
        self.__Hauteur = Hauteur

    def volume(self):
        return self.__Hauteur*self.surface()

    def get_hauteur(self):
        return self.__Hauteur
    def set_hauteur(self,Hauteur):
        self.__Hauteur = Hauteur



rectangle1 = Rectangle(5,6)
print("le perimetre du rectangle est : ",rectangle1.perimetre())
print("la surface du rectangle est : ",rectangle1.surface())

parallelepipede1 = Parallelepipede(1,3,4)
print("le volume du parallelepipede est : ",parallelepipede1.volume())
print("le perimetre du parallelepipede est : ",parallelepipede1.perimetre())
print("la surface du parallelepipede est : ",parallelepipede1.surface())





