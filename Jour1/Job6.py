class Animal(): # Création de la classe Animal
    def __init__(self,age):  # Création de la méthode init
        self.age = age   # Création de l'attribut age
        print("l'age de l'animal : ", self.age) # Affichage de l'age de l'animal

    def viellir(self): # Création de la méthode viellir
        self.age += 1  # Incrémentation de l'age de l'animal
        print("l'age de l'animal 1ans aprés est de : ", self.age)  # Affichage de l'age de l'animal

    def nommer(self, nom): # Création de la méthode nommer
        self.nom = nom  # Création de l'attribut nom
        print("le nom de l'animal est: ", self.nom)  # Affichage du nom de l'animal


object1 = Animal(10)
object1.viellir()
object1.nommer("Luna")
