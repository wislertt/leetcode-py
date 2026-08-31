class _Node:
    __slots__ = ("next", "val")

    def __init__(self, val: int = 0, next: "_Node | None" = None) -> None:
        self.val = val
        self.next = next


class MyLinkedList:
    # Singly linked list with a sentinel head node
    # Time: get/add_at_index/delete_at_index O(index), add_at_head O(1), add_at_tail O(n)
    # Space: O(n)
    def __init__(self) -> None:
        self._head = _Node()  # sentinel
        self._size = 0

    def _node_before(self, index: int) -> _Node | None:
        """Return the node preceding position index, or None if invalid."""
        if index < 0 or index > self._size:
            return None
        node = self._head
        for _ in range(index):
            if node.next is not None:
                node = node.next
        return node

    def get(self, index: int) -> int:
        prev = self._node_before(index)
        if prev is None or prev.next is None:
            return -1
        return prev.next.val

    def add_at_head(self, val: int) -> None:
        self._head.next = _Node(val, self._head.next)
        self._size += 1

    def add_at_tail(self, val: int) -> None:
        node = self._head
        while node.next is not None:
            node = node.next
        node.next = _Node(val)
        self._size += 1

    def add_at_index(self, index: int, val: int) -> None:
        if index < 0 or index > self._size:
            return
        prev = self._node_before(index)
        if prev is not None:
            prev.next = _Node(val, prev.next)
            self._size += 1

    def delete_at_index(self, index: int) -> None:
        prev = self._node_before(index)
        if prev is not None and prev.next is not None:
            prev.next = prev.next.next
            self._size -= 1
