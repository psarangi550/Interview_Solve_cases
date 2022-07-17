# final=""
# import math
# def func(num):
#     global final
#     if num==0:
#         return final[::-1]
#     else:
#         final+=str(num%2)
#         num=(math.floor(num//2))
#     return func(num)


# final=""
import math
def func(num):
    global final
    if num==0:
        return 
    else:
        print(str(num%2),end=" ")
        num=(math.floor(num//2))
    return func(num)

func(2)

