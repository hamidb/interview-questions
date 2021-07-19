Shortest Way to Form String (Leetcode #1055)
===============================
### Medium 

From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target.
If the task is impossible, return `-1`.

 

### Example 1:
```
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
```

### Example 2:
```
Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
```

### Example 3:
```
Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 ```

### Constraints:
```
Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.
```

Solution
========
```python
# T: O(MxN)
# S: O(1)
#class Solution:
#    def shortestWay(self, source: str, target: str) -> int:
#        if len(target) == 0:
#            return 0
#        idx = source.find(target[0])
#        if idx == -1: 
#            return -1
#        
#        s = idx + 1  # continue searchin starting from 's'
#        t = 1  # go to the second target character
#        while s < len(source) and t < len(target):
#            idx = source.find(target[t], s)
#            if idx == -1:  # if not found, break and try the remaining characters.
#                break
#            t += 1  # otherwise, increment the length of subsequence by 1
#            s = idx+1  # and search starting from the next source character
#        
#        # we are out of the loop. meaning we either couldn't find,
#        # or reached the end of target.
#        # So repeat the process with target[t:end] (t = length of biggest subsequence)
#        remaining = self.shortestWay(source, target[t:])
#        if remaining == -1:
#            return remaining
#        return remaining+1
        
# T: O(log(M)xN)
# S: O(N)        
    def shortestWay(self, source: str, target: str) -> int:
        #2 pointer solution
        dic = collections.defaultdict(list)
        for i, c in enumerate(source):
            dic[c].append(i)
        ans =1
        j=0
        i=-1
        while j<len(target):
            c= target[j]
            if c not in dic: return -1
            pos = bisect.bisect_right(dic[c], i)
            if pos >= len(dic[c]):
                i= -1
                ans+=1
                continue
            else: 
                i = dic[c][pos]
                j+=1
        return ans
```
