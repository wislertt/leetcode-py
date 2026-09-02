class Solution:
    # Time: O(2^n)
    # Space: O(1) extra space, excluding the output list
    def gray_code(self, n: int) -> list[int]:
        result = [0]
        for i in range(n):
            result.extend(value | (1 << i) for value in reversed(result))
        return result
