import math

class Point:
    def __init__(self,x = 0.0 ,y = 0.0):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            print("Error: Coordinates must be numbers.")
            return
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)


p = Point(3,4)
print(p.x)
print(p.y)
print(p.distance_from_origin())

p2 = Point('hg',4) #error