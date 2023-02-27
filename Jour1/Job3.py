class Operation():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        return self.number1 + self.number2
        print("la somme est: ", self.number1 + self.number2)

object1 = Operation(11, 22)
print(object1.addition())
