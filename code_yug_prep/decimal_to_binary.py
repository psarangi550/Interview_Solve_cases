from functools import reduce

result=[]
def foo(num):
    global result
    if num==0:
        return reduce(lambda x,y:str(x)+str(y),result)
    else:
        digit=num%2
        result.append(digit)
        num=num//2
        return foo(num)
print(foo(9))
