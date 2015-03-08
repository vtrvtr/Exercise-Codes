class VennDiagram(object):
    def __init__(self, total_size):
        self.total_size = total_size
        self.sectors = []
    def add_sector(self, name, size):
        self.name = name
        self.size = size
        self.sectors.append([(name, size)])
    def check_sectors(self, name):
        self.name = name
        for v in self.sectors: 
            if v == name:
                return v


def test():
    a = VennDiagram(0.85)
    a.add_sector('b1', None)
    a.add_sector('b2', 0.1)

    print a.total_size - a.check_sectors('A') 
 


test()