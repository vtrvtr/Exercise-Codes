 # [2015-03-18] Challenge #206 [Intermediate] Maximizing Crop Irrigation
from tabulate import tabulate
grid = '''..xx
x...
x...'''


class Grid():

    def __init__(self, width, height, grid):
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
        known_crops = []
        for i, row in enumerate(self.grid):
            for j, item in enumerate(row):
                if item is 'x':
                    if i - self.y >= 0 and ((i, j) not in known_crops):
                        crops += 1
                        known_crops.append((i, j))
                    elif j - self.y >= 0 and ((i, j) not in known_crops):
                        crops += 1
                        known_crops.append((i, j))
                    elif (j + self.y >= 0) and (i + self.x >= 0) and (i, j) not in known_crops:
                        crops += 1
                        known_crops.append((i, j))
        return crops


class Circle():

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return str('Radius: {}'.format(self.radius))

a = Grid(len(grid), len(grid[0]), grid)
print len(grid)
b = Circle(1)


# print a
# print b.radius
a.place_circle(b, [2, 1])
print a
# print a.circle_pos()
# print a.circle
print a.count_crops()

