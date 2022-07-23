str1="a4b3c2"

result=""
def func(str1):
    global result
    if len(str1)==0:
        return result
    else:
        if str1[0].isdigit():
            result +=result[-1]*int(str1[0])#aaaa
        else:
            result+= str1[0] #a#b
    return func(str1[1:])

# print(func(str1))

#iterative approach 


def func2(str1):
    output=""
    for a in str1:
        if a.isdigit():
            output+=output[-1]*(int(a)-1)
        else:
            output+=a
    return output

# print(func2(str1))



def func3(str1):
    final=""
    if len(str1)==1:
        return 
    else:
        for i in range(len(str1)):
            if str1[i].isdigit():
                final+=final[-1]*(int(str1[i])-1) #aaaaa
            else:
                final+=str1[i] #a#aaaaab
    return final

# print(func3(str1))


#using collections

from collections import Counter
def func4(str1):
    total=""
    c=Counter(str1)
    for key in c:
        if key.isdigit():
            total+=total[-1]*(int(key))
        else:
            total+=key
    return total

print(func4(str1)) 