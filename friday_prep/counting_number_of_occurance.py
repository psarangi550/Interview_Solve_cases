list1=[-1,0,3,5,9,12]

num=12
count=-1
def foo(list1,num):
    global count
    if len(list1)==1:
        if list1[0]==num:
            count+=1
            print(count)
            return 1
        else:
            # print(count)
            return 0
    else:
        if list1[0]==num:
            count+=1
            print(count)
            return 1+foo(list1[1:],num)
        else:
            count+=1
            return 0+foo(list1[1:],num)

print(foo(list1,num))



# import sys

# print(sys.argv[0])
# print(__file__)
# print(type(sys.argv[1]))


import argparse
parser = argparse.ArgumentParser(description="this function takes args and provide the addition")
parser.add_argument("--num1",type=int,default=10,help="provide a number")
parser.add_argument("--num2",type=int,default=20,help="provide a number")
parser.add_argument("--operation",type=str,default="+",help="provide a operator")

args=parser.parse_args()

def foo():
    if args.operation=="+":
        return (args.num1+args.num2)

print(foo())


