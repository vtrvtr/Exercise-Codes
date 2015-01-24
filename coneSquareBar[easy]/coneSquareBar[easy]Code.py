import math


class Shapes(object):

    def __init__(self, area):
        self.area = area
        self.height = math.sqrt(area)
        self.width = math.sqrt(area)

    def __str__(self):
        return "This is a generic shape of height {0} and width {1}".format(self.height, self.width)

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width


class Cube(Shapes):

    def __init__(self, volume):
        Shapes.__init__(self, volume)
        self.volume = volume
        self.compriment = math.pow(volume, 1 / 3.0)
        self.height = math.pow(volume, 1 / 3.0)
        self.width = math.pow(volume, 1 / 3.0)
        self.height = float(math.pow(volume, 1 / 3.0))

    def __str__(self):
        return "A generic cube of height {0} and width {1} and compriment {2}".format(self.height, self.width, self.compriment)

    def Volume(self):
        return self.volume

    def getCompriment(self):
        return self.compriment


class Cilinder(Shapes):

    def __init__(self, volume, height=5):
        self.volume = volume
        self.height = height
        self.radius = float(volume) / (math.pi * 2 * self.height)

    def __str__(self):
        return "A generic cilinder of height {0} and radius {1}".format(self.height, self.radius)

    def Volume(self):
        area = 2 * math.pi * self.radius
        return self.volume

    def getRadius(self):
        return self.radius


class Sphere(Cilinder):

    def __init__(self, volume):
        Cilinder.__init__(self, volume)
        self.radius = float(volume) / (math.pi * 2 * 5)

    def __str__(self):
        return "A generic shpere of radius {0}".format(self.radius)

    def Volume(self):
        return self.volume


class Cone(Cilinder):

    def __init__(self, volume, height=5):
        self.height = height
        self.radius = float(volume) / (math.pi * 2 * self.height)
        self.volume = volume

    def Volume(self):
        return self.volume

    def __str__(self):
        return "A generic cone of radius {0} and height {1}".format(self.radius, self.height)


# def test():
#     a = Shapes(10)
#     print a
#     print a.getHeight()
#     b = Cube(100)
#     print b
#     print b.getWidth()
#     print b.getCompriment()
#     c = b.Volume()
#     print c
#     d = Cilinder(11)
#     print d
#     print d.Volume()
#     print d.getRadius()
#     e = Sphere(20)
#     print e
#     print e.getRadius()
#     print e.Volume()
#     f = Cone(100)
#     print f
#     print f.getRadius()
#     print f.Volume()
# test()


def ShapesFit(volume, shape = ['Cone', 'Cube', 'Cilinder', 'Sphere'], height = 5):
	if len(shape) > 1:
		for eachShape in shape: 
			print globals()[eachShape](volume)
	else:
		shape = ''.join(shape)
		print globals()[shape](volume)


def test2():
	#print ShapesFit(39)

	 for i in xrange(6):
	 	a = i*3
	 	print "{0} cubic meters would fit in:".format(a)
	 	
	 	print ShapesFit(a)
test2()