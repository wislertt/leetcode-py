class Solution:
    # Time: O(C(n,k) * k)
    # Space: O(C(n,k) * k)
    def combine(self, n: int, k: int) -> list[list[int]]:
        result: list[list[int]] = []
        current: list[int] = []

        def backtrack(start: int) -> None:
            if len(current) == k:
                result.append(current[:])
                return

            # Prune: stop early if not enough remaining numbers to reach k
            for num in range(start, n - (k - len(current)) + 2):
                current.append(num)
                backtrack(num + 1)
                current.pop()

        backtrack(1)
        return result
