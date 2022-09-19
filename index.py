#import module as module1
#import package.module as module2
import myclass as myClass

#print("Tong 2 so la: " + str(module1.testPlus(1, 2)))

#print("Hieu 2 so la: " + str(module2.testMinus(1, 2)))


# test1 = myClass.myClass()
# test1.showName()
# test1.showAge()


# test2 = myClass.myClass('Đức', 18)
# test2.showName()
# test2.showAge()


test1 = myClass.myClass('Van', 20)
test1.showName()
test1.showAge()


test2 = myClass.child('Đức', 18)
test2.showName()
test2.showAge()

