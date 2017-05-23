def accumulate(total=0):
    while True:
        total += yield
        yield total


if __name__ == '__main__':
    acc = accumulate()
    acc.next()

    print acc.send(10)
    acc.next()

    print acc.send(20)
    acc.next()

    print acc.send(30)
    acc.next()


