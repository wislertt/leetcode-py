class Solution:
    # Time: O(n + e)
    # Space: O(n + e)
    def loud_and_rich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        n = len(quiet)
        graph: list[list[int]] = [[] for _ in range(n)]
        for a, b in richer:
            graph[b].append(a)

        answer: list[int] = [-1] * n

        def dfs(x: int) -> int:
            if answer[x] != -1:
                return answer[x]
            best = x
            for y in graph[x]:
                cand = dfs(y)
                if quiet[cand] < quiet[best]:
                    best = cand
            answer[x] = best
            return best

        return [dfs(i) for i in range(n)]
