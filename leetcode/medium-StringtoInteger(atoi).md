String to Integer (atoi) (Leetcode #8)
===============================
### Medium

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").

Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.

Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.

Rounding: If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, then round the integer to remain in the range. Specifically, integers less than `-2^31` should be rounded to `-2^31`, and integers greater than `2^31 - 1` should be rounded to `2^31 - 1`.

Return the integer as the final result.

 

### Example 1:
```
Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
```

### Example 2:
```
Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
```

### Example 3:
```
Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
```

### Example 4:
```
Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^
```

### Example 5:
```
Input: s = "words and 987"

Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.
```
 

### Constraints:
```
0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
```

### Solution
Python
```python
# class Solution:
#     def myAtoi(self, s: str) -> int:        
#         MAX = 2**31-1
#         i = 0
#         sign = 1
#         start = True
#         num = 0
#         while i < len(s):
#             if start:
#                 if s[i] == " ":
#                     pass        
#                 elif s[i] in "0123456789":
#                     # check before overflow
#                     if sign == -1 and num >= (MAX+1 - int(s[i])) / 10:
#                         return -MAX-1
#                     if sign == 1 and num >= (MAX - int(s[i])) / 10:
#                         return MAX
#                     num = num*10 + int(s[i])                    
#                     start = False
#                 elif s[i] in "-+":
#                     sign = -1 if s[i] == "-" else 1
#                     start = False
#                 else:
#                     break
#             else:
#                 if s[i] in "0123456789":
#                     if sign == -1 and num >= (MAX+1 - int(s[i])) / 10:
#                         return -MAX-1
#                     if sign == 1 and num >= (MAX - int(s[i])) / 10:
#                         return MAX    
#                     num = num*10 + int(s[i])
#                 else:
#                     break
#             i+=1
        
#         return num*sign        

class Solution:
    def myAtoi(self, s: str) -> int:        
        MAX = 2**31-1
        i = 0
        sign = 1
        start = True
        num = 0
        while i < len(s):
            if start and s[i] == " ":
                i += 1
                continue                    
            elif s[i] in "0123456789":
                # check before overflow
                if sign == -1 and num >= (MAX+1 - int(s[i])) / 10:
                    return -MAX-1
                if sign == 1 and num >= (MAX - int(s[i])) / 10:
                    return MAX
                num = num*10 + int(s[i])
            elif start and s[i] in "-+":
                sign = -1 if s[i] == "-" else 1
            else:
                break
            start = False
            i+=1
        
        return num*sign        
```

C++ 
```c++
class Solution {
public:
    int myAtoi(string s) {
        int i = 0;
        int sign = 1;
        bool start = true;
        int num = 0;

        while (i < s.size()) {            
            if (start && s[i] == ' ') {
                i++;
                continue;
            }
            auto integer = s[i] - '0';
            if (integer <= 9 && integer >= 0) {
                if (sign == -1 && num > (INT_MAX-integer) / 10) {
                    return INT_MIN;
                }
                if (sign == 1 && num > (INT_MAX-integer) / 10) {
                    return INT_MAX;
                }
                num = num*10 + integer;
            } else if (start && (s[i] == '-' || s[i] == '+')) {
                sign = s[i] == '-' ? -1 : 1;
            } else {
                break;
            }
            start = false;
            i++;
        }
        return num*sign;
    }
};
```
