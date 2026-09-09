t=int(input())
for _ in range(t):
    n=int(input())
    A=input()
    B=input()
    freq_A={'a':0}
    freq_B={'b':0}
    for i in A:
        freq_A[i]=freq_A.get(i,0)+1
    for i in B:
        freq_B[i]=freq_B.get(i,0)+1
    if freq_A['a']==freq_B['b'] and freq_B['a']==freq_A['b']:
        print("YES")
    else:
        print("NO")
        