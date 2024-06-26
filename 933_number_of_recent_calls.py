"""
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

    RecentCounter() Initializes the counter with zero recent requests.
    int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

Constraints:

    1 <= t <= 10^9
    Each test case will call ping with strictly increasing values of t.
    At most 104 calls will be made to ping.
"""
from collections import deque


class RecentCounter:

    def __init__(self):
        self.range = 3000
        self.requests = deque()
        self.length = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.length += 1

        while t - self.range > self.requests[0]:
            self.requests.popleft()
            self.length -= 1

        return self.length


if __name__ == "__main__":
    obj = RecentCounter()
    assert obj.ping(1) == 1
    assert obj.ping(100) == 2
    assert obj.ping(3001) == 3
    assert obj.ping(3002) == 3

    obj = RecentCounter()
    assert obj.ping(642) == 1
    assert obj.ping(1849) == 2
    assert obj.ping(4921) == 1
    assert obj.ping(5936) == 2
    assert obj.ping(5957) == 3
