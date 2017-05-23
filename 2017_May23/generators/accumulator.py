def accumulate(total=0):
    while True:
        v = yield
        if not v: break
        total += v
        yield total


if __name__ == '__main__':
    acc = accumulate()
    values = [1, 2, 3, 4, 5]

    for a in acc:
        if not len(values): break
        print acc.send(values.pop(0))

