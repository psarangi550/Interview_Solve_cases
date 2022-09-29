# result=[]

# def func(str1):
#     global result
#     if len(str1)==0: return "".join(result)
#     else:
#         result.append(str1[-1])
#     return func(str1[:-1])

# print(func("NETSETOS"))

i=2
output=[]
result=[]
def func(str1):
    global result
    if len(str1)==0:
        return result
    else:
        if str1[0].isdigit():
            result.append(str1[0])
            return DectoBin("".join(result))
    return func(str1[1:])

def DectoBin(str1):
    global i
    global result
    global output
    if int(str1)==0:
        return 
    else:
        output.append(int(str1)%i)
        str1=int(str1)//i
    return DectoBin(str1)


print(func("NET1SET2O3S4"))
DectoBin(9)
print(output)

