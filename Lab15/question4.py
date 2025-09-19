import math
degree=float(input("Enter the Angle (in degrees):"))
rad=degree*(math.pi/180) #can also use math.radians(degree)
print(f'sin={math.sin(rad)}')
print(f'cos={math.cos(rad)}')
print(f'tan={math.tan(rad)}')
print(f'cosec={1/math.cos(rad)}')
print(f'cot={1/math.tan(rad)}')
print(f'sec={1/math.cos(rad)}')

