from itertools import count
import itertools
import math
data=[100,200,300,400]

#itertools.count()
# print(list(zip(data,itertools.count(start=1))))

#itertools.zip_longest()
# print(list(itertools.zip_longest(range(7),data)))

#itertools.cycle
# cycle_var=itertools.cycle([x for x in range(10)])
# for i in cycle_var:
#     print(i)

# repeat_val=itertools.repeat(3,times=3)
# #repeat the same value
# for i in repeat_val:
#     print(i)


#map and starmap function
#map function
# map_val=map(math.pow,[x for x in range(10)],itertools.repeat(2))
# for i in map_val:
#     print(i)

#starmap function

starmap_val=itertools.starmap(math.pow,[(x,2) for x in range(10)])
for i in starmap_val:
    print(i)