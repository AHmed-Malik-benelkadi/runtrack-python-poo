class CompteBancaire:

    def __init__(self, numeroDe_compte, nom,prenom, solde,decouvert=False):
        self.__numeroDe_compte = numeroDe_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print("numero de compte: ", self.__numeroDe_compte)
        print("nom: ", self.__nom)
        print("prenom: ", self.__prenom)
        print("solde: ", self.__solde)
    def afficherSolde(self):
        print("solde: ", self.__solde)

    def versement(self, montant):
        self.__solde += montant
        print("solde: ", self.__solde)
    def retrait(self, montant):
            if self.__solde >= montant:
                self.__solde -= montant
                print("solde: ", self.__solde)
            else:
                print("solde insuffisant")
    def agios(self):
            if self.__solde < 0:
                self.__solde -= 20
                print("solde: ", self.__solde)
            else:
                print("solde: ", self.__solde)

    def virement(self, reference, compte,montant):

            if self.__solde >= montant:
                self.__solde -= montant
                compte.__solde += montant
                print("solde: ", self.__solde)
                print("solde: ", compte.__solde)
            else:
                print("solde insuffisant")

    def __str__(self):
        return "numero de compte: "+str(self.__numeroDe_compte)+"    nom: "+self.__nom+"    prenom: "+self.__prenom+"    solde: "+str(self.__solde)





compte1 = CompteBancaire(1, "Kololo", "Gavi", 1000)
compte1.afficher()
compte1.versement(100)
compte1.agios()
compte2 = CompteBancaire(2, "John", "Doe", 1000)
compte1.virement(2, compte2, 500)
print(compte1)
