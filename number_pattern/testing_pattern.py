n = int(input("Enter the Number of Rows"))
p = 1
for i in range(n):
    q = p
    for j in range(i + 1):
        print(q, end=" ")
        q += n - j - 1
    p += 1
    print()
