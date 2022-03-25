lst = [1, 2, 3, 4, 5, 7, 8]
missing_list = []
for i in range(lst[0],lst[-1]+1):
    if i not in lst:
        missing_list.append(i)

print(missing_list)