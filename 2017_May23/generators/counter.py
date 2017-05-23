def count():
    i = 0
    while True:
        yield i
        i += 1


def chain(*sequence):
    for i in sequence:
        for j in i: yield j

