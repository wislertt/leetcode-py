class MyCircularDeque:
    # Fixed-size ring buffer: head is the front slot, size tracks occupancy.
    # All operations are O(1) time and the buffer holds at most k ints.
    def __init__(self, k: int) -> None:
        self.buf: list[int] = [-1] * k
        self.capacity = k
        self.size = 0
        self.head = 0

    def insert_front(self, value: int) -> bool:
        if self.is_full():
            return False
        self.head = (self.head - 1) % self.capacity
        self.buf[self.head] = value
        self.size += 1
        return True

    def insert_last(self, value: int) -> bool:
        if self.is_full():
            return False
        self.buf[(self.head + self.size) % self.capacity] = value
        self.size += 1
        return True

    def delete_front(self) -> bool:
        if self.is_empty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def delete_last(self) -> bool:
        if self.is_empty():
            return False
        self.size -= 1
        return True

    def get_front(self) -> int:
        if self.is_empty():
            return -1
        return self.buf[self.head]

    def get_rear(self) -> int:
        if self.is_empty():
            return -1
        return self.buf[(self.head + self.size - 1) % self.capacity]

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity
