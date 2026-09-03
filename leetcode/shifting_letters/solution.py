class Solution:
    # Time: O(n)
    # Space: O(n)
    def shifting_letters(self, s: str, shifts: list[int]) -> str:
        total = 0
        result = list(s)
        for i in range(len(s) - 1, -1, -1):
            total = (total + shifts[i]) % 26
            result[i] = chr((ord(result[i]) - 97 + total) % 26 + 97)
        return "".join(result)
