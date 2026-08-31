from collections import deque


class MovingAverage:
    # Time: O(1) per next call
    # Space: O(size) — window holds at most size values
    def __init__(self, size: int) -> None:
        self.size = size
        self.window: deque[int] = deque()
        self.window_sum = 0

    # Time: O(1)
    # Space: O(1)
    def next(self, val: int) -> float:
        self.window.append(val)
        self.window_sum += val
        if len(self.window) > self.size:
            self.window_sum -= self.window.popleft()
        return self.window_sum / len(self.window)
