# Questão 5, 6 e 7

# Conforme pedido, segue abaixo uma função com várias classes, como reflect_x, get_line_to, slopeFromPoint.
# O caso que irá falhar será quando x for 0, nesse caso, ele retornará 'none'.

class Point:

#Point class for representing and manipulating x,y coordinates

    def __init__(self, initX, initY):

#Create a new point at the given coordinates

        self.x = in
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def reflect_x(self):
        return Point(self.x,-self.y)
        
    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

#define a method called slopeFromOrigin here

    def slopeFromPoint(self):
        if self.x == 0:
            return None
        return self.y / self.x

#define a method called coeficients
    def get_line_to(self, point):
        m = (self.y - point.y) / (self.x - point.x)
        b = self.y - (m*self.x)
        return (m,b)


