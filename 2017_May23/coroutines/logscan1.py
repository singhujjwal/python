def scan_log(filename, substr):
    with open(filename) as log:
        for line in log:
            if substr in line: yield line


if __name__ == '__main__':
    from sys import argv
    if len(argv) < 3:
        print("usage: {} filename search-string".format(argv[0]))
        exit(1)

    for line in scan_log(argv[1], argv[2]):
        print("-" * 40)
        print(line.upper())


