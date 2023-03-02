"""Créer une classe “Ville” avec comme attributs privés un nom et un nombre d'habitants.
Créer une classe “Personne” avec les attributs privés suivants : nom, age et un objet de
la classe ville.
Ajouter la méthode “ajouterPopulation” dans la classe “Personne” qui permet
d’augmenter de 1 le nombre d’habitants de la ville.
Créer un objet “Ville” avec comme arguments “Paris” et 1000000.
Afficher en console le nombre d’habitants de la ville de Paris.
Créer un autre objet “Ville” avec comme arguments “Marseille” et 861635.
Afficher en console le nombre d’habitants de la ville de Marseille.
Créer les objets suivants :
- John, 45 ans, habitant à Paris
- Myrtille, 4 ans, habitant à Paris.
- Chloé, 18 ans, habitant à Marseille.
Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces nouvelles
personnes."""

class Ville():
    def __init__(self, nom, nombreHabitants):
        self.__nom = nom
        self.__nombreHabitants = nombreHabitants
    def get_nom(self):
        return self.__nom
    def get_nombreHabitants(self):
        return self.__nombreHabitants
    def set_nom(self, nom):
        self.__nom = nom
    def set_nombreHabitants(self, nombreHabitants):
        self.__nombreHabitants = nombreHabitants
    def __str__(self):
        return "nom: "+self.__nom+"    nombreHabitants: "+str(self.__nombreHabitants)

class Personne():
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
    def get_nom(self):
        return self.__nom
    def get_age(self):
        return self.__age
    def get_ville(self):
        return self.__ville
    def set_nom(self, nom):
        self.__nom = nom
    def set_age(self, age):
        self.__age = age
    def set_ville(self, ville):
        self.__ville = ville
    def ajouterPopulation(self):
        self.__ville.set_nombreHabitants(self.__ville.get_nombreHabitants()+1)
    def __str__(self):
        return "nom: "+self.__nom+"    age: "+str(self.__age)+"    ville: "+str(self.__ville)

ville1 = Ville("Paris", 1000000)
print(ville1)
ville2 = Ville("Marseille", 861635)
print(ville2)

personne1 = Personne("John", 45, ville1)
personne1.ajouterPopulation()
print(personne1)
personne2 = Personne("Myrtille", 4, ville1)
personne2.ajouterPopulation()
print(personne2)
personne3 = Personne("Chloé", 18, ville2)
personne3.ajouterPopulation()
print(personne3)




