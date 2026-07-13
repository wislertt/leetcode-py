class Solution:
    # Time: O(n log(sum(weights)))
    # Space: O(1)
    def ship_within_days(self, weights: list[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            needed_days = 1
            current_load = 0
            for weight in weights:
                if current_load + weight > capacity:
                    needed_days += 1
                    current_load = 0
                current_load += weight
            return needed_days <= days

        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return left
