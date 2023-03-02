class Personne:
    def __init__(self,age=14):
        self.__age = age

    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
    def afficherAge(self):
        print("age: ", self.__age)

    def bonjour(self):
        print("Hello")
    def modifier_age(self, age):
        self.__age = age
        print("age: ", self.__age)

class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)

    def allerEnCour(self):
        print("Je vais en cour")
    def afficherAge(self):
        print("j'ai"," ","ans", self.get_age())

class Professeur(Personne):
    def __init__(self,matiere):
        Personne.__init__(self)
        self.__matiere = matiere

    def enseigner(self):
        print("le cours va commencer")



eleve1 = Eleve()
eleve1.afficherAge()





