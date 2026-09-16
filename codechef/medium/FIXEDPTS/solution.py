t=int(input())
for _ in range(k):
    n,k=map(int,input().split())
    if n-k==1:
        print("No")
    else:
        print("Yes")