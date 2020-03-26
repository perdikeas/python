#!/usr/bin/env python3

class Stack():
    def __init__(self, N):
        self.N=N
        self.container=['not a value' for i in range(self.N)]
        self.slotForNextInsert = 0
    def isFull(self):
        return self.slotForNextInsert==self.N
    def isEmpty(self):
        return self.slotForNextInsert==0
    def push(self, v):
        if self.isFull():
            raise Exception('stack overflow')
#        if self.slotForNextInsert>=self.N:
 #           self.container+=[None for i in range(self.N)]
        self.container[self.slotForNextInsert] = v
        self.slotForNextInsert += 1
    def peek(self):
        if self.isEmpty():
            raise Exception('stack is empty')
        else:
            return self.container[self.slotForNextInsert-1]
    def pop(self):
        if self.isEmpty():
            raise Exception('stack is empty')
        else:
            valueToReturn = self.container[self.slotForNextInsert-1]
            self.slotForNextInsert-=1
            return valueToReturn

s1 = Stack(10)

i = 0
while not s1.isFull():
    s1.push(i)
    i += 1

while not s1.isEmpty():
    print ( s1.pop())


if False:
    initial_len=10
    stack1=Stack(initial_len)
    i=0
    for i in range(50):
        stack1.push(i)
    for i in range(3):
        stack1.pop()
    print(stack1)
