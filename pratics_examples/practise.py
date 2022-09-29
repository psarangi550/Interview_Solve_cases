
def foo(num):
    if num ==0:
        return 0
    if num ==1:
        return 1
    else:
        return foo(num-1)+foo(num-2)

# print(foo(10))
for i in range(11):
    print(foo(i),end=" ")


#using the generators

def func(num):
    a=0
    b=1
    i=0
    while i < num:
        c=a+b
        yield a
        a=b
        b=c
        i+=1

for i in func(10):
    print(i)