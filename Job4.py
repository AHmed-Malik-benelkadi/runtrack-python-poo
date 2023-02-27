class Personne():
    def __init__(self, name,nom):
        self.name = name
        self.nom = nom

    def sepresenter(self):
        return "Je suis  " +self.name+ " "+ self.nom



object1 = input("Quel est votre nom ? : ")
object2 = input("Quel est votre prenom ? : ")
object4 = Personne(object1,object2)
print(object4.sepresenter())