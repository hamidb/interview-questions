Kth Largest Element in an Array (Leetcode #215)
===============================
### Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

### Example 1:
```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```
### Example 2:
```
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```
### Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.


Solution
========
It can also be solved using **quick select** algorithm in **O(n)**
```python
# O(nlogk)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        # keep pushing to pq until we have k elements in pq
        # after that, replace pq.lowest with the next number.
        for n in nums:
            if len(pq) < k:
                heapq.heappush(pq, n)
            else:
                if n > pq[0]:
                    heapq.heappop(pq)
                    heapq.heappush(pq, n)
        return pq[0]

``` 
