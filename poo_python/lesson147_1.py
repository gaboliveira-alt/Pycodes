
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name} x={self.x!r} y={self.y!r}'
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)
    
    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y
        return result_self > result_other
    

if __name__ == '__main__':
    point1 = Point(4, 2)
    point2 = Point(6, 4)
    point3 = point1 + point2
    print(point3)
    print('P1 é maior que P2?', point1 > point2)
    print('P2 é maior que P1?', point2 > point1)
    