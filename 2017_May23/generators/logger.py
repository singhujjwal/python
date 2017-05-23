def log(filename, ident):
    template = "{time} {host} {ident}: {msg}\n"
    from time import ctime
    from os import uname
    hostname = uname()[1]

    with open(filename, "a") as logfile:
        while True:
            line = yield
            if line is not None:
                output = template.format(time=ctime(), 
                                         host=hostname, 
                                         ident=ident, 
                                         msg=line)
                logfile.write(output)
             yield
             if line is None: break


