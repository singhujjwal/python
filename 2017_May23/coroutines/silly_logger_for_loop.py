def log(filename="sillylog.log"):
    with open(filename, "a") as out:
        while True:
            line = yield
            if not line: break
            out.write(line)
            yield line


if __name__ == '__main__':
    logger = log("testlog.log")

    i = 0
    for line in logger:
        logger.send("Counting {}".format(i))
        if i > 10: logger.send(None)
        i += 1


