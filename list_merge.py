l = [1,2,3]
l1 = [4,5,6]

l2 = []

for i in l:
    for k in l1:
        if i not in l2:
            l2.append(i)
        if k not in l2:
            l2.append(k)
            

print(list(set(l+l2)))
print(l2)
