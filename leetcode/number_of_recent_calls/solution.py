from collections import deque


class RecentCounter:
    # Time: O(1) amortized per ping call
    # Space: O(W) where W is the number of requests in the current 3000ms window
    def __init__(self) -> None:
        self.requests: deque[int] = deque()

    # Time: O(1) amortized (each timestamp is appended and popped at most once)
    # Space: O(1) beyond the stored window
    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)
