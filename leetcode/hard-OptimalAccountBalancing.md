Optimal Account Balancing (Leetcode #465)
===============================
### Hard

You are given an array of transactions transactions where `transactions[i] = [fromi, toi, amounti]` indicates that the person with `ID = fromi` gave `amounti` $ to 
the person with `ID = toi`.

Return the minimum number of transactions required to settle the debt.

 

### Example 1:
```
Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
```

### Example 2:
```
Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
Output: 1
Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, and all debt is settled.
 ```

### Constraints:
```
1 <= transactions.length <= 8
transactions[i].length == 3
0 <= fromi, toi <= 20
fromi != toi
1 <= amounti <= 100
```

Solution
========

```python
#  T: O(n x 2^n) (2^n i.e. "each item is either part of the subset or not").
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        final_balances = defaultdict(int);
        givers = [];
        creditors = [];
        ## get everyone's final balances, which might be positive or negative
        for fro, to, trans in transactions:
            final_balances[fro] -= trans;
            final_balances[to] += trans;
        for _, v in final_balances.items():
            if(v < 0):
                creditors.append(-v)
            elif(v > 0):
                givers.append(v)
        
        self.ans = float('inf')
        def recurse(creditors, givers, n = 0):
            nc = len(creditors)
            ng = len(givers)
            if(nc == 0 or ng == 0):
                self.ans = min(self.ans, n);
                return
            
            ## instead of iterating all debtors and creditors (which would have 2 loops)
            # remove the largest debt and iterate just over creditors)
            give = max(givers)
            idx = givers.index(give)
            for i in range(nc):
                credit = creditors[i]
                if(give < credit):
                    creditors[i] -= give;
                    recurse(creditors, givers[0:idx]+givers[idx+1:], n+1)
                    creditors[i] += give 
                elif(give == credit):
                    recurse(creditors[0:i]+creditors[i+1:], givers[0:idx]+givers[idx+1:], n+1)
                else:
                    givers[idx] -= credit;
                    recurse(creditors[0:i]+creditors[i+1:], givers, n+1)
                    givers[idx] += credit;
                        
        recurse(creditors, givers)
        return self.ans; 

# class Solution:
#     def minTransfers(self, transactions: List[List[int]]) -> int:
#         N = len(transactions)
#         balance = defaultdict(int)
#         for fro, to, val in transactions:
#             balance[fro] -= val
#             balance[to] += val
            
#         amounts = []
#         for k, v in (balance.items() or {}):
#             if v != 0:
#                 amounts.append(v)
                
#         def dfs(amounts, idx):
#             if idx >= len(amounts):
#                 return 0
#             curr = amounts[idx]
#             if curr == 0:  # setteled. Go to next.
#                 return dfs(amounts, idx+1)
            
#             res = float('inf')           
#             for i in range(idx+1, len(amounts)):
#                 nxt = amounts[i]
#                 if curr*nxt < 0:
#                     amounts[i] = curr + nxt
#                     res = min(res, 1+dfs(amounts, idx+1))
#                     amounts[i] = nxt
#                 elif curr + nxt == 0:  # best choice. Don't continue.
#                     break
#             return res
    
#         return dfs(amounts, 0)

# class Solution:
#     def minTransfers(self, transactions: List[List[int]]) -> int:
#         N = len(transactions)
#         balance = defaultdict(int)
#         for fro, to, val in transactions:
#             balance[fro] -= val
#             balance[to] += val
            
#         receivers = []
#         givers = []
#         for k, v in (balance.items() or {}):
#             if v < 0:
#                 receivers.append(-v)
#             elif v > 0:
#                 givers.append(v)
                
#         def dfs(receive_id, cnt):
#             if receive_id >= len(receivers):
#                 return cnt
            
#             res = float('inf')
#             for i in range(len(givers)):
#                 give = givers[i]
#                 receive = receivers[receive_id]
#                 if give >= receive:
#                     givers[i] -= receive
#                     receivers[receive_id] = receive
#                     res = min(res, dfs(receive_id+1, cnt+1))
#                     givers[i] += receive
#                     receivers[receive_id] += receive
#                 elif give > 0:
#                     givers[i] -= give
#                     receivers[receive_id] -= give
#                     res = min(res, dfs(receive_id, cnt+1))
#                     givers[i] += give
#                     receivers[receive_id] += give
#             return res
    
#         return dfs(0, 0)
```
