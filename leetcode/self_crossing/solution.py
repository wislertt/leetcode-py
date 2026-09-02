class Solution:
    # Time: O(n)
    # Space: O(1)
    def is_self_crossing(self, distance: list[int]) -> bool:
        d = distance
        for i in range(3, len(d)):
            # Fourth segment crosses the first.
            if d[i] >= d[i - 2] and d[i - 3] >= d[i - 1]:
                return True
            # Fifth segment touches the first.
            if i >= 4 and d[i - 1] == d[i - 3] and d[i] + d[i - 4] >= d[i - 2]:
                return True
            # Sixth segment crosses the first after an expanding spiral contracts.
            if (
                i >= 5
                and d[i - 2] > d[i - 4]
                and d[i - 3] > d[i - 1]
                and d[i - 1] + d[i - 5] >= d[i - 3]
                and d[i] + d[i - 4] >= d[i - 2]
            ):
                return True
        return False
