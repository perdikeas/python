#!/usr/bin/env python3.7
import math

def contains_nzv(list):
    for i in list:
        if i!=0:
            return True
    return False

def idx_of_fst_nzv(list):
    for i in range(len(list)):
        if list[i]!=0:
            return i+1
    return 0


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

    def __init__(self,nrows,ncols):
        self.nrows=nrows
        self.ncols=ncols
        self.buffer=[[0 for i in range(ncols)] for j in range(nrows)]

    def create_new(rows):
        result=Matrix(len(rows),len(rows[0]))
        for i in range(1,result.nrows+1):
            for j in range(1,result.ncols+1):
                result.set(i,j,rows[i-1][j-1])
        return result

    def get(self,i,j):
        return self.buffer[i-1][j-1]

    def set(self,i,j,value):
        self.buffer[i-1][j-1]=value

    def clone(self):
        return Matrix.create_new(self.buffer)

    def add(self,matrix2):
        assert self.nrows==matrix2.nrows
        assert self.ncols==matrix2.ncols
        return Matrix.create_new([[self.get(i,j)+matrix2.get(i,j) for j in range(1,self.ncols+1)] for i in range(1,self.nrows+1)])


    def scalar_mul(self,v):
        return Matrix.create_new([[v*self.get(i,j) for j in range(1,self.ncols+1)] for i in range(1,self.nrows+1)])

    def mul(self,matrix2):
        assert self.ncols==matrix2.nrows
        result=Matrix(self.nrows,matrix2.ncols)
        for i in range(1,result.nrows+1):
            for j in range(1,result.ncols+1):
                result.set(i,j,sum([self.get(i,k)*matrix2.get(k,j) for k in range(1,self.ncols+1)]))
        return result

    def contains(self,element):
        for i in range(1,self.nrows+1):
            for j in range(1,self.ncols+1):
                if element==self.get(i,j):
                    return True
        return False

    def remove_row(self,i):
        result=self.clone()
        result.buffer.pop(i-1)
        result.nrows-=1
        return result

    def remove_col(self, j):
        result=Matrix(self.nrows,self.ncols-1)


        for i in range(1,result.nrows+1):
            for j2 in range(1,result.ncols+1):
                if j2 >= j:
                    result.set(i,j,self.get(i,j+1))
                else:
                    result.set(i,j,self.get(i,j))
        result.nrows-=1
        return result




    def minor(self,i,j):
        result=self.remove_col(j)
        result=result.remove_row(i)
        return result



    def algebraic_complement(self,i,j):
        result=math.pow(-1,i+j)*(self.minor(i,j).find_determinant())
        return result


    def find_determinant(self):
        assert self.nrows==self.ncols
        if self.nrows==1:
            result=self.get(1,1)
        elif self.nrows==2:
            result=self.get(1,1)*self.get(2,2)-self.get(2,1)*self.get(1,2)
        else:
            result=sum([self.get(1,j)*self.algebraic_complement(1,j) for j in range(1,self.ncols+1)])
        return result

    def adjacent(self):
        return Matrix.create_new([[self.algebraic_complement(i,j) for j in range(1,self.ncols+1)] for i in range(1,self.nrows+1)])

    def find_inverse(self):
        result=self.adjacent().scalar_mul(1/self.find_determinant())
        return result

    #utility functions for the gauss elimination algorithm
    def get_row(self,i):
        return self.buffer[i-1]

    def get_col(self,j):
        return [self.get(i,j) for i in range(1,self.nrows+1)]

    def is_row_all_zeros(self,i):
        for v in self.get_row(i):
            if v!=0:
                return False
        return True

    def is_not_row_all_zeros(self,i):
        for v in self.get_row(i):
            if v!=0:
                return True
        return False

    def is_col_all_zeros(self,j):
        for v in self.get_col(j):
            if v!=0:
                return False
        return True

    def is_not_col_all_zeros(self,j):
        for v in self.get_col(j):
            if v!=0:
                return True
        return False

    def is_matrix_all_zeros(self):
        for i in range(1,self.nrows+1):
            if not self.is_row_all_zeros(i):
                return False
        return True


    def get_idx_of_leftmost_nzv_in_row(self,i):
        for j in range(1,self.ncols+1):
            if self.get(i,j)!=0:
                return j
        return 0

    def get_idx_of_first_nzv_in_col(self,j):
        for i in range(1,self.ncols+1):
            if self.get(i,j)!=0:
                return i
        return 0

    def non_zero_rows_are_before_zero_rows(self):
        zero_row_encountered=False
        for i in range(1,self.nrows+1):
            if self.is_row_all_zeros(i):
                zero_row_encountered=True
            if zero_row_encountered and not self.is_row_all_zeros(i):
                return False
        return True

    def is_only_nzv_in_col(self,i,j):
        for v in self.get_col(j):
            if v!=self.get(i,j) and v!=0:
                return False
        return True

    def swap_rows(self,i1,i2):
        result=self.clone()
        tmp=result.get_row(i1)
        result.buffer[i1-1]=result.get_row(i2)
        result.buffer[i2-1]=tmp
        return result

    def add_row_mul_by_scalar(self,i1,i2,v):
        result=self.clone()
        result.buffer[i1-1]=[result.get(i1,j)+v*result.get(i2,j) for j in range(1,self.ncols+1)]
        return result

    def mul_row_by_scalar(self,i,v):
        result=self.clone()
        result.buffer[i-1]=[v*element for element in result.get_row(i)]
        return result

    def rows_after_are_all_zeros(self,row_threshold):
        for i in range(row_threshold+1,self.nrows+1):
            if self.is_not_row_all_zeros(i):
                return False
        return True

    def gauss_elim_final_step(self):
        result=self.clone()
        for i in range(1,result.nrows+1):
            idx_of_leftmost_nzv=result.get_idx_of_leftmost_nzv_in_row(i)
            for _i in range(1,i):
                v=-1*result.get(i,idx_of_leftmost_nzv)
                result=result.add_row_mul_by_scalar(i,1,v)
        return result



    #this is the form in which the matrix is transformed through the gauss elimination algorithm
    #row-echelon-form
    def is_in_reduced_row_echelon_form(self):
        return self.condition_1_holds() and self.condition_2_holds() and self.condition_3_holds()


    #all the condition functions below refer to one of the conditions that must be true in order for a matrix to be in row echelon form
    def condition_1_holds(self):
        return self.non_zero_rows_are_before_zero_rows()

    def condition_2_holds(self):
        idx_of_previous_leftmost_nzv=0
        for i in range(1,self.nrows+1):
            if not self.is_row_all_zeros(i):
                idx_of_current_leftmost_nzv=self.get_idx_of_leftmost_nzv_in_row(i)
                if self.get(i,idx_of_current_leftmost_nzv)!=1:
                    return False
                else:
                    if idx_of_current_leftmost_nzv<=idx_of_previous_leftmost_nzv:
                        return False
                    else:
                        idx_of_previous_leftmost_nzv=idx_of_current_leftmost_nzv
        return True

    def condition_3_holds(self):
        for i in range(1,self.nrows+1):
            leftmost_nzv_idx=self.get_idx_of_leftmost_nzv_in_row(i)
            if not self.is_only_nzv_in_col(i,leftmost_nzv_idx):
                return False
        return True


    def gauss_elim(self):
        result=self.clone()
        if result.is_matrix_all_zeros():
            return result

        while not result.is_in_reduced_row_echelon_form():
            row_to_swap_into=1
            for j in range(1,self.ncols+1):
                colj=result.get_col(j)[row_to_swap_into-1:]
                if contains_nzv(colj):
                    idx_of_leftmost_col_that_contains_nzv=j
                    idx_of_fst_row_that_contains_nzv=idx_of_fst_nzv(colj)+row_to_swap_into-1

                    result=result.swap_rows(idx_of_fst_row_that_contains_nzv,row_to_swap_into)
                    print(Color.RED+Color.BOLD+'Swapping rows {}<-->{}'.format(idx_of_fst_row_that_contains_nzv,row_to_swap_into))
                    result._print()

                    scalar=1/self.get(row_to_swap_into,idx_of_leftmost_col_that_contains_nzv)
                    result=result.mul_row_by_scalar(row_to_swap_into,scalar)
                    print('row {}--> row{} * {}'.format(row_to_swap_into,row_to_swap_into,scalar))
                    result._print()

                    for i in range(row_to_swap_into+1,self.nrows+1):
                        v=-1*self.get(i,idx_of_leftmost_col_that_contains_nzv)
                        result=result.add_row_mul_by_scalar(i,row_to_swap_into,v)
                        print('row {} --> row {} + {}* row {}'.format(i,i,v,row_to_swap_into))

                    if result.rows_after_are_all_zeros(row_to_swap_into):
                        result.gauss_elim_final_step()
                    else:
                        row_to_swap_into+=1

            result.gauss_elim_final_step()

        return result


    def _print(self):
        for element in self.buffer:
            print(element)

matrix1=Matrix.create_new([[1,2,3],[-7,9,0],[1,0,0]])
matrix1.gauss_elim()._print()
