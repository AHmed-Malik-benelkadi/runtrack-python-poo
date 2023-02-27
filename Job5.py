class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print("le point X,Y est : ", self.x, self.y)
    def afficherX(self):
        print("le point  X est de  : ", self.x)
    def afficherY(self):
        print("le point  Y est de  : ", self.y)
    def changerX(self, x):
        self.x = x
    def changerY(self, y):
        self.y = y

object1 = Point(10, 20)
object1.afficherLesPoints()
object1.afficherX()
object1.afficherY()
object1.changerX(33)
object1.changerY(44)
object1.afficherLesPoints()
