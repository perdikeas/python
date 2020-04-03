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
        for i in range(1, self.nrows+1):
            for j in range(1, self.ncols+1):
                self.set(i,j, self.get(i, j)+matrixb.get(i,j))

    def _print(self):
        for i in range(self.nrows):
            print("{}\n".format(self.buffer[i]))


#just to check if set_value works, it does!
#random.seed(0)
matrix3=Matrix(2,2)
#matrix3._print()
for i in range(1, matrix3.nrows+1):
    for j in range(1, matrix3.ncols+1):
        r = random.randint(10, 30)
        matrix3.set(i, j, r)

#matrix3._print()

matrix1=Matrix(3,4)
matrix2=Matrix(3,4)

for i in range(1, matrix1.nrows+1):
    for j in range(1, matrix1.ncols+1):
        matrix1.set(i,j,random.randint(10,50))

for i in range(1, matrix2.nrows+1):
    for j in range(1, matrix2.ncols+1):
        matrix2.set(i,j,random.randint(50,100))


matrix1.add(matrix2)
matrix1._print()
