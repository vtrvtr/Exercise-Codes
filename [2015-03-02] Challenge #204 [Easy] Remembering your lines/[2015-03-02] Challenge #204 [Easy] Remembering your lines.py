def main(word_to_find, text):
    t = ''
    with open(text) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if (word_to_find in line.lower()):
                t += get_surounding_text(lines, i, True)
                t += get_surounding_text(lines, i)
                return t


def get_surounding_text(text, index, reverse=False):
# Gets the text below or above (reverse for above text)
    t = []
    if reverse:
        for line in reversed(text[:index]):
            t.append(line)
            if line in ('\n', '\r\n'):
                return ''.join(reversed(t))
    else:
        for line in text[index:]:
            t.append(line)
            if line in ('\n', '\r\n') or '[' in line:
                return ''.join(t[:-1])


if __name__ == '__main__':
    text = raw_input('text pls\n')
    word = raw_input('excerpt to find\n')
    print main(word.lower(), text)
