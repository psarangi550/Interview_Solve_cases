list1=[1,6,7,12,13,18,19]
target=37


def foo():
    i=0
    count_odd=0
    count_even=-1
    result=[]
    while True:
        if i%2==0:
            count_even+=1
            val=6*count_even+1
            if val==37:
                print(i)
                break
            else:
                result.append(val)
        else:
            count_odd+=1
            val=6*count_odd
            if val==37:
                print(i)
                break
            else:
                result.append(val)
        i+=1
    return result

print(foo())