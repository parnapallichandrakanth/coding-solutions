# cook your dish here
T=int(input())
for _ in range(T):
    n=int(input())
    lst=[int(i) for i in str(n)]
    print(lst.count(4))