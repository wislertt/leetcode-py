class MyCircularQueue:
    # Time: O(1) per operation
    # Space: O(k)
    def __init__(self, k: int) -> None:
        self.capacity = k
        self.data: list[int] = [0] * k
        self.head = 0
        self.size = 0

    # Time: O(1)
    # Space: O(1)
    def en_queue(self, value: int) -> bool:
        if self.is_full():
            return False
        tail_index = (self.head + self.size) % self.capacity
        self.data[tail_index] = value
        self.size += 1
        return True

    # Time: O(1)
    # Space: O(1)
    def de_queue(self) -> bool:
        if self.is_empty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    # Time: O(1)
    # Space: O(1)
    def front(self) -> int:
        if self.is_empty():
            return -1
        return self.data[self.head]

    # Time: O(1)
    # Space: O(1)
    def rear(self) -> int:
        if self.is_empty():
            return -1
        tail_index = (self.head + self.size - 1) % self.capacity
        return self.data[tail_index]

    # Time: O(1)
    # Space: O(1)
    def is_empty(self) -> bool:
        return self.size == 0

    # Time: O(1)
    # Space: O(1)
    def is_full(self) -> bool:
        return self.size == self.capacity
