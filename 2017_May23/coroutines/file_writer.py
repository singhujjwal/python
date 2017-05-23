def store(outfile):
    with open(outfile, "a") as out:
        while True:
            line = yield
            out.write(line.upper() + "\n")
            yield 
            if not line: break

output = store("data.log")
#output.next()
#output.send("This is line 1")
#output.next()
#output.send("This is line 2")
#output.next()
#output.send("This is line 3")
#output.next()
#output.send("")
#output.next()

for i in output:
    line = raw_input("Enter data: ")
    output.send(line)

    
