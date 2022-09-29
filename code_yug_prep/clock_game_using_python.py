# [1,5,9,11]-->10
# [4,7,8,10]-->20
# [3,2,6,12]-->30

import time 

def foo():
    all_clock_counter=0
    points=0
    points_dict1={"person":[]}
    while True:
        try:
            for i in range(13):
                print(i)
                time.sleep(1)
        except KeyboardInterrupt:
            print("new process started")
            if i in [1,5,9,11]:
                points+=10
            elif i in [4,7,8,10]:
                points+=20
            else:
                points+=30
            all_clock_counter+=1
        if all_clock_counter==3:
            points_dict1["person"]+=[points] 
            print(points_dict1)
            option=input("do you wish to continue y/n")
            if option.lower()=="y":
                all_clock_counter=0
                continue
            else:
                print(f"max value of count is {max(points_dict1['person'])}")
                break
        else:
            continue
foo()


        
