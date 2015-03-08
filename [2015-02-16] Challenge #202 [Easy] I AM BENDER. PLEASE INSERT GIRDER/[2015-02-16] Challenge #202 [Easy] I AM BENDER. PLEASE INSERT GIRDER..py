 # [2015-02-16] Challenge #202 [Easy] I AM BENDER. PLEASE INSERT GIRDER.

def fix_input(user_input):
    return ''.join(user_input.split('\n'))

def split_in_8(binary):
    return (binary[i:i+8] for i in range(0, len(binary), 8))

def binary_to_text(binary):
    word = ''
    for char in split_in_8(binary):
        word += chr(int(str(char),2))
    print word

def main():
    inp = input('What did you say to me?! ')
    inp = fix_input(str(inp))
    binary_to_text(inp)


main()

