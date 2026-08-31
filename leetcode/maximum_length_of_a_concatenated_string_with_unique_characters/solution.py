class Solution:
    # Time: O(2^n * n) worst case
    # Space: O(n)
    def max_len(self, arr: list[str]) -> int:
        masks: list[int] = []
        for s in arr:
            mask = 0
            for char in s:
                bit = 1 << (ord(char) - ord("a"))
                if mask & bit:
                    break
                mask |= bit
            else:
                masks.append(mask)
        best = 0

        def dfs(i: int, current: int) -> None:
            nonlocal best
            best = max(best, current.bit_count())
            for j in range(i, len(masks)):
                if not (current & masks[j]):
                    dfs(j + 1, current | masks[j])

        dfs(0, 0)
        return best
