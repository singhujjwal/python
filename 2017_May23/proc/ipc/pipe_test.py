from multiprocessing import Process, Pipe

class Car:
    def __init__(self, name):
        self.name = name

    def __str__(self): return "Car object, name = %s" % self.name


def sender(p):
    p.send(10)
    p.send(["john", "sam", 45.66])
    p.send(Car(name="Honda"))

def receiver(p):
    print p.recv()
    print "-" * 40
    print p.recv()
    print "-" * 40
    print p.recv()
    print "-" * 40



write_end, read_end = Pipe()

p1 = Process(target=sender, args=(write_end,))
p2 = Process(target=receiver, args=(read_end,))

p1.start()
p2.start()















