Isomorphic Strings (Leetcode #205)
===============================
### Easy
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

### Example 1:
```
Input: s = "egg", t = "add"
Output: true
```
### Example 2:
```
Input: s = "foo", t = "bar"
Output: false
```
### Example 3:
```
Input: s = "paper", t = "title"
Output: true
```
### Note:
You may assume both s and t have the same length.

Solution
========
```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == t: return True
        if s == "" or t == "": return False
        table = {}
        seen = {}
        for i in range(len(s)):
            tc, sc = t[i], s[i]
            if sc in table:
                if table[sc] != tc:
                    return False
            else:
                if tc in seen:
                    return False
                table[sc] = tc
                seen[tc] = 1
        return True
```

### **C++**
```c++
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int L = s.size();
        std::unordered_map<char, char> table;
        std::set<char> seen;
        if (L == 0)
            return (t.size() == L);
        for (int i=0; i < L; ++i) {
            int si = s[i], ti = t[i];
            if (table.count(si) != 0) {
                if (table[si] != ti)
                    return false;
            } else {
                if (seen.count(ti) == 1)
                    return false;
                table[si] = ti;
                seen.insert(ti);
            }
        }
        return true;
    }
};
```
