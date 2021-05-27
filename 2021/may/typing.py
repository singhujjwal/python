#!/usr/bin/python

# Type Aliases

Vector = list()

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar*num for num in vector]








if __name__ == "__main__":
    a = [2,3,4,5.0]
    print (scale(10.0, a))