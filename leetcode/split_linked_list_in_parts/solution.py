from leetcode_py import ListNode


class Solution:
    # Time: O(n + k)
    # Space: O(k)
    def split_list_to_parts(self, head: ListNode[int] | None, k: int) -> list[ListNode[int] | None]:
        length = 0
        node = head
        while node is not None:
            length += 1
            node = node.next

        width, remainder = divmod(length, k)
        parts: list[ListNode[int] | None] = []
        node = head
        for i in range(k):
            parts.append(node)
            if node is None:
                continue
            part_size = width + (1 if i < remainder else 0)
            for _ in range(part_size - 1):
                if node.next is not None:
                    node = node.next
            next_head = node.next
            node.next = None
            node = next_head
        return parts
