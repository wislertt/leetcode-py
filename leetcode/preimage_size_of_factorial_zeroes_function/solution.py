class Solution:
    # Time: O(log^2 k)
    # Space: O(1)
    def preimage_size_fzf(self, k: int) -> int:
        def zeroes(x: int) -> int:
            count = 0
            power = 5
            while power <= x:
                count += x // power
                power *= 5
            return count

        def first_with_at_least(target: int) -> int:
            low, high = 0, 5 * (target + 1)
            while low < high:
                mid = (low + high) // 2
                if zeroes(mid) >= target:
                    high = mid
                else:
                    low = mid + 1
            return low

        left = first_with_at_least(k)
        if zeroes(left) != k:
            return 0
        return first_with_at_least(k + 1) - left
