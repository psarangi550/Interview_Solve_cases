n=int(input("Enter the number of testcase "))

def foo(n):
    i=0
    while i<n:
        height=0
        cycle=int(input("Enter the number of cycle"))
        for i in range(cycle):
            if i%2 == 0:
                  height+=1  
            else:
                height*=2
        print(height)
        i+=1

foo(n)
