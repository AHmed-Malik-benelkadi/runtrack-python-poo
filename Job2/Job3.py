class livre():
    def __init__(self):
        self.disponible = True

    def verification(self):
        if self.disponible == True:
            print("Le livre est disponible")
        else:
            print("Le livre n'est pas disponible")
    def emprunter(self):
        if self.disponible == True:
            self.disponible = False
            print("Vous avez emprunté le livre")
        else:
            print("Le livre n'est pas disponible")

    def rendre  (self):
        if self.disponible == False:
            self.disponible = True
            print("Vous avez rendu le livre")
        else:
            print("Le livre n'est pas disponible")

livre1 = livre()
livre1.verification()
livre1.emprunter()


