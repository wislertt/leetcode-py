class Solution:
    # Time: O(max(n, m))
    # Space: O(max(n, m))
    def add_strings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        digits: list[str] = []
        carry = 0
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += ord(num1[i]) - ord("0")
                i -= 1
            if j >= 0:
                total += ord(num2[j]) - ord("0")
                j -= 1
            carry, digit = divmod(total, 10)
            digits.append(chr(ord("0") + digit))
        return "".join(reversed(digits))
