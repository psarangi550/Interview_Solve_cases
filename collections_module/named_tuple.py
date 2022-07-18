from collections import namedtuple
from collections import OrderedDict
import csv #importing the csv module 
import sqlite3
EmployeeRecord=namedtuple("EmployeeRecord",["eno","ename","esal","eaddr"])
emp=EmployeeRecord(eno=101,ename="rika",esal=50000,eaddr="bangalore")
emp_dict=emp._asdict()
print(emp._fields)
emp2=EmployeeRecord._make(emp_dict)
print(emp2)
print(type(emp2))
# emp2=[101,"abi",50000,"bangalore"]
# print(emp.eno)
# print(emp.ename)
# print(EmployeeRecord._make(emp2))


#reading from the csv file using the named tuple
# EmployeeRecord=namedtuple("EmployeeRecord",["eno","ename","esal","eaddr"])
# f=open("emp.csv","r")
# csv_reader=csv.reader(f)
# for emp in map(EmployeeRecord._make,csv_reader):
#     print(emp.eno,emp.ename) 
    
#reading it from the sqlite db as 
# EmployeeRecord=namedtuple("EmployeeRecord",["eno","ename","esal","eaddr"])
# conn=sqlite3.connect("db.sqlite3")
# cursor=conn.cursor()
# cursor.execute("select * from Employee;")
# for emp in map(EmployeeRecord._make,cursor.fetchall()):
#     print(emp.eno,emp.ename)