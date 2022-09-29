# def foo(num1,num2):
#     if num2 ==0:
#         return num1
#     else:
#         return foo(num2,num1%num2)

# print(foo(8,12))

i=2   
result=[]
def foo(num1,num2):
    global i
    global result
    if num1>num2:
        if i>num2:
            return max(result)
    if num2>num1:
        if i>num1:
            return max(result)
    
    if num1%i==0 and num2%i==0:
        result.append(i)
    i+=1
    return foo(num1,num2)

print(foo(8,12))




