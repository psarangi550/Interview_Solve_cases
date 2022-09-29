st1="a"
def foo(st1,n):
    count=0
    result=st1
    val=n-len(st1)
    for i in range(n-(len(st1))):
        if len(st1)==n:
            return result
        else:
            if val >len(st1):
                result+=st1
            elif val>0 and val<len(st1):
                result+=st1[val-1]
        val-=len(st1)
    print(result)
    for ele in result:
        if ele=="a":
            count+=1
    print(count)
# foo(st1,10)

#alternate etter siolution
def bar(st1,n):
    output=""
    count=0
    for _ in range(n//(len(st1))):
        output+=st1*1
    output+=st1[n%len(st1)-1]
    for ele in output:
        if ele=="a":
            count+=1
    print(count)
# bar("a",10)

#alternate Solution
def func(st1,n):
    print((st1.count("a")*(n//len(st1)))+(st1[n%len(st1)-1].count("a")))

func("a",10)


