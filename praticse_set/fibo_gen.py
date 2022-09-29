# def func(n):
#     i=0
#     a,b=0,1
#     while i<n:
#         c=a+b
#         yield a
#         a=b
#         b=c
#         i+=1

# for i in func(5):
#     print(i,end=" ")

val=5
for i in range(5):
    for j in range(i+1):
        print(val,end=" ")
    print()