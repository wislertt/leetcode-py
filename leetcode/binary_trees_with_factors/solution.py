class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def num_factored_binary_trees(self, arr: list[int]) -> int:
        mod = 10**9 + 7
        vals = sorted(arr)
        index = {v: i for i, v in enumerate(vals)}
        count_for: dict[int, int] = {}
        total = 0
        for i, v in enumerate(vals):
            ways = 1
            for j in range(i):
                if v % vals[j]:
                    continue
                complement = v // vals[j]
                if complement in index and index[complement] < i:
                    ways += count_for[vals[j]] * count_for[complement]
            count_for[v] = ways
            total += ways
        return total % mod
