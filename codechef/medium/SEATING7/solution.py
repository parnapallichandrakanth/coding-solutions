t=int(input())
for _ in range(t):
    N,M,K=map(int,input().split())
    A=list(map(int,input().split()))
    ans=[]
    j=0
    for i in range(1,N+1):
        if j==K:
            break
        if i not in A:
            print(i,end=" ")
            j+=1
    print()
        