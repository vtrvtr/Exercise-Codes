import random

number2banner = {'0' : [' _ ','| |','|_|','   '],
                 '1' : ['   ','  |','  |','   '],
                 '2' : [' _ ',' _|','|_ ','   '],
                 '3' : [' _ ',' _|',' _|','   '],
                 '4' : ['   ','|_|','  |','   '],
                 '5' : [' _ ','|_ ',' _|','   '],
                 '6' : [' _ ','|_ ','|_|','   '],
                 '7' : [' _ ','  |','  |','   '],
                 '8' : [' _ ','|_|','|_|','   '],
                 '9' : [' _ ','|_|',' _|','   '],}

input_list = []
input_table = []

file_input = '923'

#Extract data from file
for line in file_input:
    if line[0] == " ":
        line = line[1:]
    line = line.replace('\n',"")
    input_list = list(line)
    input_table.append(input_list)


for inputLine in input_table:
    banner = ['','','','']
    for digit in inputLine:
        for i in range(4):
            banner[i] = banner[i] + (number2banner[digit][i])
    for i in range(4):
        print(banner[i])



def test():
    choice = [0, 1]
    for i in range(1000):
        print(random.choice(choice)),



test()