class Solution:
    # Time: O(n log n) sorting plus linear DP
    # Space: O(n) for the two jump maps
    def odd_even_jumps(self, arr: list[int]) -> int:
        n = len(arr)

        def make_next(indices: list[int]) -> list[int | None]:
            # For each index j, the next index (in sorted order) greater than j:
            # its first jump target, honoring the smallest-index tie-break.
            nxt: list[int | None] = [None] * n
            stack: list[int] = []
            for i in indices:
                while stack and i > stack[-1]:
                    nxt[stack.pop()] = i
                stack.append(i)
            return nxt

        odd_next = make_next(sorted(range(n), key=lambda i: arr[i]))
        even_next = make_next(sorted(range(n), key=lambda i: -arr[i]))

        # higher[i]: a good end is reachable from i when the next jump is odd-numbered
        higher = [False] * n
        lower = [False] * n
        higher[n - 1] = lower[n - 1] = True
        for i in range(n - 2, -1, -1):
            odd_target = odd_next[i]
            if odd_target is not None:
                higher[i] = lower[odd_target]
            even_target = even_next[i]
            if even_target is not None:
                lower[i] = higher[even_target]

        return sum(higher)
