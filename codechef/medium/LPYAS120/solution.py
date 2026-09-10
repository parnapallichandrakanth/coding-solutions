n = int(input())
lst=[0,1]
for i in range(n-2):
    lst.append(lst[-1]+lst[-2])
for i in lst:
    print(i,end=" ")