Bulls and Cows (Leetcode #299)
===============================
### Medium

You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically,
the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as `"xAyB"`, where `x` is the number of bulls and `y` is the number of cows. Note that both secret and guess may contain duplicate digits.

 

### Example 1:
```
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
```

### Example 2:
```
Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
```

### Example 3:
```
Input: secret = "1", guess = "0"
Output: "0A0B"
```

### Example 4:
```
Input: secret = "1", guess = "1"
Output: "1A0B"
 ```

### Constraints:
```
1 <= secret.length, guess.length <= 1000
secret.length == guess.length
secret and guess consist of digits only.
```
Solution
========

### Approach 2: One Pass
#### Intuition

Let's optimize approach `1` by building the hashmap during the strings' parsing. That would allow us to reduce the number of passes to one.

#### Algorithm

Initialize the number of bulls and cows to zero.
Initialize the hashmap to count characters. During the iteration, secret string gives a positive contribution, and guess - negative contribution.

Iterate over the strings: `s` is the current character in the string secret and `g` - the current character in the string guess.

* If `s == g`, update bulls counter: `bulls += 1`.

* Otherwise, if `s != g`:

* Update cows by adding `1` if so far guess contains more `s` characters than secret: `h[s] < 0`.

* Update cows by adding `1` if so far secret contains more `g` characters than guess: `h[g] > 0`.

* Update the hashmap by marking the presence of `s` character in the string secret: `h[s] += 1`.

* Update the hashmap by marking the presence of `g` character in the string guess: `h[g] -= 1`.

 * Return the number of bulls and cows.

```python
# One pass O(N)
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        table = defaultdict(int)
        bulls, cows = 0, 0
        for g, s in zip(guess, secret):
            if g == s:
                bulls += 1
            else:
                # we increment cows if:
                #  1. we had more s in guess than in secret
                #  2. we had more g in secret than in guess
                #        more s in guess     more g in secret
                cows += int(table[s] < 0) + int(table[g] > 0) 
                table[s] += 1
                table[g] -= 1
        return str(bulls) + 'A' + str(cows) + 'B'
    
# one pass O(N) with array
# same as above
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         bulls, cows = 0, 0
#         arr = 10 * [0]
#         zero = ord('0')
#         for g, s in zip(guess, secret):
#             if g == s:
#                 bulls += 1
#             else:
#                 s = ord(s) - zero
#                 g = ord(g) - zero
#                 cows += int(arr[s] < 0) + int(arr[g] > 0) 
#                 arr[s] += 1
#                 arr[g] -= 1
#         return str(bulls) + 'A' + str(cows) + 'B'

# 2 pass O(N)
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         counter = Counter(secret)
#         bulls, cows = 0, 0
#         for i, c in enumerate(guess):
#             if c in counter:
#                 if c == secret[i]:
#                     bulls += 1
#                     cows -= int(counter[c] <= 0)
#                 else:
#                     cows += int(counter[c] > 0)
#                 counter[c] -= 1
#         return str(bulls) + 'A' + str(cows) + 'B'
    
```
