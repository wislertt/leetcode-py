class Solution:
    # Time: O((n + m) * d) where d is the max digit count
    # Space: O(n * d)
    def longest_common_prefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefixes: set[str] = set()
        for x in arr1:
            s = str(x)
            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])

        best = 0
        for y in arr2:
            s = str(y)
            for i in range(best + 1, len(s) + 1):
                if s[:i] in prefixes:
                    best = i
        return best
