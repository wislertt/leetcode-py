from collections import deque


class PhoneDirectory:
    # Time: O(1) per operation
    # Space: O(max_numbers)
    def __init__(self, max_numbers: int) -> None:
        self.free = deque(range(max_numbers))
        self.free_set = set(range(max_numbers))

    def get(self) -> int:
        if not self.free:
            return -1
        number = self.free.popleft()
        self.free_set.remove(number)
        return number

    def check(self, number: int) -> bool:
        return number in self.free_set

    def release(self, number: int) -> None:
        if number not in self.free_set:
            self.free_set.add(number)
            self.free.append(number)
