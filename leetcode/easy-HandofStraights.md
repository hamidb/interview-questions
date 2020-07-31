Hand of Straights (Leetcode #846)
===============================
### Medium

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

### Example 1:
```
Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
```

### Example 2:
```
Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
```

### Constraints:
```
1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
```

### Note:
This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

Solution
========

### Approach #1: Brute Force [Accepted]
#### Intuition
We will repeatedly try to form a group (of size W) starting with the lowest card. This works because the lowest card still in our hand must be the bottom end of a size W straight.

#### Algorithm
Let's keep a count `{card: number of copies of card}` as a TreeMap (or dict).
Then, repeatedly we will do the following steps: find the lowest value card that has 1 or more copies (say with value `x`),
and try to remove `x, x+1, x+2, ..., x+W-1` from our count. If we can't, then the task is impossible.


```python
# TimeLimitExceeded
# class Solution:
#     def isNStraightHand(self, hand: List[int], W: int) -> bool:
        
#         n = len(hand)
#         if n % W != 0: 
#             return False
#         buckets = [[] for _ in  range(n//W)]
#         return self.searchBucket(hand, W, buckets)
    
#     def searchBucket(self, nums, W, buckets):
#         if len(nums) == 0: 
#             return True
#         v = nums.pop()
#         for b in range(len(buckets)):
#             if self.canBucketHold(buckets[b], v, W):
#                 i = bisect.bisect(buckets[b], v)
#                 buckets[b].insert(i, v)
#                 if self.searchBucket(nums, W, buckets):
#                     return True
#                 buckets[b].pop(i)
#             if len(buckets[b]) == 0:
#                 break
#         nums.append(v)
#         return False
    
#     def canBucketHold(self, bucket, v, W):
#         if len(bucket) == 0:
#             return True
#         if len(bucket) == W: 
#             return False
#         if v in bucket:
#             return False
#         maxB = bucket[-1]
#         minB = bucket[0]
#         if v < minB + W and v > maxB - W:
#             return True
#         return False

# O(nlog(n))
class Solution(object):
    def isNStraightHand(self, hand, W):
        count = collections.Counter(hand)
        hand.sort() # O(nlogn)
        for m in hand:
            if count[m] == 0: continue
            for k in range(m, m+W):
                v = count[k]
                if not v: return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1
        return True
```
