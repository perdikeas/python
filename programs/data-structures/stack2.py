#!/usr/bin/env python3.7

def generate_buffer(n):
    return [0 for i in range(n)]

class Stack():

    def __init__(self,len):
        self.len=len
        self.buffer=generate_buffer(len)
        self.index=0

    def push(self,value):
        if self.is_full():
            new_list=generate_buffer(2*len(self.buffer))
            for i in range(len(self.buffer)):
                new_list[i]=self.buffer[i]
            self.buffer=new_list

        self.buffer[self.index]=value
        self.index+=1
    def pop(self):
        assert(not self.is_empty()),"Stack is empty"

        rv=self.buffer[self.index-1]
        self.index-=1
        return rv

    def is_full(self):
        if self.index==len(self.buffer):
            return True
        else:
            return False

    def is_empty(self):
        if self.index==0:
            return True
        else:
            return False

stack1=Stack(1)
for i in range(10):
    stack1.push(i)
print(stack1.buffer)
