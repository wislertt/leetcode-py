class Solution:
    # Time: O(n)
    # Space: O(1)
    def winner_of_game(self, colors: str) -> bool:
        alice = 0
        bob = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == "A":
                    alice += 1
                else:
                    bob += 1
        return alice > bob
