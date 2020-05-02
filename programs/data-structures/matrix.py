#!/usr/bin/env python3.7

#two dimensional array implementation or matrix in linear algebra
import random

# utility functions
def mul_list(scalar, alist):
    return [scalar*v for v in alist]

def add_lists(alist, blist):
    assert len(alist)==len(blist)
    return [alist[i]+blist[i] for i in range(len(alist))]

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
        self.nrows = nrows
        self.ncols = ncols
        self.buffer = [ [0 for j in range(ncols)] for i in range(nrows)]

        
    def createNew(rows): # rows is a list of lists
        nrows = len(rows)
        ncols = len(rows[0])
        for i in range(0, len(rows)):
            if len(rows[i]) != ncols:
                raise Exception("row {} has {} elements - all rows must have {} elements".format(i+1, len(rows[i]), ncols))
        result = Matrix(nrows, ncols)
        for i in range(0, nrows):
            for j in range(0, ncols):
                result.set(i+1, j+1, rows[i][j])
        return result


    def set(self, i, j, v):
        self.buffer[i-1][j-1]=v

    def get(self, i, j):
        return self.buffer[i-1][j-1]

    def add(self,matrixb):
        assert matrixb.nrows==self.nrows
        assert matrixb.ncols==self.ncols
        result  = Matrix(self.nrows,self.ncols)
        for i in range(1, self.nrows+1):
            for j in range(1, self.ncols+1):
                result.set(i, j, self.get(i, j)+matrixb.get(i, j))
        return result


    def scalar_mul(self, scalar):
        result=Matrix(self.nrows, self.ncols)
        for i in range(1, self.nrows+1):
            for j in range(1, self.ncols+1):
                result.set(i, j, scalar*self.get(i,j))
        return result

    def mul(self, matrixb):
        assert self.ncols==matrixb.nrows
        result=Matrix(self.nrows, matrixb.ncols)
        for i in range(1, self.nrows+1):
            for j in range(1, matrixb.ncols+1):
                v_ij = sum([self.get(i,k)*matrixb.get(k,j) for k in range(1, self.ncols+1)])
                result.set(i, j, v_ij)
        return result

    # useful, low-level methods for Gauss elimination

    def get_row(self, i):
        return self.buffer[i-1]

    def set_row(self, i, row):
        self.buffer[i-1] = row

    def get_col(self, j):
        return [self.get(i, j) for i in range(1, self.nrows+1)]


    def clone(self):
        result = Matrix(self.nrows, self.ncols)
        for i in range(1, self.nrows+1):
            for j in range(1, self.ncols+1):
                result.set(i, j, self.get(i, j))
        return result

    def swap_rows(self, i, j):
        result = self.clone()
        result.set_row(i, self.get_row(j))
        result.set_row(j, self.get_row(i))
        return result



    def mul_row_by_scalar(self, i, scalar):
        result = self.clone()
        result.set_row(i, mul_list(scalar, self.get_row(i)))
        return result

    # row_i becomes row_i + scalar*row_j
    def add_rows(self, i, scalar, j):
        result=self.clone()
        newRowI = add_lists(result.get_row(i)
                            , mul_list(result.get_row(j)
                                       , scalar))
        result.setRow(i, newRowI)
        return result


    def col_contains_non_zero_value(self, j):
        for i in range(1, self.nrows+1):
            if self.get(i, j)!=0:
                return True
        return False

    def row_is_all_zeros(self, i):
        return not self.row_is_not_all_zeros(i)

    def row_is_not_all_zeros(self, i):
        for j in range(1, self.ncols+1):
            if self.get(i, j)!=0:
                return True
        return False

    # returns True if all rows containing at least one non-zero
    # value appear before rows containing all zero values
    def non_zero_rows_are_before_zero_rows(self):
        encountered_all_zero_row = False
        for i in range(1, self.nrows+1):
            if self.row_is_all_zeros(i):
                encountered_all_zero_row = True
            else: # not all zeros row
                if encountered_all_zero_row:
                    return False
        return True

    def condition_1_holds(self):
        return non_zero_rows_are_before_zero_rows(self)

    # finds the index of the first (left-most) NZV
    # on row i
    def find_indx_of_leftmost_non_zero_value(self, i):
        for j in range(1, self.ncols+1):
            if self.get(i, j)!=0:
                return j
        return 0


    # Condition 2 is:
    #     The left-most non-zero element on each non-zero row
    #     has the value of 1 and is to the right of the corresponding
    #     1 of the previous row
    def condition_2_holds(self):
        # nzv: non-zero-value
        idx_of_previous_leftmost_nzv = 0
        for i in range(1, self.nrows+1):
            idx_of_current_leftmost_nzv = self.find_indx_of_leftmost_non_zero_value(i)
            assert idx_of_current_leftmost_nzv>=1
            if self.get(i, idx_of_current_leftmost_nzv)!=1:
                return False
            else:
                if idx_of_previous_leftmost_nzv>=idx_of_current_leftmost_nzv:
                    return False
            idx_of_previous_leftmost_nzv = idx_of_current_leftmost_nzv
        return True

    # Condition 3 is:
    #    The leftmost 1 of each line is the only nzv of the column in which it belongs

    def condition_3_holds(self):
        for i in range(1, self.nrows+1):
            j_indx_of_leftmost1=self.find_indx_of_leftmost_non_zero_value(i)
            assert self.get(i, indx_of_leftmost1)==1
            for i2 in range(1, self.nrows+1):
                if (self.get(i2, j_indx_of_leftmost1)!=0) and (i2 != i):
                    return False
        return True


    def is_reduced_row_echelon_form(self):
        return self.condition_1_holds() and self.condition_2_holds() and self.condition_3_holds()

    def gauss_elim(self):
        result = self.clone()
        while not self.is_reduced_row_echelon_form():
            pass # todo...
        return result
            


    def _print(self):
        for i in range(self.nrows):
            print("{}".format(self.buffer[i]))


matrix1 = Matrix.createNew([ [1, 2], [3, 4] ])


matrix1._print()


matrix1.set_row(1, [42, 43])
matrix1._print()


