class myClass():
    name = ''
    age = 0
    def __init__(self, name = '', age = 0):
        self.name = name
        self.age = age
        
    def showName(self):
        print("My name is ", self.name)

    def showAge(self):
        print("My age is ", self.age)
        

class child(myClass):
    def showName(self):
        print("My name child is ", self.name)

    def showAge(self):
        print("My age child is ", self.age)

       
# test1 = myClass()
# test1.showName()
# test1.showAge()


# test2 = myClass('Đức', 18)
# test2.showName()
# test2.showAge()
