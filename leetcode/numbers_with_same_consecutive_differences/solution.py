class Solution:
    # Time: O(2^n * n) over digit sequences of length n
    # Space: O(2^n) for the answer
    def nums_same_consec_diff(self, n: int, k: int) -> list[int]:
        digits = list(range(1, 10))
        for _ in range(n - 1):
            nxt: list[int] = []
            for num in digits:
                last = num % 10
                if last + k <= 9:
                    nxt.append(num * 10 + last + k)
                if k and last - k >= 0:
                    nxt.append(num * 10 + last - k)
            digits = nxt
        return digits
