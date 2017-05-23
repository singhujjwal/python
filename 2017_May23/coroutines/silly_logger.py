def log(filename="sillylog.log"):
    with open(filename, "a") as out:
        while True:
            line = yield
            if not line: break
            out.write(line)
            yield


if __name__ == '__main__':
    logger = log("testlog.log")

    next(logger)
    logger.send("this is line 1")
    
    next(logger)
    logger.send("this is line 2")

    next(logger)
    logger.send("this is line 3")

    next(logger)
    logger.send(None)

    next(logger)

