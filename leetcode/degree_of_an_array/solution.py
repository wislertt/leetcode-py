class Solution:
    # Time: O(n)
    # Space: O(n)
    def find_shortest_sub_array(self, nums: list[int]) -> int:
        first: dict[int, int] = {}
        last: dict[int, int] = {}
        count: dict[int, int] = {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1
        degree = max(count.values())
        return min(last[num] - first[num] + 1 for num in count if count[num] == degree)
