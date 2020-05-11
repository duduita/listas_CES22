# Questão 9

# Basicamente, quando se trata de herança, uma classe filho pode 
# herdar características do pai
# No entanto, em heranças múltiplas, há possiblidade de 'vários pais'
# Como no caso do quadradado que também é polígono, polígono regular
# e possui uma forma genérica

# O diferencial aqui, não obstante, reside no uso do MRO.
# Este que possui como característica fundamental mostrar a ordem
# que o python considera como hierarquica para as heranças
# principalmente quando se tem 'mais de um pai'

# Qual a ordem de prioridade que o python considera?
# Funciona como se fosse um DFS de busca em árvore
# É necessário fazer a árvore da herança múltipla.
# Em linhas gerais, podemos dizer, informalmente que a busca ocorre da forma:
# Primeiramente ele busca no filho, e depois vai indo dos pais da
# da 'esquerda para a direita'

class Shape:
    geometric_type = 'Generic Shape'

    def area(self) : 
        raise NotImplementeError
    
    def get_geometric_type(self):
        return self.geometric_type
    
class Plotter:

    def plot(self, ratio, topleft):
        print('Plotting at {}, ratio {}.'.format(topleft, ratio))

class Polygon(Shape, Plotter): 
    geometric_type = 'Polygon'

class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side

class RegularHexagon(RegularPolygon):
    geometric_type = 'RegularHexagon'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)

class Square(RegularPolygon):
    geometric_type = 'Square'

    def area(self):
        return self.side * self.side

# Criação de classes adicionais, conforme comando da questão

class Triangle(RegularPolygon):
    geometric_type = 'Triangle'

    def area(self):
        return self.side * self.side

class Pentagon(RegularPolygon):
    geometric_type = 'Pentagon'

    def area(self):
        return self.side * self.side


hexagon = RegularHexagon(10)
print(hexagon.area())
print(hexagon.get_geometric_type())
hexagon.plot(0.8, (75, 77))

triangle = Triangle(10)
print(triangle.area())
print(triangle.get_geometric_type())
triangle.plot(0.8, (75, 77))

pentagon = Pentagon(10)
print(pentagon.area())
print(pentagon.get_geometric_type())
pentagon.plot(0.8, (75, 77))

square = Square(12)
print(square.area())
print(square.get_geometric_type())
square.plot(0.93, (74, 75))

print(square.__class__.__mro__)
print(triangle.__class__.__mro__)
print(pentagon.__class__.__mro__)

