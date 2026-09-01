class Solution:
    # Time: O(n * log(sum(sweetness)))
    # Space: O(1)
    def maximize_sweetness(self, sweetness: list[int], k: int) -> int:
        def can_eat(target: int) -> bool:
            current = pieces = 0
            for sweet in sweetness:
                current += sweet
                if current >= target:
                    current = 0
                    pieces += 1
            return pieces > k

        low, high = 0, sum(sweetness)
        while low < high:
            mid = (low + high + 1) // 2
            if can_eat(mid):
                low = mid
            else:
                high = mid - 1
        return low
