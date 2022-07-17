import copy

list1 = [x * 10 for x in range(1, 5)] + [[3, 4]]

# shallow copy

list2 = copy.copy(list1)

print(id(list1[4]))
print(id(list2[4]))

if list1[4] is list2[4]:
    print("shallow copy")
else:
    print("deep copy")

# deep copy

list3 = copy.deepcopy(list1)

print(id(list1[4]))
print(id(list3[4]))

if list1[4] is list3[4]:
    print("shallow copy")
else:
    print("deep copy")
