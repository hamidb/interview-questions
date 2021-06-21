1 Billion Users
===============================
### Medium

We have `N` different apps with different user growth rates. At a given time t, measured in days, the number of users using an app is `g^t`
(for simplicity we'll allow fractional users), where `g` is the growth rate for that app.
These apps will all be launched at the same time and no user ever uses more than one of the apps.
We want to know how many total users there are when you add together the number of users from each app.

After how many full days will we have 1 billion total users across the `N` apps?

### Signature
```
int getBillionUsersDay(float[] growthRates)
Input
1.0 < growthRate < 2.0 for all growth rates
1 <= N <= 1,000
Output
Return the number of full days it will take before we have a total of 1 billion users across all N apps.
```

### Example 1
```
growthRates = [1.5]
output = 52
```

### Example 2
```
growthRates = [1.1, 1.2, 1.3]
output = 79
```

### Example 3
```
growthRates = [1.01, 1.02]
output = 1047
```

Solution
========

### Jensen's inequality
Since we have exponential sequences, the biggest number is the one determining the output.

```python
def getBillionUsersDay(growthRates):
  return math.ceil(9/math.log10(max(growthRates)))
```

### same as bellow but Memoize pow function

```python
# T: O(log n) and pow function
import math
def calc_users(growthRates, t, prev_t, prev):
  prev[:] = [prev[i]*pow(g, t-prev_t) for i, g in enumerate(growthRates)]
  return sum(prev)

def getBillionUsersDay(growthRates):
  return math.ceil(9/math.log10(max(growthRates)))
  left, right = max(growthRates), min(growthRates)
  left, right = math.floor(9 / math.log10(left)), math.ceil(9 / math.log10(right))
  prev = [pow(g, left) for g in growthRates]
  mid_prev = left
  while left < right:
    mid = left + (right - left) // 2
    val = calc_users(growthRates, mid, mid_prev, prev)
    mid_prev = mid
    if val < 1e9:
      left = mid + 1
    else:
      right = mid 
```

### Simple divide and conquer
```python
# T: O(log n) and pow function
import math
# Add any helper functions you may need here
def calc_users(growthRates, t, prev_t, prev):
  #return sum([pow(g, t) for g in growthRates])

def getBillionUsersDay(growthRates):
  # Write your code here
  return math.ceil(9/math.log10(max(growthRates)))
  left, right = max(growthRates), min(growthRates)
  left, right = math.floor(9 / math.log10(left)), math.ceil(9 / math.log10(right))
  while left < right:
    mid = left + (right - left) // 2
    val = calc_users(growthRates, mid)
    mid_prev = mid
    if val < 1e9:
      left = mid + 1
    else:
      right = mid 
  return left
```
