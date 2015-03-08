def someFunction(word_to_find, text):
    t = ''
    with open(text) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if (word_to_find in line):
                t += get_surounding_text(lines, i, True)
                t += get_surounding_text(lines, i)
                return t


def get_surounding_text(text, index, reverse=False):
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

print someFunction('break this enterprise', 'shakespeare.txt')
