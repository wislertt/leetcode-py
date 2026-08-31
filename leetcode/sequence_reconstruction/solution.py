class Solution:
    # Time: O(total sequence length)
    # Space: O(n)
    def sequence_reconstruction(self, nums: list[int], sequences: list[list[int]]) -> bool:
        pos = {v: i for i, v in enumerate(nums)}
        following: set[tuple[int, int]] = set()
        for seq in sequences:
            for i in range(len(seq) - 1):
                a, b = seq[i], seq[i + 1]
                if a not in pos or b not in pos or pos[a] >= pos[b]:
                    return False
                following.add((a, b))
        return all((nums[i], nums[i + 1]) in following for i in range(len(nums) - 1))
