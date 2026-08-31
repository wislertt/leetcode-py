import heapq
from itertools import count


class Node:
    def __init__(self, val: int = 0):
        self.val = val
        self.seq = 0
        self.prev: Node = self
        self.next: Node = self


class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, val: int) -> Node:
        node = Node(val)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        return node

    @staticmethod
    def remove(node: Node) -> Node:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = node
        return node

    def pop(self) -> Node:
        return self.remove(self.tail.prev)

    def peek(self) -> int:
        return self.tail.prev.val


class MaxStack:
    # Time: push O(log n), pop O(n), top O(1),
    #       peek_max O(log n) amortized, pop_max O(log n) amortized
    # Space: O(n)
    def __init__(self):
        self.stk = DoubleLinkedList()
        self.sl: list[tuple[int, int, Node]] = []
        self.seq = count()

    def push(self, x: int) -> None:
        node = self.stk.append(x)
        node.seq = next(self.seq)
        heapq.heappush(self.sl, (-x, -node.seq, node))

    def pop(self) -> int:
        node = self.stk.pop()
        return node.val

    def top(self) -> int:
        return self.stk.peek()

    def peek_max(self) -> int:
        while True:
            neg_val, _, node = self.sl[0]
            if node.prev is not node:
                return -neg_val
            heapq.heappop(self.sl)

    def pop_max(self) -> int:
        while True:
            neg_val, _, node = heapq.heappop(self.sl)
            if node.prev is not node:
                break
        DoubleLinkedList.remove(node)
        return -neg_val
