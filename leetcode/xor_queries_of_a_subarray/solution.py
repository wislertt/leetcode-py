from itertools import accumulate


class Solution:
    def xor_queries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        prefix = [0, *accumulate(arr, lambda acc, value: acc ^ value)]
        return [prefix[right + 1] ^ prefix[left] for left, right in queries]
