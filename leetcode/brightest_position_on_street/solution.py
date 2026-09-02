class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def brightest_position(self, lights: list[list[int]]) -> int:
        diff: dict[int, int] = {}
        for pos, rng in lights:
            diff[pos - rng] = diff.get(pos - rng, 0) + 1
            diff[pos + rng + 1] = diff.get(pos + rng + 1, 0) - 1

        best = 0
        brightness = 0
        best_pos = 0
        for point in sorted(diff):
            brightness += diff[point]
            if brightness > best:
                best = brightness
                best_pos = point
        return best_pos
