Longest Duplicate Substring (Leetcode #1044)
===============================
### Hard

Given a string `s`, consider all duplicated substrings: (contiguous) substrings of `s` that occur `2` or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If `s` does not have a duplicated substring, the answer is "".

 

### Example 1:
```
Input: s = "banana"
Output: "ana"
```

### Example 2:
```
Input: s = "abcd"
Output: ""
```

### Constraints:
```
2 <= s.length <= 3 * 104
s consists of lowercase English letters.
```

Solution
========
```python
hash of "cli"
L = 3
q = 1001
base = 26

hash = ('c' * 26^2) + ('l' * 26^1) + ('i' * 26^0) % 1001
hash[0] = 0
hash[i+1] = (hash[i] * base) % q
```

```python
# T: O(NlogN)
# S: O(N)
# Binary search + Rabin-Karp 
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # Rabin-Karp to search duplicate occurence of any substring.
        # or to search if substring t of length exists in s.
        # T: O(N)
        # S: O(N)

        BASE = 27
        MOD = 10**9+7
        n = len(s)
        HASH = [0] * (n+1)
        POW = [1] * (n+1)
        for i, c in enumerate(s):
            HASH[i+1] = (HASH[i] * BASE + ord(c)-ord('a')) % MOD
            POW[i+1] = (POW[i] * BASE) % MOD
            
        def getHash(left, right):
            return (HASH[right+1] - HASH[left+1] * POW[right-left] + MOD * MOD) % MOD
         
        def getAns(size):
            seen = defaultdict(list)
            for i in range(n-size+1):
                h = getHash(i, i+size-1)
                if h in seen:
                    orgStr = s[i:i+size]
                    for j in seen[h]:
                        if orgStr == s[j:j+size]:
                            return orgStr
                seen[h].append(i)
            return None
        
        ans = ""
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            tmp = getAns(mid)
            if tmp != None:
                ans = tmp
                left = mid + 1
            else:
                right = mid - 1
        return ans

# # T: O(NlogN)
# # S: O(N)
# # Binary search + Rabin-Karp 
class Solution:
    def longestDupSubstring(self, s: str) -> str:

        def check_rabin_karp(l):
            base, mod = 256, 10**9+7
            h, P = 0, base**(l-1)%mod

            for i in range(l):
                h = (h * base + ord(s[i])) % mod

            seen = defaultdict(list)
            seen[h] = [0]

            for i in range(len(s)-l):
                ss = s[i+1:i+l+1]
                h = ((h - ord(s[i])*P)*base + ord(s[i+l])) % mod
                if h < 0: h += mod
                for j in seen[h]:
                    if s[j:j+l] == ss:
                        return ss
                seen[h].append(i+1)

            return None
        
        ans, lo, hi = "", 0, len(s)
        while lo < hi:
            mid = (lo+hi)//2
            duplicate = check_rabin_karp(mid)
            
            if duplicate:
                lo = mid+1
                ans = duplicate
            else:
                hi = mid
                
        return ans
```
