class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    def setInfo(self, nm, a):
        self.name = nm
        self.age = a

    def getInfo(self):
        print("Name   :", self.name)
        print("Age    :", self.age)


# Main program (same as ObjectCreation)
p = Person()   # object creation
p.setInfo("Akshay", 26)
p.getInfo()