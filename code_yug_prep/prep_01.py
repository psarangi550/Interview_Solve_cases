#clock implementation
def foo(num1,num2):
    temp=num2
    count=0
    while temp>0:
        if temp%num1==0:
            count+=1
        temp=temp//num1
    return count


print(foo(2,512))