from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

def foo(num):
    for i in range(num):
        print(i)

# with ThreadPoolExecutor() as execute:
#     list_fo_obj=[execute.submit(foo, 10) for _ in range(10)]
#     all_exec=as_completed(list_fo_obj)
#     for val in all_exec:
#         val.result()

# with ThreadPoolExecutor() as execute:
#     list_of_fu_obj=list(execute.map(foo,[10 for _ in range(10)]))
#     for val in list_of_fu_obj:
#         val


print("End Of Main")