from __future__ import annotations

import math
from typing import ClassVar


class ImmutableListNode:
    # Test-harness API: immutable list node; print_value records the value
    printed: ClassVar[list[int]] = []

    def __init__(self, value: int, next_node: ImmutableListNode | None = None) -> None:
        self.value = value
        self.next_node = next_node

    def get_next(self) -> ImmutableListNode | None:
        return self.next_node

    def print_value(self) -> None:
        ImmutableListNode.printed.append(self.value)


class Solution:
    # Time: O(n) - one pass to slice blocks, one pass to print
    # Space: O(sqrt(n)) - one stored head per block plus per-block recursion depth
    def print_linked_list_in_reverse(self, head: ImmutableListNode) -> None:
        size = self._count(head)
        block_size = max(1, math.isqrt(size))
        heads = self._block_heads(head, block_size)
        for start in reversed(heads):
            self._print_block(start, block_size)

    def _count(self, node: ImmutableListNode | None) -> int:
        total = 0
        while node is not None:
            total += 1
            node = node.get_next()
        return total

    def _block_heads(self, head: ImmutableListNode, block_size: int) -> list[ImmutableListNode]:
        heads: list[ImmutableListNode] = []
        node: ImmutableListNode | None = head
        while node is not None:
            heads.append(node)
            for _ in range(block_size):
                nxt = node.get_next()
                if nxt is None:
                    return heads
                node = nxt
        return heads

    def _print_block(self, node: ImmutableListNode | None, remaining: int) -> None:
        if node is None or remaining == 0:
            return
        self._print_block(node.get_next(), remaining - 1)
        node.print_value()
