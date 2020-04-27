#!/usr/bin/env python3.7

#easy way
class Map_elements():
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self._ix=0

class Map():
    def __init__(self):
        self.list=list()

    def len(self):
        return len(self.list)

    def print(self):
        list_to_print=list()
        for index in self.list:
            list_to_print.append((index.key,index.value))
        print(list_to_print)

    def find_position(self,key):
        for i in range(len(self.list)):
            if self.list[i].key==key:
                return i
        return None

    def add(self,key,value):
        index=self.find_position(key)
        if index!=None:
            self.list[index].value=value
        else:
            self.list.append(Map_elements(key,value))

    def contains(self,key):
        index=self.find_position(key)
        if index!=None:
            return True
        return False

    def valueof(self,key):
        index=self.find_position(key)
        assert index!=None
        return self[index].value

    def remove(self,key):
        index=self.find_position(key)
        assert index!=None
        self.list.pop(index)


    #for now it is unecessary but I might need it later
    #iterator implementation
    
    def __iter__(self):
        return self
    def __next__(self):
        if self._ix<len(self.list):
            rv=self.list[self._ix]
            self._ix+=1
            return rv
        else:
            self.ix=0
            raise StopIteration
map1=Map()

cars=['bugatti','ferrari','rolls-royce']
i=0
while i<3:
    map1.add(cars[i],i)
    i+=1
map1.print()
print(map1.len())
print(map1.contains('bugatti'))
