#!/usr/bin/env python3.7

#two dimensional array implementation or matrix in linear algebra
import random

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


    def _print(self):
        for i in range(self.nrows):
            print("{}\n".format(self.buffer[i]))

matrix1=Matrix(2,2)
for i in range(matrix1.nrows):
    for j in range(matrix1.ncols):
        matrix1.set(i,j,random.randint(10,20))

matrix1._print()
matrix1.scalar_mul(2)
matrix1._print()
