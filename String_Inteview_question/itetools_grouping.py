# from itertools import groupby
# #importing the groupby function from itertools module
from itertools import tee
from itertools import accumulate
from operator import mul
Employee=[
    {
        "id":101,
        "name":"pratik",
        "sal":10000,
        "address":"bhubaneswar"
    },
    {
        "id":102,
        "name":"rika",
        "sal":60000,
        "address":"Bangalore"
    },
    {
        "id":103,
        "name":"abi",
        "sal":80000,
        "address":"Bangalore"
    }
]

# def sort_emp_by_address(emp):
#     return emp["address"]


# employee_group_address=groupby(Employee,sort_emp_by_address)

# for key ,value in employee_group_address:
#     print(key,len(list(value)))



## ****usage of tee function in itertools is *****
# copy1,cop2=tee(iter(Employee),2)
# for value in copy1:
#     print(value)


#**usage of the accumulate function in itertools is ****
# iter_mul=accumulate([1,2,3,4,5],mul)

# for item in iter_mul:
#     print(item)


#takewhile and dropwhile 

#dropwhile:-drop the values untill it hit the True response
#takewhile:-drop the values after it hit the first False response

#behave same as the filter function


