class firstCLass:
    """ first calls variables"""
    classname = "first"
    i= 1234
    def __init__(self):
            print("init called")
    def __init__(self,i):
            print("init called")
            self.i=i
    def f(self):
        print("values are {}| {}".format(self.classname,self.i))


firstObject = firstCLass(2)
print(firstObject.i)
print(firstObject.classname)
firstObject.f()


class SecondCHildClass(firstCLass):
    pass

secondObject = SecondCHildClass(23)
print(secondObject.f())

class thisCLass(firstCLass):
    j= 1234
    def __init__(self):
            print("init called")
    def __init__(self,i,j):
            print("init called")
            self.i=i
            self.j=j
    def f(self):
        print("values are {}| {} | {}".format(self.classname,self.i,self.j))


firstObject = firstCLass(99)
print(firstObject.i)
print(firstObject.classname)
firstObject.f()


thirdObject =thisCLass(88,77)
print(thirdObject.i)
print(thirdObject.classname)
thirdObject.f()
