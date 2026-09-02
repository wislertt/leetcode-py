class Solution:
    # Time: O(n + m)
    # Space: O(n)
    def find_champion(self, n: int, edges: list[list[int]]) -> int:
        weaker_count = [0] * n
        for _stronger, weaker in edges:
            weaker_count[weaker] += 1

        champions = [team for team in range(n) if weaker_count[team] == 0]
        return champions[0] if len(champions) == 1 else -1
