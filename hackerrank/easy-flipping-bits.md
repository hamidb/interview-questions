Flipping bits (HackerRank)
===============================
### Easy
![Problem Statement](./pdfs/flipping-bits-English.pdf)

Solution
========
```python
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    max_int = 0xFFFFFFFF
    return max_int - n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
    
```

