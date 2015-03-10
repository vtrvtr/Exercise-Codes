 # [2015-03-06] Challenge #204 [Hard] Addition chains


def construct_chain(chain, finalN):
    while chain[-1] < finalN:
        chain.append(max(chain) + chain[len(chain) - 1])
    return chain[:-1]


def fine_tunnint(chain, finalN):
    rest = finalN - chain[-1]
    while chain[-1] < finalN:
        print rest
        for n in reversed(chain):
            if n < rest and chain[-1] + n < finalN:
                rest = n
                chain.append(n + chain[-1])
                break
            elif rest == 1:
                chain.append(finalN)
                break
    return chain


def choose_better_path(length, finalN):
    paths = [[1, 2], [1, 2, 3], [1, 2, 3, 5]]
    for path in paths:
        add_chain = construct_chain(path, finalN)
        complete_chain = fine_tunnint(add_chain, finalN)
        print len(complete_chain)
        if len(complete_chain) == length + 1:
            return add_chain

choose_better_path(19, 123456)