class Solution:
    # Time: O(n^2 * 2^n) overlap precompute plus O(n^2 * 2^n) DP over masks
    # Space: O(n * 2^n) for the parent-tracking DP table
    def shortest_superstring(self, words: list[str]) -> str:
        n = len(words)
        if n == 1:
            return words[0]

        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = words[i], words[j]
                    for k in range(min(len(a), len(b)), 0, -1):
                        if a.endswith(b[:k]):
                            overlap[i][j] = k
                            break

        size = 1 << n
        dp = [[0] * n for _ in range(size)]
        parent = [[-1] * n for _ in range(size)]
        for mask in range(1, size):
            for last in range(n):
                if not mask >> last & 1:
                    continue
                prev_mask = mask ^ (1 << last)
                if prev_mask == 0:
                    dp[mask][last] = len(words[last])
                    continue
                best_len = 10**9
                best_prev = -1
                for prev in range(n):
                    if prev_mask >> prev & 1:
                        cand = dp[prev_mask][prev] + len(words[last]) - overlap[prev][last]
                        if cand < best_len:
                            best_len = cand
                            best_prev = prev
                dp[mask][last] = best_len
                parent[mask][last] = best_prev

        full = size - 1
        last = min(range(n), key=lambda i: dp[full][i])
        order: list[int] = []
        mask = full
        while last != -1:
            order.append(last)
            prev = parent[mask][last]
            mask ^= 1 << last
            last = prev
        order.reverse()

        result = words[order[0]]
        for i in range(1, n):
            result += words[order[i]][overlap[order[i - 1]][order[i]] :]
        return result
