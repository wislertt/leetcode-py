class Solution:
    # Time: O(n)
    # Space: O(1) extra (output excluded)
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        window = abs(k)
        offset = 1 if k > 0 else -window
        total = sum(code[(offset + j) % n] for j in range(window))
        result = [0] * n
        for i in range(n):
            result[i] = total
            total += code[(i + offset + window) % n] - code[(i + offset) % n]
        return result
