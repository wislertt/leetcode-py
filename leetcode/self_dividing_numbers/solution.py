class Solution:
    # Time: O((right - left + 1) * log10(right))
    # Space: O(1) extra (output excluded)
    def self_dividing_numbers(self, left: int, right: int) -> list[int]:
        def is_self_dividing(num: int) -> bool:
            remaining = num
            while remaining > 0:
                digit = remaining % 10
                if digit == 0 or num % digit != 0:
                    return False
                remaining //= 10
            return True

        return [num for num in range(left, right + 1) if is_self_dividing(num)]
