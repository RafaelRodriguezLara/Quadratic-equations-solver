import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

x1 = -b - (math.sqrt(b*b - (4*a*c)))/2*a
x2 = -b + (math.sqrt(b*b - (4*a*c)))/2*a

print("x1 = ", x1)
print("x2 = ", x2)
