class NumArray:
    # Time: __init__ O(n), update O(log n), sum_range O(log n)
    # Space: O(n)
    def __init__(self, nums: list[int]) -> None:
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (self.n + 1)
        for i, value in enumerate(nums, start=1):
            self.tree[i] += value
            parent = i + (i & -i)
            if parent <= self.n:
                self.tree[parent] += self.tree[i]

    def update(self, index: int, val: int) -> None:
        self._add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sum_range(self, left: int, right: int) -> int:
        return self._prefix(right + 1) - self._prefix(left)

    def _add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def _prefix(self, i: int) -> int:
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total
