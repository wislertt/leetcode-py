import bisect


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def longest_obstacle_course(self, obstacles: list[int]) -> list[int]:
        tails: list[int] = []
        result: list[int] = []
        for height in obstacles:
            pos = bisect.bisect_right(tails, height)
            if pos == len(tails):
                tails.append(height)
            else:
                tails[pos] = height
            result.append(pos + 1)
        return result
