class Solution:
    # Time: O(n)
    # Space: O(1)
    def judge_circle(self, moves: str) -> bool:
        x = 0
        y = 0
        for move in moves:
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "L":
                x -= 1
            else:
                x += 1
        return x == 0 and y == 0
