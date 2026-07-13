class Solution:
    # Time: O(n + t) where t = len(trust)
    # Space: O(n)
    def find_judge(self, n: int, trust: list[list[int]]) -> int:
        # Net trust score: indegree - outdegree. Judge must reach n - 1.
        trust_score = [0] * (n + 1)
        for truster, trusted in trust:
            trust_score[truster] -= 1
            trust_score[trusted] += 1

        for person in range(1, n + 1):
            if trust_score[person] == n - 1:
                return person
        return -1
