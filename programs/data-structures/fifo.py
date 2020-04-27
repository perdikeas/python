#!/usr/bin/env python3.7

# os
def os_malloc(n):
    return [None for i in range(n)]


# library implementation
class Queue():
    def __init__(self,len):
        self.list=os_malloc(len)
        self.front = 0
        self.back = 0

    def is_empty(self):
        return self.front==self.back

    def is_full(self):
        return self.back-self.front == len(self.list)


    def push(self,value):
        if self.is_full():
            new_list=os_malloc(2*len(self.list))
            for x in range(len(self.list)):
                new_list[x]=self.list[x]
            self.list=new_list

        self.list[self.back % len(self.list)]=value
        self.back += 1

    def pop(self):
        if self.is_empty():
            raise Exception('queue is empty')
        rv = self.list[self.front % len(self.list)]
        self.front += 1
        return rv


# client programmer
q=Queue(1)
for i in range(10):
    q.push(i**2)
for i in range(4):
    print(q.pop())
