 # [2015-03-18] Challenge #206 [Intermediate] Maximizing Crop Irrigation
from tabulate import tabulate
grid = '''.x.
..x'''


class Grid():

    def __init__(self, height, width, grid):
        self.height = height
        self.width = width
        self.grid = [[token for token in line] for line in grid.split()]

    def __str__(self):
        table = self.grid
        return tabulate(table, tablefmt="grid")

    def place_circle(self, circle, position):
        self.circle = circle
        self.x, self.y = position
        self.grid[self.x][self.y] = 'o'

    def circle_pos(self):
        try:
            return self.x, self.y
        except:
            return "There's no circle"

    def count_crops(self):
        crops = 0
        circle_center = (self.x, self.y)
        for token in self.grid[self.x][self.y:self.y+self.circle.radius+1]:
            if token is 'x':
                crops += 1
        print self.grid[self.circle.radius][self.y]
        for token in self.grid[self.x][self.y]:
            if token is 'x':
                crops += 1
        return crops

class Circle():

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return str('Radius: {}'.format(self.radius))

a = Grid(2, 3, grid)
b = Circle(1)


# print a
# print b.radius
a.place_circle(b, [1,1])
print a 
# print a.circle_pos()
# print a.circle
print a.count_crops()


    