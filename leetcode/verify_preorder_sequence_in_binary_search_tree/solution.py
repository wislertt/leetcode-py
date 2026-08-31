class Solution:
    # Time: O(n)
    # Space: O(n)
    def verify_preorder(self, preorder: list[int]) -> bool:
        stack: list[int] = []
        last_popped = float("-inf")
        for value in preorder:
            if value < last_popped:
                return False
            while stack and stack[-1] < value:
                last_popped = stack.pop()
            stack.append(value)
        return True
