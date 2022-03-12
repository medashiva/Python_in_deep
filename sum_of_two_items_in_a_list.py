import itertools


l = [1,2,3,4,5,6,7,8]
target = 9
target_sum_list = []
for number in itertools.combinations(l,2):
    if sum(number) == target:
        target_sum_list.append(number)

print(target_sum_list)