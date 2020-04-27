#!/usr/bin/env python3.7

#two dimensional array implementation or matrix in linear algebra
import random


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Matrix():
    def __init__(self, nrows, ncols):
        self.buffer=list()
        self.nrows = nrows
        self.ncols = ncols
        self.buffer = [ [0 for j in range(ncols)] for i in range(nrows)]



    def set(self, i, j, v):
        self.buffer[i-1][j-1]=v



    def get(self, i, j):
        return self.buffer[i-1][j-1]



    def add(self,matrixb):
        assert matrixb.nrows==self.nrows
        assert matrixb.ncols==self.ncols
        new_list=Matrix(self.nrows,self.ncols)
        for i in range(1, self.nrows+1):
            for j in range(1, self.ncols+1):
                new_list.set(i,j, self.get(i, j)+matrixb.get(i,j))



    def scalar_mul(self,scalar):
        new_list=Matrix(self.nrows,self.ncols)
        for i in range(1,self.nrows+1):
            for j in range(1,self.ncols+1):
                new_list.set(i,j,self.get(i,j)*scalar)

    def mul(self, matrixb):
        assert self.ncols==matrixb.nrows
        rv=Matrix(self.nrows, matrixb.ncols)
        for i in range(1, self.nrows+1):
            for j in range(1, matrixb.ncols+1):
                v_ij = sum([self.get(i,k)*matrixb.get(k,j) for k in range(1, self.ncols+1)])
                rv.set(i, j, v_ij)
        return rv


    def gaus_elim_algorithm(self):
        pass


    def reduced_matrix(self,i,j):
        self.buffer.pop(i-1)
        for row in range(self.nrows):
            self.buffer[row].pop(j-1)

    def find_determinant(self):
        if self.nrows==2 and self.ncols==2:
            rv=self.get(1,1)*self.get(2,2)-self.get(1,2)*self.get(2,1)
        else:
            rv=0
            i=random.randint(1,self.nrows+1)
            for j in range(1,self.ncols+1):
                rv+=self.get(i,j)*find_determinant(self.reduced_matrix,i,j)
        return rv


    def swap_rows(self,row1,row2):
        row_to_swap=self.buffer[row1-1]
        self.buffer[row1-1]=self.buffer[row2-1]
        self.buffer[row2-1]=row_to_swap


    def multiply_row_by_scalar(self,row,scalar):
        for index in range(len(self.buffer[row-1])):
            self.set(row,index,self.get(row,index)*scalar)

    def add_rows(self,row1,row2,scalar):
        for index in range(1,self.ncols+1):
            self.set(row1,index,self.get(row1,index)+self.get(row2,index)*scalar)


    def _print(self):
        for i in range(self.nrows):
            print("{}\n".format(self.buffer[i]))
