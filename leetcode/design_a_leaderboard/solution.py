import heapq


class Leaderboard:
    # Time: add_score O(1), top O(n log k), reset O(1)
    # Space: O(n) where n is the number of players on the leaderboard
    def __init__(self) -> None:
        self.scores: dict[int, int] = {}

    # Time: O(1)
    # Space: O(1)
    def add_score(self, player_id: int, score: int) -> None:
        self.scores[player_id] = self.scores.get(player_id, 0) + score

    # Time: O(n log k)
    # Space: O(k)
    def top(self, k: int) -> int:
        return sum(heapq.nlargest(k, self.scores.values()))

    # Time: O(1)
    # Space: O(1)
    def reset(self, player_id: int) -> None:
        del self.scores[player_id]
