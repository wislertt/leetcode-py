class Solution:
    # Time: O(log(buckets))
    # Space: O(1)
    def poor_pigs(self, buckets: int, minutes_to_die: int, minutes_to_test: int) -> int:
        states = minutes_to_test // minutes_to_die + 1
        pigs = 0
        covered = 1
        while covered < buckets:
            covered *= states
            pigs += 1
        return pigs
