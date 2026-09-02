class Solution:
    # Time: O(1)
    # Space: O(1)
    def number_of_matches(self, n: int) -> int:
        # Each match eliminates exactly one team, and all but the winner are
        # eliminated, so n - 1 matches are played regardless of pairing rules.
        return n - 1
