Minimum Flips to Make a OR b Equal to c(Leetcode #1318)
===============================
### Medium

Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ).
(bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

 

### Example 1:
```
Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
```
### Example 2
```
Input: a = 4, b = 2, c = 7
Output: 1
```

### Example 3:
```
Input: a = 1, b = 2, c = 3
Output: 0
```

### Constraints:
```
1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9
```

Solution
========
### counts the number of 1s in n
```
don't give up just yet, this is easier magic trick than it seems!
imagine your intiger bits are a stack of 32 playing cards, each either red or black
imagine simultaneously sliding out every other card in the deck to your left starting from the
top of the deck while maintaining all the spaces
now shift the new stack of cards on your left one space down so the cards in each deck are parallel
assuming red represents 0's and black 1's you notice if you add up each parallel pair of cards you will
have the number of black cards at each level
now imagine the process of adding each pair of cards together squeezes each pair into 1 new card labeled
with a number corresponding to the sum you just found
now squeeze the new deck of 16 cards down so there are no more spaces, and repeat the process once more
you now have 8 cards each constructed from merging 4 cards and each labeled with a number representing
the total number of black cards out of the 4
repeat this again, now you have 4 cards,
repeat this again, now you have 2 cards,
repeat this again, now you have 1 card, you notice the number on the card reads how many black cards
you had in the original deck
the magic trick is done, the audience roars in a standing ovation, pen and teller stare at you baffled 
```
```python
class Solution:
    # def minFlips(self, a: int, b: int, c: int) -> int: 
    #     cnt = 0
    #     while a  or b or c:
    #         aa = a % 2
    #         bb = b % 2
    #         cc = c % 2
    #         if aa and bb and not cc:
    #             cnt += 2
    #         elif (aa or bb) and not cc:
    #             cnt += 1
    #         elif not aa and not bb and cc:
    #             cnt += 1
    #         else:
    #             pass
    #         a //= 2
    #         b //= 2
    #         c //= 2
    #     return cnt
    
    def minFlips(self, a: int, b: int, c: int) -> int: 
        def count(n):
            a1 = 0b01010101010101010101010101010101
            a2 = 0b00110011001100110011001100110011
            a3 = 0b00001111000011110000111100001111
            a4 = 0b00000000111111110000000011111111
            a5 = 0b00000000000000001111111111111111
            n = (n & a1) + (n>>1 & a1)
            n = (n & a2) + (n>>2 & a2)
            n = (n & a3) + (n>>4 & a3)
            n = (n & a4) + (n>>8 & a4)
            return (n & a5) + (n>>16 & a5)
        diff = (a | b) ^ c
        a_one = a & diff  # from the bits that were different which are 1s in a, they must all be flipped to 0
        b_one = b & diff  # from the bits that were different which are 1s in b, they must all be flipped to 0
        zeros = ~(a|b) & diff  # from the bits that were different which zeros in both a and b, they must be flipped in either a or b
        # When we see a difference, count a's one + count b's one + count both zeros 
        return count(a_one)+count(b_one)+count(zeros)
```
