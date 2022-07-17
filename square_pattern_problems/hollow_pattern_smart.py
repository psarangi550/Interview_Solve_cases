# n = int(input("Enter the number of rows"))
# for i in range(n):
#     for j in range(n):
#         if i == j or j == 0 or i == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# hollow decresing triangle

# n = int(input("Enter the number of rows"))
# for i in range(n):
#     for j in range(i, n):
#         if i == 0 or j == i or i + j == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input("Enter the number of rows"))
# for i in range(n):
#     for j in range(i, n):
#         if i == 0 or j == i or i + j == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


n = int(input("Enter the number of rows"))
for i in range(n - 1):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i + 1):
        if j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(i):
        if j == (i - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, n):
        if i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(i, n - 1):
        if j == n - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
