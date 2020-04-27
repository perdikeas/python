#!/usr/bin/env python3


########################
# OS API (Application Programming Interface)

def os_malloc(n):
    return [None for i in range(n)]
        

########################
# library implementation


class Stack():

    def __init__(self, initial_len):
        self.list=os_malloc(initial_len)
        self.current_index=0

    def push(self,value):
        if self.current_index==len(self.list):
            new_list = os_malloc(2*len(self.list))
            print('copying {} elements'.format(len(self.list)))
            for i in range(len(self.list)):
                new_list[i]=self.list[i]
            self.list = new_list

        assert self.current_index < len(self.list)
        self.list[self.current_index]=value
        print('wrote value {} in array pos {}'.format(value, self.current_index))
        self.current_index+=1

    def pop(self):

        if self.current_index==0:
            raise Exception('stack is empty')
        else:
            index_to_pop=self.current_index-1
            self.current_index-=1
            return self.list[index_to_pop]

########################
# client coder

stack=Stack(10)
for i in ['v{}'.format(i) for i in range(20)]:
    stack.push(i)

for i in range(20):
    print(stack.pop())
    
