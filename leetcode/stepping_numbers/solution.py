from collections import deque


class Solution:
    # Time: O(2^log(high)) - at most ~10k stepping numbers below 2 * 10^9
    # Space: O(2^log(high)) for the queue
    def count_stepping_numbers(self, low: int, high: int) -> list[int]:
        ans: list[int] = []
        if low == 0:
            ans.append(0)
        q: deque[int] = deque(range(1, 10))
        while q:
            v = q.popleft()
            if v > high:
                break
            if v >= low:
                ans.append(v)
            last = v % 10
            if last > 0:
                q.append(v * 10 + last - 1)
            if last < 9:
                q.append(v * 10 + last + 1)
        return ans
