Design Twitter (Leetcode #355)
===============================
### Medium

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

* `Twitter()` Initializes your twitter object.
* `void postTweet(int userId, int tweetId)` Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
* `List<Integer> getNewsFeed(int userId)` Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
* `void follow(int followerId, int followeeId)` The user with ID followerId started following the user with ID followeeId.
* `void unfollow(int followerId, int followeeId)` The user with ID followerId started unfollowing the user with ID followeeId.
 

### Example 1:
```
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
``` 

### Constraints:
```
1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 104
All the tweets have unique IDs.
At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
```

Solution
========

```python
class Twitter:

    def __init__(self):
        """ Initialize your data structure here. """
        self.connections = defaultdict(set)
        self.posts = defaultdict(deque)
        self.cnt = 0  # act as timestamp

    def postTweet(self, userId: int, tweetId: int) -> None:
        """ Compose a new tweet. """
        self.follow(userId, userId)
        user_posts = self.posts[userId]
        user_posts.insert(0, (self.cnt, tweetId))
        if len(user_posts) > 10:
            user_posts.pop()
        
        self.cnt += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """ Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent."""
        ans = []
        pq = []
        for followee in self.connections[userId]:
            tweets = self.posts[followee]
            if tweets:
                # add first (most recent) tweets of all followers to pq.
                # append(-count, tweetid, userId, currIdx)
                pq.append((-tweets[0][0], tweets[0][1], followee, 0))
        heapq.heapify(pq)
        k = 10
        while pq:
            if k == 0:
                return ans
            count, tweetId, userId, idx = heapq.heappop(pq)
            ans.append(tweetId)
            if idx+1 < len(self.posts[userId]):
                tweet = self.posts[userId][idx+1]
                heapq.heappush(pq, (-tweet[0], tweet[1], userId, idx+1))
            k -= 1
        return ans
                
    def follow(self, followerId: int, followeeId: int) -> None:
        """ Follower follows a followee. If the operation is invalid, it should be a no-op. """
        self.connections[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """ Follower unfollows a followee. If the operation is invalid, it should be a no-op. """
        if followeeId in self.connections[followerId]:
            self.connections[followerId].remove(followeeId)
            
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
```
