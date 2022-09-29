st1="aaabbbdcaa"

output="a3b3d1c1a1"

def foo(st1):
    count=1
    result=""
    for ele in range(len(st1)-1):
        if st1[ele] == st1[ele+1]:
            count+=1
        else:
            result+=st1[ele]+str(count)
            count=1
    result+=st1[-1]+str(count)
    return result

print(foo(st1))
        
