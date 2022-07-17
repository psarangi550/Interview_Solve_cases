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

n = int(input("Enter the Number of rows"))
for i in range(n):
    for j in range(n):
        if i == n//2 or j == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
