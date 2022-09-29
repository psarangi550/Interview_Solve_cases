list1=[205,2670,5008,500,120,30]

def foo(list1):
    digit=""
    result=[]
    for ele in list1:
        temp=ele
        while temp>0:
            if temp%10==0:
                if temp%100!=0:
                    result.append(int(str(temp//10)+str(digit)))
                    break
                else:
                    result.append(int(str(temp//100)+str(digit)))
                    break
            else:
                digit=temp%10
            temp=temp//10
        digit=""
    return result

print(foo(list1))




