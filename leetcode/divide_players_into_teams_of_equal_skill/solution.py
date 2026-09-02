from collections import Counter


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def divide_players(self, skill: list[int]) -> int:
        n = len(skill)
        total = sum(skill)
        target, rem = divmod(total, n // 2)
        if rem:
            return -1
        counts = Counter(skill)
        chemistry = 0
        for val in sorted(counts):
            need = target - val
            if need < val:
                break
            if need == val:
                if counts[val] % 2:
                    return -1
                chemistry += val * val * (counts[val] // 2)
            elif counts[need] != counts[val]:
                return -1
            else:
                chemistry += val * need * counts[val]
        return chemistry
