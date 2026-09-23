t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    cnt=0
    j=0
    lst=[]
    while n>=j*k:
        lst.append(j*k)
        j+=1
        
    for i in range(1,n+1):
        if i in lst:
            cnt+=1
        cnt+=1
    print(cnt)
        
            
            
            
        
        