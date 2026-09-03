class Solution:
    # Time: O(log(target))
    # Space: O(1)
    def broken_calc(self, start_value: int, target: int) -> int:
        ops = 0
        while target > start_value:
            if target % 2:
                target += 1
            else:
                target //= 2
            ops += 1
        return ops + start_value - target
