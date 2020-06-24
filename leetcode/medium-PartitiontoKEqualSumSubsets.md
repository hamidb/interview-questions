Partition to K Equal Sum Subsets (Leetcode #698)
===============================
### Medium
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

### Example 1:

```
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 ```

### Note:

```
1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
```

Solution
========

### Explanation
Approach #1: Search by Constructing Subset Sums [Accepted]
Intuition

As even when k = 2, the problem is a "Subset Sum" problem which is known to be NP-hard, (and because the given input limits are low,) our solution will focus on exhaustive search.

A natural approach is to simulate the k groups (disjoint subsets of nums). For each number in nums, we'll check whether putting it in the i-th group solves the problem. We can check those possibilities by recursively searching.

Algorithm

Firstly, we know that each of the k group-sums must be equal to `target = sum(nums) / k`. (If this quantity is not an integer, the task is impossible.)

For each number in nums, we could add it into one of `k` group-sums, as long as the group's sum would not exceed the target. For each of these choices, we recursively search with one less number to consider in nums. If we placed every number successfully, then our search was successful.

One important speedup is that we can ensure all the 0 values of each group occur at the end of the array groups, by enforcing `if (groups[i] == 0) break`. This greatly reduces repeated work - for example, in the first run of search, we will make only 1 recursive call, instead of k. Actually, we could do better by skipping any repeated values of `groups[i]`, but it isn't necessary.

Another speedup is we could sort the array nums, so that we try to place the largest elements first. When the answer is true and involves subsets with a low size, this method of placing elements will consider these lower size subsets sooner. We can also handle `elements nums[i] >= target` appropriately. These tricks are not necessary to solve the problem, but they are presented in the solutions below.

```python
class Solution(object):
# Time Complexity: O(k^{N-k} k!), where N is the length of nums. As we skip additional zeroes in groups, naively we will make O(k!) calls to search, then an additional O(k^{N-k}) calls after every element of groups is nonzero.
# Space Complexity: O(N), the space used by recursive calls to search in our call stack.

    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if group == 0: break
            nums.append(v)
            return False

        nums.sort()
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        return search([0] * k)
```     
