class Solution:
    # Time: O(n)
    # Space: O(1)
    def escape_ghosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        my_dist = abs(target[0]) + abs(target[1])
        return all(
            abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) > my_dist for ghost in ghosts
        )
