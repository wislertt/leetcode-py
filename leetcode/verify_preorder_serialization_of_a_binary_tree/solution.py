class Solution:
    # Time: O(n)
    # Space: O(1)
    def is_valid_serialization(self, preorder: str) -> bool:
        slots = 1
        for token in preorder.split(","):
            if slots <= 0:
                return False
            if token == "#":
                slots -= 1
            else:
                slots += 1
        return slots == 0
