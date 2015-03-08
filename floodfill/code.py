# def createGrid(h, w):
#     height = [[] for _ in range(h)]
#     return [['.' for i in range(w)] for _ in height]



# def substituteChar(x, y, c, grid):
#     try:
#         grid[x][y] = c
#         return grid
#     except IndexError:
#         print "Index Error. Grid is 0-index, x and y must be smaller than the grid size"


# def test():
# #Cretegrid test
#     a = createGrid(3, 3)
# #FloodFill test
# #print substituteChar(0, 0, '*', floodFill(0, 1, '*', a))
# #isContinious test
#     substituteChar(0, 0, '8', a)
#     substituteChar(0, 1, '8', a)
#     substituteChar(1, 1, '8', a)
#     substituteChar(2, 2, '8', a)
#     for i in a:
#         print i
#     # print isValid(a, (0, 2), 3, 3)
#     print a[0][2]

# test()

n,m = map(int, raw_input().split())
mem = [list(raw_input()) for _ in range(m)]
x,y,c = raw_input().split()
x,y = int(x), int(y)
base = mem[y][x]
working = {(x,y)}



if not base == c:
    while len(working) > 0:
        print mem
        x, y = working.pop()
        if mem[y][x] == base:
            print 'working is', len(working), working
            mem[y][x] = c
            working.update({((x-1)%n,y), ((x+1)%n, y), (x, (y-1)%m), (x, (y+1)%m)})

for s in mem:
    print(''.join(s))



