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

        return self.taches


    def filtrerListe(self,status):
        liste = []
        for tache in self.taches:
            if tache.status == status:
                liste.append(tache)
        return liste

    def __str__(self):
        return "taches: "+str(self.taches)


Tache1 = Tache("manger","Je doit manger ce soir ","Fini")
Tache2 = Tache("dormir","Aprés avoir manger je doit dormir ","en cours")
Tache3 = Tache("travailler","Puis le lendemain je doit aller au travaille ","en cours")
Tache4 = Tache("sport","Aprés le travaille je doit aller a la salle de sport ","en cours")
Tache5 = Tache("voyager","Apres de mois de travaille je merite un voyage ","en cours")

liste = [Tache1,Tache2,Tache3,Tache4,Tache5]
listeDeTaches = ListeDeTaches(liste)
for tache in listeDeTaches.afficherListe():
    print(tache)
listeDeTaches.ajouterTache(Tache("Repos","Et puis je doit me reposé","en cours"))
for tache in listeDeTaches.afficherListe():
    print(tache)

listeDeTaches.supprimerTache(Tache1)
for tache in listeDeTaches.afficherListe():
    print(tache)
listeDeTaches.marquer_commefini(Tache2)
for tache in listeDeTaches.afficherListe():
    print(tache)
print(listeDeTaches.filtrerListe("fini ! "))

#
