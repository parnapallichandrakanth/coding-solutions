# Given tuple
tup = (1, 2, 3, 4, 5)
lst=[]
for i in range(len(tup)-1,-1,-1):
    lst.append(tup[i])
print(tuple(lst))