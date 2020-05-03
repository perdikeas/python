#!/usr/bin/env python3.7

#two dimensional array implementation or matrix in linear algebra
import random

# utility functions
def mul_list(scalar, alist):
    return [scalar*v for v in alist]

def add_lists(alist, blist):
    assert len(alist)==len(blist)
    return [alist[i]+blist[i] for i in range(len(alist))]

def indx_of_first_nzv(alist):
    for i in range(len(alist)):
        if (alist[i] != 0):
            return i
    return -1

def contains_nzv(alist):
    for v in alist:
        if (v != 0):
            return True
    return False


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
                            , mul_list(scalar
                                       , result.get_row(j)))

        result.set_row(i, newRowI)
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
        return self.non_zero_rows_are_before_zero_rows()

    # finds the index of the first (left-most) NZV
    # on row i - or 0 if the row is all zeros
    def find_indx_of_leftmost_non_zero_value(self, i):
        for j in range(1, self.ncols+1):
            if self.get(i, j)!=0:
                return j
        return 0

    # returns the j-index of the first column that
    # contains a non-zero value - or 0 if no such
    # column exists. NB: ignore rows that are < rowThreshold
    def find_leftmost_col_that_contains_nzv(self, rowThreshold):
        for j in range(1, self.ncols+1):
            # the below works because rowThreshold is indexed according
            # to programmatic conventions here, while it is supplied
            # according to math conventions in the parameter
            if contains_nzv(self.get_col(j)[rowThreshold:]):
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
            if self.row_is_not_all_zeros(i):
                idx_of_current_leftmost_nzv = self.find_indx_of_leftmost_non_zero_value(i)
                assert idx_of_current_leftmost_nzv != 0
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
            if self.row_is_not_all_zeros(i):
                j_indx_of_leftmost1=self.find_indx_of_leftmost_non_zero_value(i)
                assert self.get(i, j_indx_of_leftmost1)==1
                for i2 in range(1, self.nrows+1):
                    if (self.get(i2, j_indx_of_leftmost1)!=0) and (i2 != i):
                        return False
        return True


    def is_reduced_row_echelon_form(self):
        '''
        print ("evaluating whether matrix is in RREF")
        self._print()
        cond1 = self.condition_1_holds()
        print ("condition 1 is {}".format(cond1))
        if not cond1:
            return False
        else:
            cond2 = self.condition_2_holds()
            print ("condition 2 is {}".format(cond2))
            if not cond2:
                return False
            else:
                cond3 = self.condition_3_holds()
                print ("condition 3 is {}".format(cond3))
                return cond3
        '''
        return self.condition_1_holds() and self.condition_2_holds() and self.condition_3_holds()

    # todo use the RREF notation consistently everywhere

    def linesAfterAreAllZero(self, rowToSwapInto):
        for i in range(rowToSwapInto+1, self.nrows+1):
            if self.row_is_not_all_zeros(i):
                return False
        return True

    def do_final_step(self):
        result = self.clone()
        for i in range(result.nrows, 1, -1):
            if result.row_is_all_zeros(i):
                continue
            j = indx_of_first_nzv(result.get_row(i))+1
            v = result.get(i, j)
            assert v == 1
            for k in range(i-1, 0, -1):
                scalar = - result.get(k, j)
                print("\n add row mul by scalar: row-{} <- {}*row-{}".format(k, scalar, i))
                result = result.add_rows(k, scalar, i)
                result._print()
        return result
                
            

    def gauss_elim(self):
        result = self.clone()
        rowToSwapInto = 1
        while rowToSwapInto <= result.nrows:
            print (Color.CYAN+Color.BOLD+"\nstarting next loop"+Color.END)
            result._print()
            # if we are swaping into row <rowToSwapInto> than we ignore rows below that number
            j = result.find_leftmost_col_that_contains_nzv(rowToSwapInto-1)
            full_col = result.get_col(j)
            truncated_col = full_col[(rowToSwapInto-1):]
            idx_of_row_containing_fst_nzv = indx_of_first_nzv(full_col)+rowToSwapInto
            # idx = 1
            print("LM col with NZV = {}, full col is {}, fst row containing NZV is {}".format(j, full_col, idx_of_row_containing_fst_nzv))

            assert idx_of_row_containing_fst_nzv != -1
            if idx_of_row_containing_fst_nzv != rowToSwapInto:
                print(Color.BOLD+Color.RED+"\nswap row operation {} <-> {}".format(rowToSwapInto, idx_of_row_containing_fst_nzv)+Color.END)
                result = result.swap_rows(rowToSwapInto, idx_of_row_containing_fst_nzv)
                result._print()
            val = result.get(rowToSwapInto, j)
            assert val != 0
            if (val != 1):
                scalar = 1/val
                print(Color.BOLD+Color.RED+"\nrow scalar mul: {} * row {}".format(scalar, rowToSwapInto)+Color.END)
                result = result.mul_row_by_scalar(rowToSwapInto, scalar)
                result._print()

            for i in range(rowToSwapInto+1, result.nrows+1):
                val_i = result.get(i, j)
                print("M[{}, {}]={}".format(i, j, val_i))
                if (val_i != 0):
                    scalar = -val_i
                    print("\n add row mul by scalar: row-{} <- {}*row-{}".format(i, scalar, rowToSwapInto))
                    result = result.add_rows(i, scalar, rowToSwapInto)
                    result._print()
            if result.linesAfterAreAllZero(rowToSwapInto):
                break
            else:
                rowToSwapInto += 1

        result = result.do_final_step()
        print (Color.BOLD+Color.CYAN+"the shit is ready"+Color.END)
        assert result.is_reduced_row_echelon_form()
        return result



    def _print(self, color=Color.YELLOW):
        for i in range(self.nrows):
            print("{}{}{}".format(color, self.buffer[i], Color.END))


matrix1 = Matrix.createNew([ [0, 0, -2, 0, 7],
                             [2, 4, -10, 6, 12],
                             [2, 4, -5, 6, -5]])
matrix1.gauss_elim()

matrix2 = Matrix.createNew([[2, 3, -4], [3, -1, 2], [5, 6, 8]])
matrix2.gauss_elim()

matrix3 = Matrix.createNew([[1, 2, -2, 1], [3, -3, 1, 0], [2, -8, 3, -2]])
matrix3.gauss_elim()

matrix4 = Matrix.createNew([[3, 5, -8], [2, 1, -1], [5, 2, 3], [-1, 1, 1]])
matrix4.gauss_elim()

matrix5 = Matrix.createNew([[0, 1, 2, 2], [1, 1, 2, 3], [2, 2, 2, 3], [2, 3, 3, 3]])
matrix5.gauss_elim()
