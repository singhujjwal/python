from MyMath import MyManager


manager = MyManager(address=('127.0.0.1', 6060), authkey="secret")


manager.connect()
math = manager.Maths()
print math.add(10, 20)
print math.mul(20, 30)





