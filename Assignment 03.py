# -*- coding: utf-8 -*-
"""
Created on Mon May 18 21:15:13 2020

@author: Dell
"""


#Assignment 03
#Task 01 - 01 pgm - Write a function to compute 5/0 and use try/except to catch the exceptions.

def divide(x,y):
    try : 
        #Floor Divison : Gives only Fractional Part As Answer 
        result = x//y
        print ("Yeah! Your answer is : ",result)
    except ZeroDivisonError:
        print ("Sorry! You are dividing by zero")
 
divide(5,1)  
    
#Task 01 - 02 Pgm - Implement a Python program to generate all sentences where subject is in ["Americans",
#"Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].
 
subject = ["Americans","Indians"]
verb = ["Play","watch"]
obj = ["Baseball","cricket"]



#use list comprehension instead of looping over each of the predicates
sentence_list = [(sub+ " " + vb + " "+ ob ) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
    print(sentence)
    
    
#Task 02 - 01 Pgm -Write a function so that the columns of the output matrix are powers of the input vector.
#The order of the powers is determined by the increasing boolean argument. Specifically, when
#increasing is False, the i-th output column is the input vector raised element-wise to the power
#of N - i - 1.

import numpy as np 

##Iterate over each number in the input vector n times,n being the number of columns in the o/p matrix a nd output
## an intermediate vector.Use diff order formula based on increasing and decreasing condition.
## Reshape the intermediate vector using the size of the input vector(rows) and n  (columns) to generate the o/p matrix

def gen_vander_matrix(ipvector,n,increasing = False):
    if not increasing:
        op_matx = np.array([x**(n-1-i) for x in ipvector for i in range(n)]).reshape(ipvector.size,n)
    elif increasing:
        op_matx = np.array([x**i for x in ipvector for i in range(n)]).reshape(ipvector.size,n)
    
    return op_matx

print("---------------OUTPUT------------------\n")

inputvector = np.array([1,2,3,4,5])
no_col_opmat = 3

op_mat_dec_order = gen_vander_matrix(inputvector,no_col_opmat,False)
op_matx_inc_order = gen_vander_matrix(inputvector,no_col_opmat,True)

print("The input array is:",inputvector,"\n")
print("Number of columns in output matrix should be:",no_col_opmat,"\n")
print("Vander matrix of the input array in decreasing order of powers:\n\n",op_mat_dec_order,"\n")
print("Vander matrix of the input array in increasing order of powers:\n\n",op_matx_inc_order,"\n")


inputvector = np.array([1,2,4,6,8,10])
no_col_opmat = 5 
op_mat_dec_order = gen_vander_matrix(inputvector,no_col_opmat,False)
op_matx_inc_order = gen_vander_matrix(inputvector,no_col_opmat,True)

print("--------------------------------------------------\n")
print("The input array is:",inputvector,"\n")
print("Number of columns in output matrix should be:",no_col_opmat,"\n")
print("Vander matrix of the input array in decreasing order of powers:\n\n",op_mat_dec_order,"\n")
print("Vander matrix of the input array in increasing order of powers:\n\n",op_matx_inc_order,"\n")


   
        
    


