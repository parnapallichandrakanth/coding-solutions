t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    cnt=0
    i=0
    j=2
    if n<k:
        print(n)
    else:
        while i<n:
            if i==k:
                cnt+=1
                k=k*j 
                j+=1
            i+=1
            cnt+=1
        print(cnt+1)
            
            
            
        
        