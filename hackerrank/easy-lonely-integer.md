Lonely Integer (HackerRank)
===============================
### Easy
You will be given an array of integers. All of the integers except one occur twice. That one is unique in the array.

Given an array of integers, find and print the unique element.

For example, [1,2,3,4,3,2,1], the unique element is 4.

Function Description

Complete the lonelyinteger function in the editor below. It should return the integer which occurs only once in the input array.

lonelyinteger has the following parameter(s):

a: an array of integers
Input Format

The first line contains a single integer, , denoting the number of integers in the array.
The second line contains  space-separated integers describing the values in .

Constraints

It is guaranteed that  is an odd number and that there is one unique element.
, where .
Output Format

Print the unique integer in the array.

```
Sample Input 0
1
1
Sample Output 0
1
Explanation 0
There is only one element in the array, thus it is unique.
```
```
Sample Input 1
3
1 1 2
Sample Output 1
2
Explanation 1
We have two 's, and  is unique.
```
```
Sample Input 2
5
0 0 1 2 1
Sample Output 2
2
Explanation 2
We have two 's, two 's, and one .  is unique.
```
Solution
========

```python
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    result = a[0]
    for i in range(1, len(a)):
        result ^= a[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()


```
