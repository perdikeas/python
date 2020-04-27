#!/usr/bin/env python3.7

def generate_buffer(n):
    return [0 for i in range(n)]

class Queue():

    def __init__(self,len):
        self.buffer=generate_buffer(len)
        self.front=0
        self.rear=0

    def is_full(self):

        if self.rear-self.front==len(self.buffer):
            return True
        else:
            return False

    def is_empty(self):

        if self.front==self.rear:
            return True
        else:
            return False

    def push(self,value):

        if self.is_full():
            new_list=generate_buffer(2*len(self.buffer))
            for i in range(len(self.buffer)):
                new_list[i]=self.buffer[i]
            self.buffer=new_list

        self.buffer[self.rear%len(self.buffer)]=value
        self.rear+=1

    def pop(self):
        assert(not self.is_empty()),"Queue is empty"

        
        rv=self.buffer[self.front]
        self.front+=1
        return rv

    def peak_rear(self):
        assert(not self.is_empty()),"Queue is empty"
        return self.rear

    def peak_front(self):
        assert(not self.is_empty()),"Queue is empty"
        return self.front

queue1=Queue(1)
for i in range(5):
    queue1.push(i)
for i in range(5):
    print(queue1.pop())
