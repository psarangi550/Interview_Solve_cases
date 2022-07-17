n= int(input("Enter the number of rows"))

for i in range(n-1):
    for j in range(i,n):
        print(" " , end=" ")
    for j in range(i):
        print(i+1, end=" ")
    for j in range(i+1):
        print(i+1, end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n-1):
        print(n-i, end=" ")
    for j in range(i,n):
        print(n-i, end=" ")
    
    print()