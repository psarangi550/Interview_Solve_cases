# n = int(input("Enter the Number of rows"))

# for i in range(n):
#     p = n
#     for j in range(i+1):
#         print(p, end=" ")
#         p -= 1
#     print()

# n = int(input("Enter the Number of rows"))

# # for i in range(n):
# #     p = n
# #     for j in range(i+1):
# #         print(" ", end=" ")
# #     for j in range(i, n):
# #         print(p, end=" ")
#         p -= 1
#     print()


# n = int(input("Enter the Number of rows"))

# for i in range(n):
#     p = n-i
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i, n):
#         print(p, end=" ")
#         p -= 1
#     print()


# alternate better approach
# n = int(input("Enter the Number of rows"))
# q = n
# for i in range(n):
#     p = q
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i, n):
#         print(p, end=" ")
#         p -= 1
#     q -= 1
#     print()

# n = int(input("Enter the Number of rows"))
# q = 0
# for i in range(n):
#     k = 1
#     p = q
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print(k, end=" ")
#         k += 1
#     for j in range(i):
#         print(p, end=" ")
#         p -= 1
#     q += 1
#     print()


# alternate approach
n = int(input("Enter the Number of rows"))
for i in range(n):
    k = 1
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print(k, end=" ")
        k += 1
    for j in range(i+1):
        print(k, end=" ")
        k -= 1
    print()
