#!/usr/bin/python
"""
    Purpose: Demo Class and inheritence
"""

class myClass():
    def __init__(self, num1,num2):
        self.num1 = num1
        self.num2 = num2
        #return None    return type of __init__ is always and always None
    
    def mul(self):
        return self.num1*self.num2

    #This method is used for priting the object
    def __str__(self):
       return f'num1 :{str(self.num1)}\nnum2 :{str(self.num2)}\n '
    
    #This method is used for printing incases if __str__ is not defined
    def __repr__(self):
        return f'num1 :{str(self.num1)}\nnum2 :{str(self.num2)}\n '



class mySubClass(myClass):
    def __init__(self,num1,num2):
        super().__init__( num1,num2  )


if __name__ == "__main__":
    myClass = myClass(12,23)
    print(myClass)
    print(myClass.mul())
    print(10*"=" +" >MySubclass")
    mySubClass = mySubClass(34,56)
    print(mySubClass)
