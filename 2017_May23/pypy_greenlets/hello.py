from greenlet import greenlet

def test1():
    print("In test1...")
    gr2.switch()
    print("Back in test1...")
    gr2.switch()

def test2():
    print("In test2...")
    gr1.switch()
    print("Back in test2...")

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
