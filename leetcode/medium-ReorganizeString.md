Reorganize String (Leetcode #767)
===============================
### Medium

Given a string `S`, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

### Example 1:
```
Input: S = "aab"
Output: "aba"
```

### Example 2:
```
Input: S = "aaab"
Output: ""
```

### Note:
`S` will consist of lowercase letters and have length in range `[1, 500]`.
 

Solution
========

```python
# T: O(N*A + Alog(A))
# A = 26, N = len(S)
class Solution:
    def reorganizeString(self, S: str) -> str:
        freq = Counter(S).most_common()  # sort by count
        N = len(S)
        if freq[0][1] > (N+1)/2:
            return ''
        A = list(''.join([c*t for c, t in freq]))[::-1]  # S=aaab then A=baaa
        ans = N*[None]
        ans[::2], ans[1::2] = A[N//2:], A[:N//2]
        return ''.join(ans)

# # T: O(N*log(A))
# # A = 26, N = len(S)
# class Solution:
#     def reorganizeString(self, S: str) -> str:
#         max_heap = [(-cnt, c) for c, cnt in Counter(S).items()]
#         heapq.heapify(max_heap)
#         if -max_heap[0][0] > (len(S)+1) // 2:
#             return ''
        
#         ans = ''
#         while len(max_heap) >= 2:
#             cnt1, c1 = heapq.heappop(max_heap)
#             cnt2, c2 = heapq.heappop(max_heap)
#             if not ans or c1 != ans[-1]:
#                 ans += c1+c2
#             else: 
#                 ans += c2+c1
#             if cnt1+1: heapq.heappush(max_heap, (cnt1+1, c1))
#             if cnt2+1: heapq.heappush(max_heap, (cnt2+1, c2))
#         return ans + (max_heap[0][1] if max_heap else '')
```

