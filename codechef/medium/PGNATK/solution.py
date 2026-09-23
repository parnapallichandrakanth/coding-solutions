t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    cnt=0
    work=0
    while work<n:
        cnt+=1
        if work%k!=0:
            work+=1
    print(cnt)
        
            
            
            
        
        