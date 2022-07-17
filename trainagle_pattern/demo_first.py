# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

#alternate approach
# for i in range(5):
#     print((i+1) * "* ")


# n=int(input("Eneter the number of rows"))
# for i in range(n):
#     print((n-(i+1))*" "+(i+1)*"*")


# n=int(input("Eneter the number of rows"))
# for i in range(n):
#     print(i * " "+(n-i)*"*")

n=int(input("Eneter the number of rows"))
for i in range(n):
    print((n-(i+1))*" "+(i+1)*"* "+(n-(i+1))*" ")
for i in range(n):
    print((i)*" "+(n-i)*"* "+(i)*" ")






# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# n=int(input("Enter number of rows "))

# for i in range(n):
#     for j in range(i+1):
#         print(n-j,end=" ")
#     print()


# for i in range(1,n):
#     print((n-i)*" "+((i)*"* "))