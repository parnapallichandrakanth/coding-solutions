N=int(input())
A=list(map(int,input().split()))
M=int(input())
for i in A:
    i=i//2**M 
print(A)