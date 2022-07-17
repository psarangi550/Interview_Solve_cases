# n = int(input("Enter the number of rows"))
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()


# n = int(input("Enter the number of rows"))
# for i in range(n):
#     for j in range(n):
#         if j == 0 or j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input("Enter the number of rows"))
# for i in range(n):
#     for j in range(n):
#         if i == j or i+j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input("Enter the Number of rows"))
# for i in range(n):
#     for j in range(n):
#         if i == n//2 or j == n//2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input("Enter the Number of rows"))
# for i in range(n):
#     for j in range(n):
#         if i == n-1 or j == 0 or i == j:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# n = int(input("Enter the Number of rows"))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i + j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input("Enter the Number of rows"))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n - 1 or j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# hollow triangle pattern

# n = int(input("Enter the number of rows"))

# for i in range(n):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i):
#         if j == 0 or i == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(i + 1):
#         if i == n - 1 or i == j:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# n = int(input("Enter the number of rows"))

# for i in range(n - 1):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i):
#         if j == 0 or i == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(i + 1):
#         if i == n - 1 or i == j:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# for i in range(n):
#     for j in range(i + 1):
#         print(" ", end=" ")
#     for j in range(i, n - 1):
#         if i == j:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(i, n):
#         if (j == 0 and i > 0) or j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# alternate ways
