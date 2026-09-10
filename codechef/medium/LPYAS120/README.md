# LPYAS120

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program to generate and print the  **Fibonacci series**  up to the  **$N$th term**  using a for-loop.

The  **Fibonacci series**  is the sequence where each number is the  **sum of the previous two numbers of the sequence** 

The number at the  **nth position**  can be represented by:
 **Fn = Fn-1 + Fn-2** 
where,
 **F0 = 0 and F1 = 1** 

Check the sample input / output below for further clarity.

### Sample 1:
Input
Output

```
10
```

```
0 1 1 2 3 5 8 13 21 34 
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-10T09:13:14.176Z  

```py
n = int(input())
lst=[0,1]
for i in range(n-2):
    lst.append(lst[-1]+lst[-2])
for i in lst:
    print(i,end=" ")
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS120)