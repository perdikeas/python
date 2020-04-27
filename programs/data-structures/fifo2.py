#!/usr/bin/env python3.7

def os_malloc(n):
    return [0 for i in range(n)]

class Queue():

    def __init__(self,len):
        self.list=os_malloc(len)
        self.front=0
        self.rear=0

    def is_full(self):
        return self.rear-self.front==len(self.list)

    def is_empty(self):
        return self.rear==self.front

    def push(self,value):
        if self.rear==len(self.list):
            new_list=os_malloc(2*len(self.list))
            for i in range(len(self.list)):
                new_list[i]=self.list[i]
            self.list=new_list
        self.list[self.rear%len(self.list)]=value
        self.rear+=1

    def pop(self):
        if self.front-self.rear==0:
            raise Exception('queue is empty')


        value_to_pop=self.list[self.front]
        self.front+=1
        return value_to_pop

q=Queue(2)
for i in range(10):
    q.push(i**2)
for i in range(10):
    print(q.pop())
print(q.is_empty())
