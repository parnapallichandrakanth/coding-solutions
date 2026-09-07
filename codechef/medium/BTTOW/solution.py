N,K=map(int,input().split())
A=list(map(int,input().split()))
for i in range(len(A)):
    if A[i]-K>0:
        A[i]-=K 
    else:
        A[i]+=K 
print(A)
        