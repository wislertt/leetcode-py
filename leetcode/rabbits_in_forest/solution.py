from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(k)
    def num_rabbits(self, answers: list[int]) -> int:
        total = 0
        for answer, count in Counter(answers).items():
            group_size = answer + 1
            total += -(-count // group_size) * group_size
        return total
