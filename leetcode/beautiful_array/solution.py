class Solution:
    # Time: O(n)
    # Space: O(n)
    def beautiful_array(self, n: int) -> list[int]:
        # Divide and conquer: odds and evens of a beautiful array are each
        # beautiful, and concatenating two beautiful halves never creates a
        # bad triple since 2 * nums[k] == nums[i] + nums[j] requires nums[i]
        # and nums[j] of the same parity while k sits in the other half.
        res = [1]
        while len(res) < n:
            res = [2 * x - 1 for x in res] + [2 * x for x in res]
        return [x for x in res if x <= n]
