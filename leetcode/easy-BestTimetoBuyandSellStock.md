Best Time to Buy and Sell Stock (Leetcode #121)
===============================
### Easy

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

### Example 1:
```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```             
### Example 2:

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

### Solution

![O(n) approach](images/image0002.png)

```python
class Solution:
#  O(n^2)
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) == 0 or len(prices) == 1:
#             return 0
        
#         l = len(prices)
#         max_p = 0
#         for i in range(l-1): # 0 ... l-2
#             for j in range(i+1, l): # i+1 ... l-1
#                 if prices[i] >= prices[j]:
#                     continue
#                 else:
#                     if max_p < prices[j] - prices[i]:
#                         max_p = prices[j] - prices[i]          
#         return max_p
        
#  O(n)
        def maxProfit(self, prices: List[int]) -> int:
            max_profit = 0
            min_buy = 0xffffffff
            for x in prices:
                if x < min_buy:
                    min_buy = x
                elif x - min_buy > max_profit:
                    max_profit = x - min_buy
            return max_profit
```
