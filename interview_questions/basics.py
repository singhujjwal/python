#!/home/centos/p38/bin/python

import collections
from typing import OrderedDict



def defaultdict_factory():

    # default values as set so can be used as a h
    graph = collections.defaultdict(set)
    print (graph)

    # DEfault dictionary of values as list
    d = collections.defaultdict(list)
    print (d)

    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    for k,v in s:
        d[k].append(v)
    print (d)
    print (sorted(d.items()))

    # easy to find number of characters in a string

    s = 'missisippi'
    ss = collections.defaultdict(int)
    for char in s:
        ss[char] +=1

    print (sorted(ss))


def namedtuple_Example():
    Point = collections.namedtuple("Point", ['x','y'])
    p = Point(11, y=12)
    q = Point(23,22)
    x,y = p
    v = p.x + p.y

class LRU(OrderedDict):
    'Limit size, evicting the least recently looked-up key when full'

    def __init__(self, maxsize=128, /, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        if key in self:
            self.move_to_end(key)
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]


def array():
    N= 5
    arr =[0]*5
    print (arr)

    arr = [0 for i in range(N)]
    print (arr)

    rows, cols = (7, 5)

    arr = [[0]*cols]*rows
    print (arr)
    arr = [[0 for i in range(cols)] for j in range(rows)]

    print (arr)


def main():
    print (f"Hello...")
    # Dictionary
    d = {'a': 4, 'b':312312, 'd': 'ASasdsa', 'e': ['My', "Nmae"]}
    d = {'a': 4, 'b':312312, 'd': 41, 'e': 123}
    print (d)


    for v in d.values():
        print (v)

    for k,v in d.items():
        print (f"The key is {k} and value is {v}")

    mydict = {'george': 16, 'amber': 19}
    print(list(mydict.keys()))
    print(list(mydict.values()))
    # [list(mydict.values()).index(16)])  # Prints george





if __name__ == '__main__':
    # main()
    # defaultdict_factory()
    array()