# Given an integer array A ( below example )
# Write a function which takes integer array A as an input parameter and returns the integer from this function based on the below condition 
# Output => return an integer which is smallest +ve no > 0 and not present in A 

# Sample Examples : 

# import functools


from functools import reduce

A= [1,3,6,4,1,2]
# A =[-1,-3]
# A = [1,2,3] 

num_list=[x for x in range(1,len(A)+1)]
def foo(list1):
    count=0
    for ele in num_list:
        count+=1
        if ele not in list1:
            print(ele)
            break
    else:
        print(count+1)


foo(A)
