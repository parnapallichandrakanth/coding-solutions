# LPYAS80

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a Python program that reverse the given tuple and print its values.

 **Given tuple in code editor:**  (1, 2, 3, 4, 5)
 **Expected Output:**  (5, 4, 3, 2, 1)

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-10T09:06:13.840Z  

```py
# Given tuple
tup = (1, 2, 3, 4, 5)
lst=[]
for i in range(len(tup)-1,-1,-1):
    lst.append(tup[i])
print(tuple(lst))
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS80)