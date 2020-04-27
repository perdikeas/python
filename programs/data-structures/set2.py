#!/usr/bin/env python3.7


class Set():

    def __init__(self):
        self.buffer=list()
        self._ix=0

    def contains(self,value):
        return  value in self

    def length(self):
        return len(self.buffer)

    def add(self,value):
        if not self.contains(value):
            self.buffer.append(value)

    def is_subset_of(self,setb):
        for i in self:
            if not setb.contains(i):
                return False
        return True


    def is_equal_to(self,setb):
        return self.is_subset_of(setb) and setb.is_subset_of(self)

    def union(self,setb):
        setc=Set()
        setc.buffer.extend(self.buffer)
        for value in setb:
            if not self.contains(value):
                setc.add(value)

        return setc

    def remove(self,value):
        assert self.contains(value),"This value is not in the set"
        self.buffer.remove(value)

    def cartesian_join(self,setb):
        setc=Set()
        for i in self:
            for j in setb:
                setc.add((i,j))
        return setc

    def intersect(self,setb):
        setc=Set()
        for i in self:
            if setb.contains(i):
                setc.add(i)
        for j in setb:
            if self.contains(j):
                setc.add(j)
        return setc

    def difference(self,setb):
        setc=Set()
        for value in self:
            if not setb.contains(value):
                setc.add(value)
        return setc

    def __iter__(self):
        return self

    def __next__(self):
        if self._ix < len(self.buffer):
            v = self.buffer[self._ix]
            self._ix += 1
            return v
        else:
            self._ix=0
            raise StopIteration

    def _print(self):
        print(self.buffer)

a=Set()
a.add(2)
a.remove(2)
a.add(3)
for i in range(1,10):
    a.add(i)
b=Set()
for i in range(1,10):
    b.add(i**2)
c=a.union(b)
d=a.cartesian_join(b)

a._print()
b._print()
c._print()
d._print()
