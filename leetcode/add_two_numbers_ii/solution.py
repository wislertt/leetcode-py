from leetcode_py import ListNode


class Solution:
    # Time: O(max(m, n))
    # Space: O(m + n)
    def add_two_numbers(
        self, l1: ListNode[int] | None, l2: ListNode[int] | None
    ) -> ListNode[int] | None:
        stack1: list[int] = []
        stack2: list[int] = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head: ListNode[int] | None = None
        while stack1 or stack2 or carry:
            digit_sum = carry
            if stack1:
                digit_sum += stack1.pop()
            if stack2:
                digit_sum += stack2.pop()
            carry, digit = divmod(digit_sum, 10)
            head = ListNode(digit, head)
        return head
