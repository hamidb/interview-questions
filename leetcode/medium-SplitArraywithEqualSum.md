Split Array with Equal Sum (Leetcode #548)
===============================
### Medium
Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

`0 < i, i + 1 < j, j + 1 < k < n - 1`
Sum of subarrays `(0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1)` should be equal.
where we define that subarray `(L, R)` represents a slice of the original array starting from the element indexed `L` to the element indexed `R`.

### Example:
```
Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
```

### Note:
```
1 <= n <= 2000.
Elements in the given array will be in range [-1,000,000, 1,000,000].
```

Solution
========
### Approach #5 Using Cumulative Sum and HashSet [Accepted]
#### Algorithm
In this approach, firstly we form a cumulative sum array sumsum, where `sum[i]sum[i]` stores the cumulative sum of the array numsnums upto the i_th index. Then, we start by traversing over the possible positions for the middle cut formed by `j`. 
For every `j`, firstly, we find all the left cut's positions, `i`, that lead to equalizing the sum of the first and the second part (i.e. `sum[i-1] = sum [j-1] - sum[i]sum[i−1]=sum[j−1]−sum[i]`) and 
store such sums in the setset (a new HashSet is formed for every `j` chosen). Thus, the presence of a sum in setset implies that such a sum is possible for having
equal sum of the first and second part for the current position of the middle `cut(j)`.

Then, we go for the right cut and find the position of the right cut that leads to equal sum of the third and the fourth part
(`sum[n-1]-sum[k]=sum[k-1] - sum[j]sum[n−1]−sum[k]=sum[k−1]−sum[j]`), for the same middle cut as chosen earlier. 
We also, look if the same sum exists in the setset. If so, such a triplet `(i, j, k)` exists which satisfies the required criteria, otherwise not.

### Python
```python
class Solution:
#     # O(N^3)
#     def splitArray(self, nums: List[int]) -> bool:
#         sums = {}
#         N = len(nums)
#         c_sum = [nums[0]]
#         for i in range(1, N):
#             c_sum.append(c_sum[i-1] + nums[i])

#         for i in range(1, N-5):
#             s1 = sums.get((0, i-1))
#             if s1 is None:
#                 s1 = sums[(0, i-1)] = c_sum[i-1]
#             for j in range(i+2, N-3):
#                 s2 = sums.get((i+1, j-1))
#                 if s2 is None:
#                     s2 = sums[(i+1, j-1)] = c_sum[j-1]-c_sum[i]
#                 if s1 != s2: continue
#                 for k in range(j+2, N-1):
#                     s3 = sums.get((j+1, k-1))
#                     if s3 is None:
#                         s3 = sums[(j+1, k-1)] = c_sum[k-1]-c_sum[j]
#                     if s2 != s3: continue
#                     s4 = sums.get((k+1, N-1))
#                     if s4 is None:
#                         s4 = sums[(k+1, N-1)] = c_sum[N-1]-c_sum[k]
#                     if s4 == s3: return True
#         return False
    
    # O(N^2)
    def splitArray(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 7:
            return False
        c_sum = [nums[0]]
        for i in range(1, N):
            c_sum.append(c_sum[i-1] + nums[i])

        for j in range(3, N-3):
            set_j = set()
            for i in range(1, j-1):
                s1 = c_sum[i-1]
                s2 = c_sum[j-1] - c_sum[i]
                if s1 != s2:
                    continue
                set_j.add(s1)                    
            for k in range(j+2, N-1):
                s3 = c_sum[k-1] - c_sum[j]
                s4 = c_sum[N-1] - c_sum[k]
                if s4 != s3: continue
                if s4 in set_j:
                    return True
        return False
```

### C++
```c++
class Solution {
public:
    bool splitArray(vector<int>& nums) {
        if (nums.size() < 7) return false;
        int N = nums.size();
        int* sums = new int[N];
        sums[0] = nums[0];
        for (int i=1; i < N; ++i) {
            sums[i] = sums[i-1] + nums[i];
        }
        for (int j=3; j < N-3; ++j) {
            std::unordered_set<int> set;
            for (int i=1; i < j-1; ++i) {
                auto s1 = sums[i-1];
                auto s2 = sums[j-1] - sums[i];
                if (s1 != s2) continue;
                set.emplace(s1);
            }
            for (int k=j+2; k < N-1; ++k) {
                auto s3 = sums[k-1] - sums[j];
                auto s4 = sums[N-1] - sums[k];
                if (s3 != s4) continue;
                if (set.count(s3) != 0) {
                    delete[] sums;
                    return true;  
                } 
            }
        }
        delete[] sums;
        return false;
    }
};

```
