class Solution:
    # Time: O(n * sqrt(max(nums)) * alpha(n))
    # Space: O(max(nums))
    def largest_component_size(self, nums: list[int]) -> int:
        parent: dict[int, int] = {}

        def find(x: int) -> int:
            root = x
            while parent[root] != root:
                root = parent[root]
            while parent[x] != root:
                parent[x], x = root, parent[x]
            return root

        def union(a: int, b: int) -> None:
            if b not in parent:
                parent[b] = b
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                parent[root_a] = root_b

        for num in nums:
            parent[num] = num

        for num in nums:
            reduced = num
            factor = 2
            while factor * factor <= reduced:
                if reduced % factor == 0:
                    union(num, factor)
                    while reduced % factor == 0:
                        reduced //= factor
                factor += 1
            if reduced > 1:
                union(num, reduced)

        sizes: dict[int, int] = {}
        largest = 0
        for num in nums:
            root = find(num)
            sizes[root] = sizes.get(root, 0) + 1
            largest = max(largest, sizes[root])
        return largest
