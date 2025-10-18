"""(2) Idea of inheritance- parent and child classes. Extend the Quadrilateral class with two
child classes - Square and Rectangle. In the constructor of the child classes, call the
parent’s constructor with a single side or 2 sides as the case may be. Define functions
getArea() in the child classes that return the area of the square or the rectangle."""
class Quadrilateral:
    def __init__(self,side1,side2,side3,side4):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        self.side4=side4

class Square(Quadrilateral):
    def __init__(self,side):
        super().__init__(side,side,side,side)

    def getArea(self):
        return self.side1*self.side1

s_a=Square(2)
print(f"The area of the square is:{s_a.getArea()}")

class Rectangle(Quadrilateral):
    def __init__(self,len,bred):
        super().__init__(len,bred,len,bred)

    def getArea(self):
        return 2*(self.side1 + self.side3)

r_a=Rectangle(2,3)
print(f"The area of the rectangle is:{r_a.getArea()}")

