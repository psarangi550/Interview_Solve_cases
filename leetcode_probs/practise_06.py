# list1=[10,20,10,30,40,50]
# result=[]
# for i in range(len(list1)-1,-1,-1):
#     result.append(list1[i])
# print(result)

list1=[10,20,10,30,40,50]

#alternate approach 

# def foo(list1):
#     n=len(list1)
#     for i in range(n//2):
#         if list1[n-1-i]>list1[i]:
#             list1[i],list1[n-1-i] = list1[n-1-i],list1[i]
#     return list1

# print(foo(list1))
# input=[
#     {"name":"Rohan","location":"l1"},
#     {"name":"Mohan","location":"l2"},
#     {"name":"Nitin","location":"l1"},
#     {"name":"Arjun","location":"l3"},
#     {"name":"Mohit","location":"l2"},
# ]

# dict1={}
# for ele in input:
#     # print(ele)
#     if ele['location'] not in dict1:
#         dict1[ele['location']]=[ele]
#     else:
#         dict1[ele['location']].append(ele)
# print(dict1)

import csv #importing the csv module 
result=[]
with open("emp.csv","r") as csv_file:
    csv_reader=csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        # print(line)
        if int(line[2])>35000:
            line[3]=str(int(line[3])+200)
            result.append(line)
            
            
print(result)

def foo(list1):
    with open("emp_new.csv", "w") as csv_write:
        csv_writer = csv.writer(csv_write)
        csv_writer.writerow(["empid","dates","salary","bonus"])
        for item in list1:
            csv_writer.writerow(item)

foo(result)
#     
#     csv_writer.writerow()





































