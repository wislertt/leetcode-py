class Solution:
    # Time: O(n)
    # Space: O(1)
    def decode_at_index(self, s: str, k: int) -> str:
        size = 0
        for char in s:
            size = size * int(char) if char.isdigit() else size + 1

        for char in reversed(s):
            k %= size
            if k == 0 and char.isalpha():
                return char
            if char.isdigit():
                size //= int(char)
            else:
                size -= 1
        raise ValueError("k out of range")
