from leetcode_py import ListNode


class Solution:
    # Time: O(n + m) where n = len(nums), m = list length
    # Space: O(n) for the value set
    def modified_list(self, nums: list[int], head: ListNode[int] | None) -> ListNode[int] | None:
        drop = set(nums)
        dummy: ListNode[int] = ListNode(0)
        tail = dummy
        node = head
        while node is not None:
            nxt = node.next
            if node.val not in drop:
                tail.next = node
                tail = node
                node.next = None
            node = nxt
        return dummy.next
