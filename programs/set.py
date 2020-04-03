#!/usr/bin/env python3.7
class Set():
    def __init__(self):
        self.buffer=list()
        self._ix=0

    def print(self):
        print(self.buffer)

    def len(self):
        return len(self.buffer)

    def contains(self,element):
        for value in self:
            if value==element:
                return True
        return False

    def add(self,element):
        if not self.contains(element):
            self.buffer.append(element)

    def remove(self,element):
        assert self.contains(element) , 'element must be in set'

        self.buffer.remove(element)

    def is_equal_to(self,setb):
        return self.is_subset_of(setb) and setb.is_subset_of(self)

    def is_subset_of(self,setb):
        setb=Set()

        for value in self:
            if not setb.contains(value):
                return False

        return True

    def union(self,setb):
        setc=Set()

        setc.buffer.extend(self.buffer)

        for value in setb:
            if not self.contains(value):
                setc.add(value)

        return setc

    def cartesian_joint(self,setb):
        setc=Set()

        for value in self:
            for element in setb:

                setc.add((value,element))

        return setc

    def intersect(self,setb):
        setc=Set()

        for value in self:
            if  setb.contains(value):
                setc.add(value)

        for value in setb:
            if  self.contains(value):
                setc.add(value)

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
            #print ("{}".format(self._ix))
            v = self.buffer[self._ix]
            self._ix += 1
            return v
        else:
            self._ix=0
            raise StopIteration


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
d=a.cartesian_joint(b)

a.print()
b.print()
c.print()
d.print()


class Person():
    def __init__(self):
        self.name = 'John Smith'
        self.age = 44
    def __iter__(self):
        yield self.name
        yield self.age



p = Person()
pl = list(p)
print (pl)
