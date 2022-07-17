# here we are using the number pattern along with the number
# n = int(input("Enter the number of rows"))
# for i in range(n):
#     for j in range(i+1):
#         if i % 2 == 0:
#             print("1", end=" ")
#         else:
#             print("2", end=" ")
#     print()

# using the dimond pattern for with the increasing number
# n = int(input("Enter the number of rows"))
# p = 1
# q = 5
# for i in range(n-1):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i):
#         print(p, end=" ")
#     for i in range(i+1):
#         print(p, end=" ")
#     p += 1
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i, n-1):
#         print(q, end=" ")
#     for j in range(i, n):
#         print(q, end=" ")
#     q += 1
#     print()

# here we are using the decreasing value for the test
n = int(input("Enter the number of rows"))
p = 1
for i in range(n-1):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print(p, end=" ")
    for i in range(i+1):
        print(p, end=" ")
    p += 1
    print()

for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n-1):
        print(p, end=" ")
    for j in range(i, n):
        print(p, end=" ")
    p -= 1
    print()
