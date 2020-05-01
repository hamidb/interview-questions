Group Anagrams (Leetcode #49)
===============================
### Medium
Given an array of strings, group anagrams together.

### Example:

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```
### Note:
All inputs will be in lowercase.
The order of your output does not matter.

Solution
========
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # more easily append elements to dict of lists
        result = collections.defaultdict(list)
        for s in strs:
            result[''.join(sorted(s))].append(s)  # Use sorted (string) elements as the hash key.
        return result.values()
```
