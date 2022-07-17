# result=""
# def func(str1):
#     global result
#     size=len(str1)
#     if size==0:
#         return result[::-1]
#     if str1[0].isdigit():
#         result+=str(str1[0])
#     return func(str1[1:])


# print(func("NET1SET2O3S4"))

#alternate approach 
result=""
output=""
def func(str1):
    global result
    global output
    if len(str1)==0:
        return output
    else:
        result+=str1[-1]
        if str1[-1].isdigit():
            output+=str1[-1]
    return func(str1[:-1])

print(func("NET1SET2O3S4"))



