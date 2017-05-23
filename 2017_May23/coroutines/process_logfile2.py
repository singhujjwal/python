def read_log(filename="system.log"):
    with open(filename) as log:
        for line in log:
            yield line


def filter_log(regex):
    import re
    pattern = re.compile(regex)
    while True:
        line = yield
        #yield pattern.findall(line) 
        if pattern.search(line):
            yield line
        else:
            yield None

def count_lines(total=0):
    while True:
        line = yield
        if type(line) is str:
            total += 1
        yield total

if __name__ == '__main__':
    asterisks = filter_log(r'info')
    asterisks.next()

    count = count_lines()
    count.next()

    for line in read_log():
        result = asterisks.send(line)
        t = count.send(result)
        if type(line) is str:
            print "Line: {}, Count: {}".format(result, t)

        asterisks.next()
        count.next()


