N=int(input())
A=list(map(int,input().split()))
M=int(input())
for i in range(len(A)):
    A[i]=A[i]//2**M 
print(A)