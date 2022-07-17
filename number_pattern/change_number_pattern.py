# n = int(input("Enter the number of rows"))
# for i in range(n):
#     p = 1
#     for j in range(i+1):
#         print(p, end=" ")
#         p += 1
#     print()

# n = int(input("Enter the number of rows"))
# for i in range(n):
#     p = 1
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i, n):
#         print(p, end=" ")
#         p += 1
#     print()

# n = int(input("Enter the number of rows"))
# for i in range(n):
#     p = 1
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i):
#         print(p, end=" ")
#         p += 1
#     for j in range(i+1):
#         print(p, end=" ")
#         p += 1
#     print()


n = int(input("Enter the number of rows"))
for i in range(n-1):
    p = 1
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print(p, end=" ")
        p += 1
    for j in range(i+1):
        print(p, end=" ")
        p += 1
    print()

for i in range(n):
    p = 1
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n-1):
        print(p, end=" ")
        p += 1
    for j in range(i, n):
        print(p, end=" ")
        p += 1
    print()
