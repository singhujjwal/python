def read_log(filename="system.log"):
    with open(filename) as log:
        for line in log:
            yield line


def filter_log(regex):
    import re
    pattern = re.compile(regex)
    while True:
        line = yield
        if type(line) is not str: 
            yield None
        else:
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
    info = filter_log(r'info')
    next(info)  # start the co-routine

    eth1 = filter_log(r'eth1')
    next(eth1)   # start the co-routine

    for line in read_log():
        result = info.send(line)
        if result is str:
            ethernet_interfaces = eth1.send(result)
            if ethernet_interfaces:
                print(ethernet_interfaces)

        next(info)
        next(eth1)


