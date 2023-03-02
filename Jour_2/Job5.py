class Voiture():
    def __init__(self, marque,modele,annee,kilometrage,en_Marche=False,reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__enMarche = en_Marche
        self.__reservoir = reservoir
    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_annee(self):
        return self.__annee
    def get_kilometrage(self):
        return self.__kilometrage
    def get_enMarche(self):
        return self.__enMarche

    def set_marque(self, marque):
        self.__marque = marque
    def set_modele(self, modele):
        self.__modele = modele
    def set_annee(self, annee):
        self.__annee = annee
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
    def set_enMarche(self, en_Marche):
        self.__enMarche = en_Marche


    def __verifier_plein(self):
        if self.__reservoir > 5:
            print("la voiture peut demarrer")
        else:
            print("la voiture ne peut pas demarrer")

    def demarrer(self):
        self.__enMarche = True
        print("La voiture est démarrée")
    def arreter(self):
        self.__enMarche = False
        print("La voiture est arrêtée")




    def __str__(self):
        return "marque: "+self.__marque+"    modele: "+self.__modele+"    annee: "+str(self.__annee)+"    kilometrage: "+str(self.__kilometrage)+"    enMarche: "+str(self.__enMarche)

voiture1 = Voiture("BMW", "X5", 2015, 10000)
print(voiture1)


verifier_plein = voiture1._Voiture__verifier_plein()
print(verifier_plein)


