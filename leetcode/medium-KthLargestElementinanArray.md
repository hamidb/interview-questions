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
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest 
        return select(0, len(nums) - 1, len(nums) - k)
```

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
