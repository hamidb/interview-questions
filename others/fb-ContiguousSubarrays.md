Contiguous Subarrays
===============================
### Facebook

You are given an array arr of `N` integers. For each index `i`, you are required to determine the number of contiguous subarrays that fulfill the following conditions:

* The value at index `i` must be the maximum element in the contiguous subarrays, and
* These contiguous subarrays must either start from or end on index `i`.

### Signature
```
int[] countSubarrays(int[] arr)
Input
Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
Size N is between 1 and 1,000,000
Output
An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]
```

### Example:
```
arr = [3, 4, 1, 6, 2]
output = [1, 3, 1, 5, 1]
Explanation:
For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
For index 1 - [4], [3, 4], [4, 1]
For index 2 - [1]
For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
For index 4 - [2]
So, the answer for the above input is [1, 3, 1, 5, 1]
```

Solution
========

```python
# O(n) solution
def count_subarrays(arr):
  # Write your code here
  # T: O(N)
  res = len(arr) * [1]
  
  # for each i, find the nearest smaller element to the i's left. 
  stack = []
  for i in range(len(arr)):
    while stack and arr[i] > arr[stack[-1]]:
      stack.pop()
    if len(stack) == 0:
      res[i] += i
    else:
      res[i] += i - stack[-1] - 1
    stack.append(i)
      
  # for each i, find the nearest smaller element to the i's right.
  stack = []
  for i in range(len(arr)-1, -1, -1):
    while stack and arr[i] > arr[stack[-1]]:
      stack.pop()
    if len(stack) == 0:
      res[i] += len(arr) - 1 - i 
    else:
      res[i] += stack[-1] - i - 1
    stack.append(i)
    
  return res

```
