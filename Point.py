import math

class Point:
    def __init__(self, x=0, y=0):
        self.move(x,y)

    def move(self, x, y):
        self.x = x
        self.y = y
    
    def reset(self):
        self.move(0,0)

    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x)**2 + 
            (self.y - other_point.y)**2
        )

# Using it:
p1 = Point(1,2)
p2 = Point(3,4)
p3 = Point()
print(p1.calculate_distance(p2))
p2.move(5,0)
print(p2.calculate_distance(p3))
assert (p2.calculate_distance(p1) == p1.calculate_distance(p2))
p1.move(3,4)
print(p1.calculate_distance(p2))
print(p1.calculate_distance(p3))