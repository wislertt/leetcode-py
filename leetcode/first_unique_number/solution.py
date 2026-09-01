from collections import Counter, deque


class FirstUnique:
    # Time: __init__ O(n), show_first_unique amortized O(1), add O(1)
    # Space: O(n)
    def __init__(self, nums: list[int]) -> None:
        self.counts: Counter[int] = Counter(nums)
        self.queue: deque[int] = deque(nums)

    def show_first_unique(self) -> int:
        while self.queue and self.counts[self.queue[0]] != 1:
            self.queue.popleft()
        return self.queue[0] if self.queue else -1

    def add(self, value: int) -> None:
        self.counts[value] += 1
        self.queue.append(value)
