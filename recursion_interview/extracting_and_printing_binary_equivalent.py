import math
# result=""
# def func(str1):
#     global result
#     if len(str1)==0:
#         return func2(int(result))
#     else:
#         if str1[0].isdigit():
#             result+=str1[0]
#     return func(str1[1:])

# output=""
# def func2(num1):
#     global output
#     if num1==0:
#         return output[::-1]
#     else:
#         output+=str(num1%2)
#         num1=(num1//2)
#     return func2(num1)

# print(func2(int(total)))

# total=func("NETSET11OS")
# print(output)


# print(func("NETSET11OS"))


total=""
result=""
def func(str1):
    global total
    global result
    if len(str1)==0:
        return result
    else:
        if str1[-1].isdigit():
            result+=str1[-1]
    return func(str1[:-1])

vector=func("NET1SET2O3S4")
print(vector)

output=""
new_num=0
def getbninary(num):
    global output
    global new_num
    if num==0:
        return output[::-1]
    else:
        new_num=int(num/2)
        output+=str(num%2)
    return getbninary(new_num)


# print(getbninary(10))

for i in vector :
    print(getbninary(int(i)))

