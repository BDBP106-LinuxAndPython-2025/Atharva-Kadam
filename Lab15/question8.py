x=float(input("Enter x coordinate: "))
y=float(input("Enter y coordinate: "))
if ( x>0 and y>0 ):
    print("The point is in Quadrant 1")
elif ( x<0 and y>0 ):
    print("The point is in Quadrant 2")
elif ( x<0 and y<0 ):
    print("The point is in Quadrant 3")
else :
    print ("The point is in Quadrant 4")