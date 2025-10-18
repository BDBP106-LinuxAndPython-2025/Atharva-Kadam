"""(1) Create a class called Quadrilateral that takes in four parameters - side1, side2, side3 and
side4. Write two functions isSquare() and isRectangle() that checks for all the sides
being equal (for a square) and the opposite sides being equal (for a rectangle), and returns
True/False. Create an instance of the Quadrilateral with (a) all sides being different,
(b) Opposite sides being same, (c) all sides being the same. Print the appropriate output."""
class Quadrilateral:
    def __init__(self,side1,side2,side3,side4):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        self.side4=side4

    def isSquare(self):
        if self.side1==self.side2==self.side3==self.side4:
            return True
        else:
            return False

    def isRectangle(self):
        if self.side1==self.side3 and self.side2==self.side4:
            return True
        else:
            return False
q_a=Quadrilateral(1,2,3,4)
q_b=Quadrilateral(1,2,1,2)
q_c=Quadrilateral(2,2,2,2)
print("Quadrilateral with all different sides:")
print(f"(a)Is the first instance q_a a square? {q_a.isSquare()}")
print(f"(a)Is the first instance q_a a rectangle? {q_a.isRectangle()}")
print()
print("Quadrilateral with two same sides:")
print(f"(b)Is the first instance q_b a square? {q_b.isSquare()}")
print(f"(b)Is the first instance q_b a rectangle? {q_b.isRectangle()}")
print()
print("Quadrilateral with all same sides:")
print(f"(c)Is the first instance q_c a square? {q_c.isSquare()}")
print(f"(c)Is the first instance q_c a rectangle? {q_c.isRectangle()}")
print()
