Top K Frequent Words (Leetcode #692)
===============================
### Medium

Given a non-empty list of words, return the `k` most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

### Example 1:

```
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
```

### Example 2:
```
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
```

### Note:
```
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
```

### Follow up:
Try to solve it in `O(n log k)` time and `O(n)` extra space.

Solution
========

```python
# # T: O(NlogN)
# # S: O(N)
# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         def cmp(a, b):
#             if a[1] < b[1]: return 1
#             if a[1] == b[1]:
#                 if a[0] > b[0]: return 1
#                 if a[0] == b[0]: return 0
#                 return -1
#             return -1
        
#         count = defaultdict(int)
#         for word in words:
#             count[word] += 1
#         return [k for k, _ in sorted(count.items(), key=functools.cmp_to_key(cmp))[:k]]


# # T: O(Nlogk)
# # S: O(N)
# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         def cmp(a, b):
#             if a[1] < b[1]: return 1
#             if a[1] == b[1]:
#                 if a[0] > b[0]: return 1
#                 if a[0] == b[0]: return 0
#                 return -1
#             return -1
        
#         count = defaultdict(int)
#         for word in words:
#             count[word] += 1
#         ans = []
#         for item in count.items():
#             idx = self.bisect_left(ans, item, cmp)
#             if len(ans) < k:
#                 ans.insert(idx, item)
#             else:
#                 if idx < k:
#                     ans.insert(idx, item)
#                     ans.pop()
#         return [k for k, _ in ans]
                        
#     def bisect_left(self, arr, element, cmp):
#         left, right = 0, len(arr)
#         while left < right:
#             mid = (left + right) // 2
#             v = arr[mid]
#             if cmp(v, element) < 0:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left
                
# T: O(N log k)
# S: O(N)
class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    def __eq__(self, other):
        if self.freq == other.freq:
            return self.word == other.word
    def __gt__(self, other):
        if self.freq == other.freq:
            return self.word < other.word
        return self.freq > other.freq
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
class Solution(object):

    def topKFrequent(self, words, k):
        count = defaultdict(int)
        for word in words:
            count[word] += 1
        heap = []        
        for key, v in count.items():
            heapq.heappush(heap, Word(key, v))
            if len(heap) > k:
                heapq.heappop(heap)
        result = k*[None]
        for i in range(k):
            popped = heapq.heappop(heap)
            result[k-1-i] = popped.word
        return result
        
```

C++
```c++
#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

class Word {
public:
    string word;
    int freq;

    Word(string w, int f) : word(w), freq(f) {}

    // Comparator for priority queue
    bool operator<(const Word& other) const {
        if (freq == other.freq) {
            return word > other.word; // Lexicographical order for ties
        }
        return freq < other.freq; // Min-heap based on frequency
    }
};

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        // Step 1: Count frequencies
        unordered_map<string, int> count;
        for (const auto& word : words) {
            count[word]++;
        }

        // Step 2: Create a min-heap (priority queue)
        priority_queue<Word> minHeap;

        for (const auto& [key, freq] : count) {
            minHeap.push(Word(key, freq));
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }

        // Step 3: Extract top k words
        vector<string> result(k);
        for (int i = k - 1; i >= 0; --i) {
            result[i] = minHeap.top().word;
            minHeap.pop();
        }

        return result;
    }
};
```
