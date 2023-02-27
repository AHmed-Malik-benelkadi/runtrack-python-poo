class Personnage():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1
    def droite(self):
        self.x += 1
    def haut(self):
        self.y += 1
    def bas(self):
        self.y -= 1

    def position(self):
        # sous forme de tuple  (x,y)
        return (self.x, self.y)

object1 = Personnage(1, 2)
print(object1.position())
object1.gauche()
print(object1.position())
object1.droite()
print(object1.position())
object1.haut()
print(object1.position())
object1.bas()
print(object1.position())

