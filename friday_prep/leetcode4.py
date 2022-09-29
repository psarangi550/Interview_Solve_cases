list1=[["B","C"],["D","B"],["C","A"]]

a,b=map(set,zip(*list1))

print(a)

print(b)
