from itertools import cycle
str1="abcac"
def foo(str1,n):
    val=0
    result = str1
    iter_cycle=cycle(result)
    for i in iter_cycle:
        if val==(n-len(str1)):
            break
        else:
            result+=i
        val+=1
    print(result)
    count=0
    for ele in result:
        if ele=="a":
            count+=1
    print(count)

foo(str1,10)

