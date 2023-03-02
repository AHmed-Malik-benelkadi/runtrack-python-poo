class Tache():
    def __init__(self,titre,description,status):
        self.titre = titre
        self.description = description
        self.status = status

    def __str__(self):
        return "titre: "+self.titre+"    description: "+self.description+"    status: "+self.status

class ListeDeTaches():
    def __init__(self,taches):
        self.taches = taches

    def ajouterTache(self,tache):
        self.taches.append(tache)
    def supprimerTache(self,tache):
        self.taches.remove(tache)
    def marquer_commefini(self,tache):
        tache.status = "fini"
    def afficherListe(self):
        """qui permet de retourner une liste de toutes les taches."""
        return self.taches

    """qui permet de filtrer les taches par rapport à un statut et retourne
cette liste."""
    def filtrerListe(self,status):
        liste = []
        for tache in self.taches:
            if tache.status == status:
                liste.append(tache)
        return liste

    def __str__(self):
        return "taches: "+str(self.taches)


Tache1 = Tache("manger","description1","en cours")
Tache2 = Tache("dormir","description2","en cours")
Tache3 = Tache("travailler","description3","en cours")
Tache4 = Tache("sport","description4","en cours")
Tache5 = Tache("voyager","description5","en cours")

liste = [Tache1,Tache2,Tache3,Tache4,Tache5]
listeDeTaches = ListeDeTaches(liste)
for tache in listeDeTaches.afficherListe():
    print(tache)
listeDeTaches.ajouterTache(Tache("titre6","description6","en cours"))
for tache in listeDeTaches.afficherListe():
    print(tache)

listeDeTaches.supprimerTache(Tache1)
for tache in listeDeTaches.afficherListe():
    print(tache)
listeDeTaches.marquer_commefini(Tache2)
for tache in listeDeTaches.afficherListe():
    print(tache)
print(listeDeTaches.filtrerListe("fini"))

#
