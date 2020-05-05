Forming a Magic Square (HackerRank)
===============================
### Medium
We define a magic square to be an nxn matrix of distinct positive integers from 1 to 9 where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

You will be given a 3x3 matrix s of integers in the inclusive range [1-9].
We can convert any digit a to any other digit b in the range [1-9] at cost of `|a-b|`.
Given s, convert it into a magic square at minimal cost. Print this cost on a new line.

*Note*: The resulting magic square must contain distinct integers in the inclusive range .

For example, we start with the following matrix:
```
5 3 4
1 5 8
6 4 2
```
We can convert it to the following magic square:
```
8 3 4
1 5 9
6 7 2
```
This took three replacements at a cost of `|5-8|+|8-9|+|4-7|`

*Function Description*

Complete the formingMagicSquare function in the editor below.
It should return an integer that represents the minimal total cost of converting the input square to a magic square.

`formingMagicSquare` has the following parameter(s):

s: a 3x3 array of integers
Input Format

Each of the lines contains three space-separated integers of row s[i].

Constraints

Output Format

Print an integer denoting the minimum cost of turning matrix  into a magic square.

Sample Input 0
```
4 9 2
3 5 7
8 1 5
```
Sample Output 0

1
Explanation 0

If we change the bottom right value, , from  to  at a cost of ,  becomes a magic square at the minimum possible cost.

Sample Input 1
```
4 8 2
4 5 7
6 1 6
```
Sample Output 1

4
Explanation 1

Using 0-based indexing, if we make

-> at a cost of 
-> at a cost of 
-> at a cost of ,
then the total cost will be .

Solution
========
![explanation](images/image0006.png)

```python
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    # All possible cases
    pre =  [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]], 
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]

    results = []
    for p in pre:
        total = 0
        for r in range(3):
            for c in range(3):
                total += abs(s[r][c]-p[r][c])
        results.append(total)
    return min(results)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()


```
