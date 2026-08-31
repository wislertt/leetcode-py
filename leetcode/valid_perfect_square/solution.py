class Solution:
    # Time: O(log num)
    # Space: O(1)
    def is_perfect_square(self, num: int) -> bool:
        low, high = 1, num
        while low <= high:
            mid = (low + high) // 2
            squared = mid * mid
            if squared == num:
                return True
            if squared < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
