from collections import deque


class MyStack:
    def __init__(self) -> None:
        self.queue: deque[int] = deque()

    # Time: O(n)
    # Space: O(n)
    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    # Time: O(1)
    # Space: O(1)
    def pop(self) -> int:
        return self.queue.popleft()

    # Time: O(1)
    # Space: O(1)
    def top(self) -> int:
        return self.queue[0]

    # Time: O(1)
    # Space: O(1)
    def empty(self) -> bool:
        return len(self.queue) == 0
