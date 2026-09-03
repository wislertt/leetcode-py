from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(m) for the nums set
    def num_components(self, head: ListNode[int] | None, nums: list[int]) -> int:
        values = set(nums)
        count = 0
        in_component = False
        node = head
        while node is not None:
            if node.val in values:
                if not in_component:
                    count += 1
                    in_component = True
            else:
                in_component = False
            node = node.next
        return count
