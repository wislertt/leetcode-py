class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def relative_sort_array(self, arr1: list[int], arr2: list[int]) -> list[int]:
        rank = {v: i for i, v in enumerate(arr2)}
        present = sorted((x for x in arr1 if x in rank), key=lambda x: rank[x])
        rest = sorted(x for x in arr1 if x not in rank)
        return present + rest
