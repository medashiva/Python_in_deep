'''
itertools - v2.3




'''

import itertools

data = [ 1, 4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]

group_by = itertools.groupby(enumerate(data),)

for i in group_by:
    print(i)
