
# for i in range(5):
#     val=1
#     for j in range(i,5):
#         print(" ",end=" ")
#     for j in range(i):
#         print(val,end=" ")
#     for j in range(i+1):
#         print(val,end=" ")
    
#     val+=1
#     print()


#pascal_triangle

for i in range(5):
    val=1
    for j in range(i,5):
        print(" ",end=" ")
    for j in range(i):
        if j<i:
            if j==0:
                print(1,end=" ")
            else:
                print(((i-1)*j+(i-1)*(j-1)),end=" ")
        if j==i:
            print(1,end=" ")
    for j in range(i+1):
        if j<i:
            if j==0:
                print(1,end=" ")
            else:
                print(((i-1)*j+(i-1)*(j-1)),end=" ")
        if j==i:
            print(1,end=" ")
    print()


