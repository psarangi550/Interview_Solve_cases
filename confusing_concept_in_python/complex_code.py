from functools import reduce
from operator import mul
list1=[1,2,3,4]
def foo(list1):
    mul_num=None
    out=[]
    for ele in list1:
        result=[1,2,3,4]
        result.remove(ele)
        # mul_num=mul(result)
        mul_num=reduce(mul,result)
        out.append(mul_num)
    return out

print(foo(list1))