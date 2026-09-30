t=int(input())
for _ in range(t):
    N,M,K=map(int,input().split())
    A=list(map(int,input().split()))
    ans=[]
    for i in range(1,N+1):
        if i not in A:
            print(i,end=" ")
    print()
        