x,y,f=map(int,input().split())
first=x*12
second=y*12+f
print(first if first<second else second)