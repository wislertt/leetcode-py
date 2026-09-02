class Solution:
    # Time: O(log_7 |num|)
    # Space: O(log_7 |num|)
    def convert_to_base_7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        digits = ""
        value = abs(num)
        while value:
            digits = str(value % 7) + digits
            value //= 7
        return f"-{digits}" if negative else digits
