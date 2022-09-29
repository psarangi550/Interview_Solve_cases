def foo(start,end):
    result=False
    for i in range(start,end):
        for j in range(2,i):
            if i%j == 0:
                result=False
                break
        else:
            result=True
        if result:
            print(i)

foo(3,20)

# for i in range(2,20):
#     if foo(i):
#         print(i)