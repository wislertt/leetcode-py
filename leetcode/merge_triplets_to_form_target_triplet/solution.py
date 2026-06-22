class Solution:
    # Time: O(n)
    # Space: O(1)
    def merge_triplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        tx, ty, tz = target
        found_x = found_y = found_z = False

        for a, b, c in triplets:
            # Skip any triplet that would push a component past the target.
            if a > tx or b > ty or c > tz:
                continue
            if a == tx:
                found_x = True
            if b == ty:
                found_y = True
            if c == tz:
                found_z = True
            if found_x and found_y and found_z:
                return True

        return found_x and found_y and found_z
