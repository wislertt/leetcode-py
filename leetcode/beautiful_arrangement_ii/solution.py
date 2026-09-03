class Solution:
    # Zig-zag the first k+1 values between the low and high ends: the k gaps of that
    # prefix are exactly k, k-1, ..., 1, then a plain ascending run keeps only 1.
    # Time: O(n)
    # Space: O(1) extra besides the output list
    def construct_array(self, n: int, k: int) -> list[int]:
        result: list[int] = []
        low, high = 1, k + 1
        while low < high:
            result.extend([low, high])
            low += 1
            high -= 1
        if low == high:
            result.append(low)
        result.extend(range(k + 2, n + 1))
        return result
