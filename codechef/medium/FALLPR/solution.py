t=int(input())
for _ in range(t):
    l=int(input())
    arr=list(map(int,input().split()))
    s=sum(arr)
    m=min(arr)
    if s>=0:
        print("Yes")
    elif s-m>=0:
        print("Yes")
    else:
        print("No")