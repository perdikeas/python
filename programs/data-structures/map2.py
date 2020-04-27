#!/usr/bin/env python3.7

class Map_entry():

    def __init__(self,key,value):
        self.key=key
        self.value=value

class Map():
    def __init__(self):
        self.buffer=list()
        self._ix=0

    def len(self):
        return len(self.buffer)

    def contains(self,key):
        for element in self:
            if element.key==key:
                return True

    def find_position(self,key):
        for index in range(len(self.buffer)):
            if self.buffer[index].key==key:
                return index
        return None

    def add(self,key,value):
        index=self.find_position(key)
        if index!=None:
            self.buffer[index].value=value
        else:
            self.buffer.append(Map_entry(key,value))

    def remove(self,key):
        assert self.contains(key),"This key is not in the map"
        index_to_remove=self.find_position(key)
        self.buffer.pop(index_to_remove)

    def value_of(self,key):
        assert self.contains(key),"This key is not in the map"
        index=self.find_position(key)
        return self.buffer[index].value

    def __iter__(self):
        return self

    def __next__(self):
        if self._ix<len(self.buffer):
            return self.buffer[self._ix]
            self._ix+=1
        else:
            self._ix=0
            raise StopIteration

    def _print(self):
        print(self.buffer)
