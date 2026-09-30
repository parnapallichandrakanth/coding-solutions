t=int(input())
N,M=map(int,input().split())
for _ in range(t):
    if N%2==0 or M%2==0:
        print("Yes")
    else:
        print("No")