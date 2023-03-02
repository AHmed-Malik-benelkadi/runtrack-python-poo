class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def information_vehicule(self,modele):
        print("marque: ", self.marque)
        print("annee: ", self.annee)
        print("prix: ", self.prix)
        print("modele: ", modele)
    def demarrer(self):
        print("[Attention] Je roule !")

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix,portes=4):
        super().__init__(marque, annee, prix)
        self.portes = portes

    def information_vehicule(self,modele):
        super().information_vehicule(modele)
        print("marque: ", self.marque)
        print("annee: ", self.annee)
        print("prix: ", self.prix)
        print("modele: ", modele)
        print("portes: ", self.portes)

    def demarrer(self):
        print("[Attention] Je roule !")
        print("Je suis une voiture")
class Moto(Vehicule):
    def __init__(self, marque, annee, prix, roues=2):
        super().__init__(marque, annee, prix)
        self.roues = roues

    def information_vehicule(self,modele):
        super().information_vehicule(modele)
        print("marque: ", self.marque)
        print("annee: ", self.annee)
        print("prix: ", self.prix)
        print("modele: ", modele)
        print("roues: ", self.roues)

    def demarrer(self):
        print("[Attention] Je roule !")
        print("Je suis une moto")



voiture1 = Vehicule("Marcedes", 2020, 18500)
voiture1.information_vehicule("C200")
voiture1.demarrer()

vehicule1 = Voiture("Marcedes", 2020, 18500)
vehicule1.information_vehicule("Class A")
vehicule1.demarrer()

motocyclette1 = Moto("Yamaha", 1987, 4500)
motocyclette1.information_vehicule("1200 Vmax")
motocyclette1.demarrer()