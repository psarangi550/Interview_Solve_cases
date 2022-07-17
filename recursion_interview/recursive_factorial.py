# def fact(num):
#     if num == 0:
#         return 1
#     else:
#         return num * fact(num-1)

#alternate approach 
result=[]
def fact(num):
    if num == 0:
        return result.append(1)
    else:
        result.append(num)
    return fact(num-1)

# print(fact(5))
output=1
fact(5)
for num in result:
    output*=num

print(output)
