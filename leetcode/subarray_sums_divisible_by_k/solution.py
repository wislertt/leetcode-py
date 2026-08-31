class Solution:
    # Time: O(n)
    # Space: O(k)
    def subarrays_div_by_k(self, nums: list[int], k: int) -> int:
        mod_count: dict[int, int] = {0: 1}
        prefix_mod = 0
        count = 0
        for num in nums:
            prefix_mod = (prefix_mod + num) % k
            count += mod_count.get(prefix_mod, 0)
            mod_count[prefix_mod] = mod_count.get(prefix_mod, 0) + 1
        return count
