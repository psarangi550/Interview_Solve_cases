# Give a list of Coins and value x , find minimum number of coins that sum up to x
from itertools import permutations

IN=[1,2,5,10,20,50] 
x = 65
OUT=3 
ans=(50+10+5)

# IN=[1,5,6,9]
# x=11
# OUT=2 
# ans=(6+5)

def foo(IN,n):
    result=[]
    for i in range(1,len(IN)-1):
        val=list(permutations(IN,i))
        for ele in val:
            if sum(ele)==n:
                result.append(len(ele))
    return max(result)

# print(foo(IN,11))
print(foo(IN,65))







# for item in permutations(IN,2):
#     print(item)