from collections import defaultdict, Counter


h, w = 10, 10
txt = '''xx.z
    xx..
    ..yy
    z.yy'''


list_text = txt.split()



def findY(start_line, line_indice, char_indice, block_char, grid):
    block_y = 0
    for start_line in grid[line_indice:]:
        if start_line[char_indice] is block_char and start_line[char_indice] not in visited:
            block_y += 1
        else:
            return block_y


def findX(line_indice, block_char, grid):
    block_x = 0
    for x_char in grid[line_indice]:
        if x_char is block_char:
            block_x += 1
    return block_x

a = txt.strip()
b = a.split()

visited = []


def determineBlock(grid, base_sign, visited=[]):
    block_list = []
    visited = set(visited)
    print visited
    for line_indice, line in enumerate(grid):
        block_char = None
        base_sign = '.'
        for char_indice, char in enumerate(line):
            # print char,
            if char is not base_sign and char not in visited:
                print char
                #print block_char
                if block_char is None:
                    block_char = char
                block_x = findX(line_indice, block_char, grid)
                print block_x
                if char is not block_char and char not in visited:
                    #print visited, char
                    return block_x, block_y, block_char
                block_y = findY(
                    line, line_indice, char_indice, block_char, grid)
                print block_y
                visited.update(block_char)
    return block_list



def determineSigns(grid):
    all_signs = [signs for lines in grid for signs in lines if signs is not '.']
    return set(all_signs)



def test():
    print determineBlock(b, '.')





def test2():
    count = defaultdict(int)
    amounts = []
    visited = []
    x_list = []
    y_list = []
    for sign in set([signs for lines in b for signs in lines if signs is not '.']):
        amounts.append((sign, sum(x.count(sign) for x in b)))
    for line in b:
        for char in line:
            if char is not '.' and char not in visited:
                x_list.append((char, sum(x.count(char) for x in line)))
                visited.append(char)

    sorted_total = sorted(amounts, key=lambda x: x[0])
    sorted_x = sorted(x_list, key=lambda x: x[0])
    
    for total, x in zip(sorted_total, sorted_x):
        print "Block of size {0}x{1} made of {2}".format(x[1], total[1]/x[1], total[0])


def test3(grid, sign, x_line):
    x = sum(x.count(sign) for x in x_line)
    y = sum(x.count(sign) for x in grid)/x
    return x,y

print test3(b, 'z', b[0])   
