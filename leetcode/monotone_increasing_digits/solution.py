class Solution:
    # Time: O(d) where d is the number of digits in n
    # Space: O(d)
    def monotone_increasing_digits(self, n: int) -> int:
        digits = list(str(n))
        for i in range(len(digits) - 1):
            if digits[i] > digits[i + 1]:
                while i > 0 and digits[i - 1] == digits[i]:
                    i -= 1
                digits[i] = str(int(digits[i]) - 1)
                for j in range(i + 1, len(digits)):
                    digits[j] = "9"
                break
        return int("".join(digits))
