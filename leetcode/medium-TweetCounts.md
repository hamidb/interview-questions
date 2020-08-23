Tweet Counts Per Frequency (Leetcode #1348)
===============================
### Medium
Implement the class TweetCounts that supports two methods:

* recordTweet(string tweetName, int time):

  &emsp;&emsp; Stores the tweetName at the recorded time (in seconds).

* getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime)

&emsp;&emsp; Returns the total number of occurrences for the given tweetName per minute, hour, or day (depending on freq) starting from the startTime (in seconds) and ending at the endTime (in seconds).

freq is always minute, hour or day, representing the time interval to get the total number of occurrences for the given tweetName.
The first time interval always starts from the startTime, so the time intervals are `[startTime, startTime + delta*1>,  [startTime + delta*1, startTime + delta*2>, [startTime + delta*2, startTime + delta*3>, ... , [startTime + delta*i, min(startTime + delta*(i+1), endTime + 1)>` for some non-negative number i and delta (which depends on freq).  
 

### Example:
```
Input
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

Output
[null,null,null,null,[2],[2,1],null,[4]]
```
Explanation
```
TweetCounts tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 0);
tweetCounts.recordTweet("tweet3", 60);
tweetCounts.recordTweet("tweet3", 10);                             // All tweets correspond to "tweet3" with recorded times at 0, 10 and 60.
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // return [2]. The frequency is per minute (60 seconds), so there is one interval of time: 1) [0, 60> - > 2 tweets.
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // return [2, 1]. The frequency is per minute (60 seconds), so there are two intervals of time: 1) [0, 60> - > 2 tweets, and 2) [60,61> - > 1 tweet.
tweetCounts.recordTweet("tweet3", 120);                            // All tweets correspond to "tweet3" with recorded times at 0, 10, 60 and 120.
tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // return [4]. The frequency is per hour (3600 seconds), so there is one interval of time: 1) [0, 211> - > 4 tweets.
```

### Constraints:

There will be at most 10000 operations considering both recordTweet and getTweetCountsPerFrequency.

`0 <= time, startTime, endTime <= 10^9`

`0 <= endTime - startTime <= 10^4`

Solution
========
```python
class TweetCounts:
    def __init__(self):
        self.table = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if self.table.get(tweetName) is None:
            self.table[tweetName] = [time]
        else:
            self.table[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.table:
            return []
        occurrence = self.table[tweetName] 
        occurrence.sort()
        delta = 1
        if freq == "minute":
            delta = 60
        if freq == "hour":
            delta = 60*60
        if freq == "day":
            delta = 60*60*24
            
        hist = []
        start = startTime
        for i in range(startTime, endTime+1, delta):
            counter = 0
            for c in occurrence:
                if c < i:  # interval has not yet started
                    continue
                if c >= i + delta:  # outside [start-finish) interval
                    break
                if c < min(endTime+1, i+delta):  # if endTime < i+delta  then c can be endTime
                    counter += 1
            hist.append(counter)
            start += delta
        return hist
        

# class TweetCounts:

#     def __init__(self):
#         self.dt = collections.defaultdict(list)

#     def recordTweet(self, tweetName: str, time: int) -> None:
#         bisect.insort(self.dt[tweetName], time)

#     def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int):
#         dt = 1 * 60 if freq == 'minute' else 60 * 60 if freq == 'hour' else 3600 * 60
#         rst, timeline = [], self.dt[tweetName]
#         for i in range(startTime, endTime+1, dt): 
#             rst.append(bisect.bisect_left(timeline, min(i+dt, endTime+1)) - bisect.bisect_left(timeline, i))
#         return rst
                
# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
```
