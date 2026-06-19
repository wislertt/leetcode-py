class Solution:
    # Time: O(n)
    # Space: O(n) for the carry-overflow list, O(1) extra otherwise
    def plus_one(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1, *digits]
