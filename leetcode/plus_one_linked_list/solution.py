from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def plus_one(self, head: ListNode[int] | None) -> ListNode[int] | None:
        dummy = ListNode(0)
        dummy.next = head
        # rightmost node not equal to 9
        last_not_nine = dummy
        node = head
        while node is not None:
            if node.val != 9:
                last_not_nine = node
            node = node.next
        last_not_nine.val += 1
        node = last_not_nine.next
        while node is not None:
            node.val = 0
            node = node.next
        return dummy if last_not_nine is dummy else head
