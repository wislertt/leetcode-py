class Solution:
    # Time: O(cost.length + 26^3 + n)
    # Space: O(26^2)
    def minimum_cost(
        self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]
    ) -> int:
        unreach = 10**18
        dist = [[unreach] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        for o, c, w in zip(original, changed, cost, strict=True):
            dist[ord(o) - 97][ord(c) - 97] = min(dist[ord(o) - 97][ord(c) - 97], w)
        for k in range(26):
            dist_k = dist[k]
            for i in range(26):
                dist_ik = dist[i][k]
                if dist_ik == unreach:
                    continue
                dist_i = dist[i]
                for j in range(26):
                    if dist_ik + dist_k[j] < dist_i[j]:
                        dist_i[j] = dist_ik + dist_k[j]
        total = 0
        for s, t in zip(source, target, strict=True):
            d = dist[ord(s) - 97][ord(t) - 97]
            if d == unreach:
                return -1
            total += d
        return total
