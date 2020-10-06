Missing Element in Sorted Array (Leetcode #1060)
===============================
### Medium

Given a sorted array `A` of unique numbers, find the `K`-th missing number starting from the leftmost number of the array.


### Example 1:
```
Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
```

### Example 2:
```
Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
```

### Example 3:
```
Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
 ```

### Note:
```
1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8
```


Solution
========
### Hint1:
First define a function `f(x)` that counts the number of missing elements until `x`.

### Hint2:
Then use binary search with the given function `f(x)` to find the `k`th missing element.

```python
# T: O(logn)
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
    
        def missing(x):
            return nums[x] - nums[0] - x
        
        n = len(nums)
        if k > missing(n-1):
            return nums[-1] + (k-missing(n-1)) # how many steps needed after nums[-1]  
        
        lo, hi = 0, n-1
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            if missing(mid) < k:
                lo = mid+1
            else:
                hi = mid-1
        return nums[lo-1] + k - missing(lo-1)
```
