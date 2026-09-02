class Solution:
    # Time: O(n * 31)
    # Space: O(n * 31)
    def find_maximum_xor(self, nums: list[int]) -> int:
        root: dict[int, dict] = {}

        def insert(word: int) -> None:
            node = root
            for bit in range(30, -1, -1):
                node = node.setdefault((word >> bit) & 1, {})

        result = 0
        insert(nums[0])
        for num in nums[1:]:
            node = root
            best = 0
            for bit in range(30, -1, -1):
                key = (num >> bit) & 1
                if (1 - key) in node:
                    best |= 1 << bit
                    node = node[1 - key]
                else:
                    node = node[key]
            result = max(result, best)
            insert(num)
        return result
