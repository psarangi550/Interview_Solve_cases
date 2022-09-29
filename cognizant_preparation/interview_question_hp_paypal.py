import csv
from operator import itemgetter
def foo():
    result={}
    temp=[]
    with open("/mnt/c/Users/611903295/Downloads/coding_folder/emp.csv","r") as csv_file:
        reader=csv.reader(csv_file)
        next(reader)
        for line in reader:
           result[line[0]]=temp.append({"date":line[1],"salary":int(line[2])})
        print(result)

# for i in range(10):
#     foo(i)

foo()