def store(outfile):
    with open(outfile, "a") as out:
        while True:
            line = yield
            out.write(line.upper() + "\n")
            #yield 
            if not line: break

output = store("data.log")
output.next()

try:
    while True:
        line = raw_input("Enter data: ")
        output.send(line)
except StopIteration: pass


    
